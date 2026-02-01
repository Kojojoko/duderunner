from PIL import Image
import sys

def analyze_row1(path):
    img = Image.open(path)
    width, height = img.size
    
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    data = img.load()
    
    # Row 1 Approx Y range: 58 to 695
    y_start = 58
    y_end = 695
    
    non_empty_cols = []
    
    for x in range(width):
        has_content = False
        for y in range(y_start, y_end):
            if data[x, y][3] > 0:
                has_content = True
                break
        if has_content:
            non_empty_cols.append(1)
        else:
            non_empty_cols.append(0)
            
    regions = []
    in_region = False
    start = 0
    for x in range(width):
        is_content = non_empty_cols[x]
        if is_content and not in_region:
            start = x
            in_region = True
        elif not is_content and in_region:
            regions.append((start, x))
            in_region = False
            
    if in_region:
        regions.append((start, width))
        
    print(f"Row 1 (Y {y_start}-{y_end}) has {len(regions)} sprites:")
    for i, r in enumerate(regions):
        print(f"  Sprite {i}: x={r[0]}, w={r[1]-r[0]}")

if __name__ == "__main__":
    analyze_row1("assets/pradeep_sheet.png")
