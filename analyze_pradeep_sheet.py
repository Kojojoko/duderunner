"""
Analyze pradeep_sheet.png to find the death frame
"""
from PIL import Image
import os

path = r"c:\Users\Kumaresa pandiyan\OneDrive\Documents\duderunner\assets\pradeep_sheet.png"
img = Image.open(path)

print("="*60)
print("ANALYZING PRADEEP_SHEET.PNG FOR DEATH FRAME")
print("="*60)
print(f"Image size: {img.size}")

# Convert to RGBA if needed
if img.mode != 'RGBA':
    img = img.convert('RGBA')

# Get the alpha channel to find non-transparent regions
alpha = img.split()[-1]
pixels = alpha.load()

width, height = img.size

# Find all non-transparent regions by scanning rows
print("\nScanning for content rows...")
print("-"*60)

content_rows = []
current_row_start = None

for y in range(height):
    has_content = False
    for x in range(width):
        if pixels[x, y] > 10:  # Not fully transparent
            has_content = True
            break
    
    if has_content:
        if current_row_start is None:
            current_row_start = y
    else:
        if current_row_start is not None:
            content_rows.append((current_row_start, y - 1, y - current_row_start))
            current_row_start = None

if current_row_start is not None:
    content_rows.append((current_row_start, height - 1, height - current_row_start))

print(f"Found {len(content_rows)} content row groups:")
for i, (start, end, h) in enumerate(content_rows, 1):
    print(f"  Row {i}: y={start:4} to {end:4} (height: {h:4}px)")

# Now find frames in the last row (death frame should be there)
if len(content_rows) >= 3:
    print(f"\nAnalyzing Row 3 (death frame):")
    print("-"*60)
    row_start, row_end, row_height = content_rows[2]
    
    # Scan for horizontal content regions in this row
    content_cols = []
    current_col_start = None
    
    for x in range(width):
        has_content = False
        for y in range(row_start, row_end + 1):
            if pixels[x, y] > 10:
                has_content = True
                break
        
        if has_content:
            if current_col_start is None:
                current_col_start = x
        else:
            if current_col_start is not None:
                content_cols.append((current_col_start, x - 1, x - current_col_start))
                current_col_start = None
    
    if current_col_start is not None:
        content_cols.append((current_col_start, width - 1, width - current_col_start))
    
    print(f"Found {len(content_cols)} frame(s) in Row 3:")
    for i, (start, end, w) in enumerate(content_cols, 1):
        print(f"  Frame {i}: x={start:4} to {end:4}, width={w:4}px")
        print(f"           Box: ({start}, {row_start}, {w}, {row_height})")

print("\n" + "="*60)
print("USE THESE COORDINATES FOR DEATH FRAME!")
print("="*60)
