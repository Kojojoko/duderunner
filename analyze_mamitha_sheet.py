"""
Advanced analyzer for mamitha_sheet to detect individual animation frames.
This script will help us better understand the frame structure.
"""
from PIL import Image
import os

# Paths
assets_dir = r"c:\Users\Kumaresa pandiyan\OneDrive\Documents\duderunner\assets"
input_path = os.path.join(assets_dir, "mamitha_sheet.png")

print(f"Analyzing {input_path}...")
img = Image.open(input_path)
width, height = img.size

print(f"Original size: {width}x{height}")

if img.mode != 'RGBA':
    img = img.convert('RGBA')

data = img.load()

# Find rows of content
def find_horizontal_regions(image):
    """Find horizontal regions (rows) with content"""
    width, height = image.size
    data = image.load()
    
    has_content = []
    for y in range(height):
        row_has_content = False
        for x in range(width):
            if data[x, y][3] > 0:
                row_has_content = True
                break
        has_content.append(row_has_content)
    
    # Find regions
    regions = []
    in_region = False
    start_y = 0
    
    for y in range(height):
        if has_content[y] and not in_region:
            start_y = y
            in_region = True
        elif not has_content[y] and in_region:
            if y - start_y > 20:  # Minimum height threshold
                regions.append((start_y, y))
            in_region = False
    
    if in_region:
        regions.append((start_y, height))
    
    return regions

# Find vertical regions within a row
def find_frames_in_row(image, row_start, row_end):
    """Find individual frames within a row"""
    width, height = image.size
    data = image.load()
    
    has_content = []
    for x in range(width):
        col_has_content = False
        for y in range(row_start, min(row_end, height)):
            if data[x, y][3] > 0:
                col_has_content = True
                break
        has_content.append(col_has_content)
    
    # Find regions with gap threshold
    regions = []
    in_region = False
    start_x = 0
    gap_size = 0
    min_gap = 15  # Minimum gap between frames
    
    for x in range(width):
        if has_content[x]:
            if not in_region:
                start_x = x
                in_region = True
                gap_size = 0
            else:
                gap_size = 0
        elif in_region:
            gap_size += 1
            if gap_size >= min_gap:
                regions.append((start_x, x - gap_size))
                in_region = False
    
    if in_region:
        regions.append((start_x, width))
    
    return regions

print("\n" + "="*60)
print("ROW ANALYSIS:")
print("="*60)

rows = find_horizontal_regions(img)
print(f"Found {len(rows)} rows with content:\n")

all_frames = []
for i, (start_y, end_y) in enumerate(rows):
    row_height = end_y - start_y
    print(f"Row {i+1}:")
    print(f"  Y range: {start_y} to {end_y}")
    print(f"  Height: {row_height}px")
    
    frames = find_frames_in_row(img, start_y, end_y)
    print(f"  Frames: {len(frames)}")
    
    for j, (start_x, end_x) in enumerate(frames):
        frame_width = end_x - start_x
        print(f"    Frame {j+1}: x={start_x}-{end_x}, width={frame_width}px")
        all_frames.append({
            'row': i + 1,
            'frame': j + 1,
            'x': start_x,
            'y': start_y,
            'width': frame_width,
            'height': row_height,
            'box': (start_x, start_y, end_x, end_y)
        })
    print()

print("="*60)
print(f"TOTAL FRAMES DETECTED: {len(all_frames)}")
print("="*60)

# Show recommended frames to use
print("\nRECOMMENDATION:")
print("-" * 60)
if len(all_frames) >= 5:
    print(f"✓ Detected {len(all_frames)} frames")
    print("  You can select which frames to use for:")
    print("    - 4 frames for running animation")
    print("    - 1 frame for jump pose")
    print("\n  Sample frame coordinates:")
    for i in range(min(8, len(all_frames))):
        f = all_frames[i]
        print(f"    Frame {i+1} (Row {f['row']}): x={f['x']}, y={f['y']}, size={f['width']}x{f['height']}")
else:
    print(f"⚠ Only detected {len(all_frames)} frames")
    print("  The script will use the available frames and duplicate as needed")

print("\nTo manually select frames, edit normalize_mamitha_sheet.py")
print("and specify the frame coordinates from above.")
