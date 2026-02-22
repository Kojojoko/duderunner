"""
Re-normalize Hero Sheet with Death Frame
Using the CORRECT original coordinates from normalize_sheet.py
"""
from PIL import Image
import os

input_path = r"c:\Users\Kumaresa pandiyan\OneDrive\Documents\duderunner\assets\pradeep_sheet.png"
output_path = r"c:\Users\Kumaresa pandiyan\OneDrive\Documents\duderunner\assets\hero_sheet_normalized.png"

img = Image.open(input_path)
print("="*60)
print("HERO SHEET RE-NORMALIZATION WITH DEATH FRAME")
print("="*60)
print(f"Original spritesheet size: {img.size}")

# Frame coordinates from normalize_sheet.py (CORRECT ones)
frames_data = [
    # Run frames (Row 1)
    {"name": "run0", "x": 25, "y": 58, "w": 407, "h": 637},
    {"name": "run1", "x": 504, "y": 58, "w": 263, "h": 637},
    {"name": "run2", "x": 811, "y": 58, "w": 387, "h": 637},
    {"name": "run3", "x": 1233, "y": 58, "w": 439, "h": 637},
    # Jump frame (Row 2)
    {"name": "jump", "x": 101, "y": 833, "w": 296, "h": 878},
    # Death frame (Row 3) - CORRECTED COORDINATES!
    {"name": "death", "x": 667, "y": 1938, "w": 377, "h": 467},
]

# Find max width and height for uniform size
max_width = max(f["w"] for f in frames_data)
max_height = max(f["h"] for f in frames_data)
print(f"Max frame dimensions: {max_width}x{max_height}")

# Extract and pad each frame
normalized_frames = []
for frame in frames_data:
    # Crop the frame from original
    box = (frame["x"], frame["y"], frame["x"] + frame["w"], frame["y"] + frame["h"])
    cropped = img.crop(box)
    
    # Create a new image with max dimensions (transparent background)
    padded = Image.new("RGBA", (max_width, max_height), (0, 0, 0, 0))
    
    # Center horizontally, align to bottom vertically
    x_offset = (max_width - frame["w"]) // 2
    y_offset = max_height - frame["h"]
    padded.paste(cropped, (x_offset, y_offset))
    
    normalized_frames.append(padded)
    print(f"Processed {frame['name']}: {frame['w']}x{frame['h']} -> {max_width}x{max_height}")

# Create new spritesheet
num_run_frames = 4
sheet_width = max_width * num_run_frames
sheet_height = max_height * 2  # 2 rows

new_sheet = Image.new("RGBA", (sheet_width, sheet_height), (0, 0, 0, 0))

# Place run frames in row 1
for i, frame in enumerate(normalized_frames[:4]):
    new_sheet.paste(frame, (i * max_width, 0))
    print(f"  run{i} placed at ({i * max_width}, 0)")

# Place jump frame in row 2 (position 1)
jump_x = max_width
new_sheet.paste(normalized_frames[4], (jump_x, max_height))
print(f"  jump placed at ({jump_x}, {max_height})")

# Place death frame in row 2 (position 2)
death_x = max_width * 2
new_sheet.paste(normalized_frames[5], (death_x, max_height))
print(f"  death placed at ({death_x}, {max_height})")

# Save
new_sheet.save(output_path, optimize=True)

original_size = os.path.getsize(input_path)
final_size = os.path.getsize(output_path)

print("\n" + "="*60)
print("✓ SUCCESS!")
print("="*60)
print(f"Saved to: {output_path}")
print(f"New spritesheet size: {new_sheet.size}")
print(f"File size: {final_size / (1024*1024):.2f} MB (was {original_size / (1024*1024):.2f} MB)")
print("\nFrame layout:")
print("  Row 1: [run0] [run1] [run2] [run3]")
print("  Row 2: [empty] [jump] [death] [empty]")
print("\nNew frame coordinates (all {}x{}):".format(max_width, max_height))
print(f"  run0: ({0}, {0})")
print(f"  run1: ({max_width}, {0})")
print(f"  run2: ({max_width*2}, {0})")
print(f"  run3: ({max_width*3}, {0})")
print(f"  jump: ({jump_x}, {max_height})")
print(f"  death: ({death_x}, {max_height})")
print("\n✓ Hero sheet matches Mamitha layout!")
print("="*60)
