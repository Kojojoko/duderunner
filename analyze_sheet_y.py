from PIL import Image
import sys

def find_gaps_y(path):
    img = Image.open(path)
    width, height = img.size
    print(f"Size: {width}x{height}")
    
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    data = img.load()
    
    non_empty_rows = []
    
    for y in range(height):
        has_content = False
        for x in range(width):
            if data[x, y][3] > 0:
                has_content = True
                break
        if has_content:
            non_empty_rows.append(1)
        else:
            non_empty_rows.append(0)
            
    regions = []
    in_region = False
    start = 0
    for y in range(height):
        is_content = non_empty_rows[y]
        if is_content and not in_region:
            start = y
            in_region = True
        elif not is_content and in_region:
            regions.append((start, y))
            in_region = False
            
    if in_region:
        regions.append((start, height))
        
    print(f"Found {len(regions)} horizontal regions (rows) of content:")
    for r in regions:
        print(f"  Start: {r[0]}, End: {r[1]}, Height: {r[1]-r[0]}")

if __name__ == "__main__":
    find_gaps_y("assets/pradeep_sheet.png")
