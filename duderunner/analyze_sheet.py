from PIL import Image
import sys

def find_gaps(path):
    img = Image.open(path)
    width, height = img.size
    print(f"Size: {width}x{height}")
    
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    data = img.load()
    
    # 1. Scan X columns for transparency
    empty_cols = []
    
    # To save time, check every pixel in column?
    # Or just check if column has ANY non-transparent.
    
    non_empty_cols = []
    
    for x in range(width):
        has_content = False
        for y in range(height):
            if data[x, y][3] > 0: # Alpha > 0
                has_content = True
                break
        if has_content:
            non_empty_cols.append(1)
        else:
            non_empty_cols.append(0)
            
    # Find active regions
    regions = []
    in_region = False
    start = 0
    for x in range(width):
        is_content = non_empty_cols[x]
        if is_content and not in_region:
            start = x
            in_region = True
        elif not is_content and in_region:
            regions.append((start, x)) # x is first empty pixel
            in_region = False
            
    if in_region:
        regions.append((start, width))
        
    print(f"Found {len(regions)} vertical regions (columns) of content:")
    for r in regions:
        print(f"  Start: {r[0]}, End: {r[1]}, Width: {r[1]-r[0]}")
        
    # Same for Y?
    # Let's just focus on X first.
    
if __name__ == "__main__":
    find_gaps("assets/pradeep_sheet.png")
