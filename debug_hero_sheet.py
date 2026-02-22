"""
Debug script to verify hero_sheet_normalized.png structure
Shows exactly what frames exist and where
"""
from PIL import Image

path = r"c:\Users\Kumaresa pandiyan\OneDrive\Documents\duderunner\assets\hero_sheet_normalized.png"
img = Image.open(path)

print("="*60)
print("HERO SHEET ANALYSIS")
print("="*60)
print(f"Image size: {img.size}")
print(f"Mode: {img.mode}")

# Expected frame positions
frame_width = 439
frame_height = 878

frames = [
    ("run0", 0, 0),
    ("run1", 439, 0),
    ("run2", 878, 0),
    ("run3", 1317, 0),
    ("jump", 439, 878),
    ("death", 878, 878),
]

print("\nChecking each frame position:")
print("-"*60)

for name, x, y in frames:
    # Extract the frame
    box = (x, y, x + frame_width, y + frame_height)
    frame = img.crop(box)
    
    # Check if frame has any non-transparent pixels
    if frame.mode == 'RGBA':
        # Get alpha channel
        alpha = frame.split()[-1]
        bbox = alpha.getbbox()
        
        if bbox:
            actual_width = bbox[2] - bbox[0]
            actual_height = bbox[3] - bbox[1]
            print(f"{name:8} @ ({x:4}, {y:4}): ✓ HAS CONTENT ({actual_width}x{actual_height} pixels)")
        else:
            print(f"{name:8} @ ({x:4}, {y:4}): ✗ EMPTY/TRANSPARENT")
    else:
        print(f"{name:8} @ ({x:4}, {y:4}): ? Cannot check (not RGBA)")

print("\n" + "="*60)
print("If 'death' shows EMPTY, the frame wasn't extracted correctly!")
print("="*60)
