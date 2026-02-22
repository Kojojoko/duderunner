"""
COMPLETE Mamitha Sheet Normalization
- Row 1: 4 running frames (ALL SAME SIZE)
- Row 2 Frame 3: Jump frame (crouch pose)
- Row 3: Death/hit frame
All frames normalized to EXACT same dimensions
"""
from PIL import Image
import os

# Paths
assets_dir = r"c:\Users\Kumaresa pandiyan\OneDrive\Documents\duderunner\assets"
input_path = os.path.join(assets_dir, "mamitha_sheet.png")
output_path = os.path.join(assets_dir, "mamitha_sheet_normalized.png")

# Target dimensions (matching hero_sheet_normalized.png EXACTLY)
TARGET_FRAME_WIDTH = 439
TARGET_FRAME_HEIGHT = 878

print("="*60)
print("COMPLETE MAMITHA SHEET NORMALIZATION WITH DEATH FRAME")
print("="*60)
print(f"Loading {input_path}...")
img = Image.open(input_path)
print(f"Original size: {img.size[0]}x{img.size[1]}")
print(f"Target frame size: {TARGET_FRAME_WIDTH}x{TARGET_FRAME_HEIGHT}")

if img.mode != 'RGBA':
    img = img.convert('RGBA')

# Frame coordinates from analysis
# Row 1: Running frames (4 frames)
run_frames_coords = [
    {'name': 'run0', 'x': 26, 'y': 159, 'w': 370, 'h': 580},
    {'name': 'run1', 'x': 461, 'y': 159, 'w': 241, 'h': 580},
    {'name': 'run2', 'x': 746, 'y': 159, 'w': 346, 'h': 580},
    {'name': 'run3', 'x': 1127, 'y': 159, 'w': 409, 'h': 580},
]

# Row 2 Frame 3: Jump frame (crouch/jump down pose)
jump_frame_coord = {'name': 'jump', 'x': 770, 'y': 992, 'w': 304, 'h': 816}

# Row 3: Death/hit frame
death_frame_coord = {'name': 'death', 'x': 614, 'y': 2126, 'w': 334, 'h': 424}

all_frames = run_frames_coords + [jump_frame_coord, death_frame_coord]

print(f"\nExtracting and normalizing {len(all_frames)} frames...")
print(f"  Row 1: 4 running frames (will be SAME SIZE)")
print(f"  Row 2 Frame 3: 1 jump frame (crouch pose)")
print(f"  Row 3: 1 death frame (hit obstacle)")
print("-"*60)

normalized_frames = []

# Find the maximum dimensions from ALL frames to ensure consistency
max_original_width = max(f['w'] for f in all_frames)
max_original_height = max(f['h'] for f in all_frames)
print(f"Max original dimensions: {max_original_width}x{max_original_height}")

for frame_info in all_frames:
    # Extract the frame
    box = (
        frame_info['x'],
        frame_info['y'],
        frame_info['x'] + frame_info['w'],
        frame_info['y'] + frame_info['h']
    )
    frame = img.crop(box)
    
    # Create normalized canvas - EXACT size for ALL frames
    normalized = Image.new("RGBA", (TARGET_FRAME_WIDTH, TARGET_FRAME_HEIGHT), (0, 0, 0, 0))
    
    # Calculate scaling to fit target dimensions while maintaining aspect ratio
    frame_w, frame_h = frame.size
    
    # Use the SAME scale for all frames based on max dimensions
    scale = min(TARGET_FRAME_WIDTH / max_original_width, TARGET_FRAME_HEIGHT / max_original_height)
    
    new_w = int(frame_w * scale)
    new_h = int(frame_h * scale)
    
    # Resize frame
    frame = frame.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # Position: center horizontally, align to bottom vertically
    x_offset = (TARGET_FRAME_WIDTH - new_w) // 2
    y_offset = TARGET_FRAME_HEIGHT - new_h
    
    # Paste onto normalized canvas
    normalized.paste(frame, (x_offset, y_offset), frame)
    normalized_frames.append(normalized)
    
    print(f"  {frame_info['name']}: {frame_w}x{frame_h} -> {new_w}x{new_h} @ scale {scale:.3f}")

# Create final spritesheet
# Layout: Row 1 = 4 run frames, Row 2 = jump + death (2 frames)
num_run_frames = 4
sheet_width = TARGET_FRAME_WIDTH * num_run_frames  # 1756
sheet_height = TARGET_FRAME_HEIGHT * 2  # 1756

print(f"\nCreating spritesheet: {sheet_width}x{sheet_height}")
print("-"*60)

new_sheet = Image.new("RGBA", (sheet_width, sheet_height), (0, 0, 0, 0))

# Row 1: Run frames
for i in range(4):
    x_pos = i * TARGET_FRAME_WIDTH
    new_sheet.paste(normalized_frames[i], (x_pos, 0))
    print(f"  run{i} placed at ({x_pos}, 0)")

# Row 2: Jump frame (left side) and Death frame (right side)
jump_x = TARGET_FRAME_WIDTH  # Position 1 (second slot)
death_x = TARGET_FRAME_WIDTH * 2  # Position 2 (third slot)

new_sheet.paste(normalized_frames[4], (jump_x, TARGET_FRAME_HEIGHT))
print(f"  jump placed at ({jump_x}, {TARGET_FRAME_HEIGHT})")

new_sheet.paste(normalized_frames[5], (death_x, TARGET_FRAME_HEIGHT))
print(f"  death placed at ({death_x}, {TARGET_FRAME_HEIGHT})")

# Save
print(f"\nSaving to {output_path}...")
new_sheet.save(output_path, optimize=True)

# Statistics
original_size = os.path.getsize(input_path)
final_size = os.path.getsize(output_path)
reduction = (1 - final_size / original_size) * 100

print("\n" + "="*60)
print("✓ SUCCESS!")
print("="*60)
print(f"Output file: mamitha_sheet_normalized.png")
print(f"Dimensions: {sheet_width}x{sheet_height}")
print(f"File size: {final_size / (1024*1024):.2f} MB (was {original_size / (1024*1024):.2f} MB)")
print(f"Reduction: {reduction:.1f}%")
print("\nFrame layout:")
print("  Row 1: 4 running frames (ALL SAME SIZE)")
print("  Row 2: jump + death frames")
print("\nFrame coordinates:")
print(f"  run0: ({0}, {0})")
print(f"  run1: ({TARGET_FRAME_WIDTH}, {0})")
print(f"  run2: ({TARGET_FRAME_WIDTH*2}, {0})")
print(f"  run3: ({TARGET_FRAME_WIDTH*3}, {0})")
print(f"  jump: ({jump_x}, {TARGET_FRAME_HEIGHT})")
print(f"  death: ({death_x}, {TARGET_FRAME_HEIGHT})")
print("\n✓ All frames SAME size - Ready with death animation!")
print("="*60)
