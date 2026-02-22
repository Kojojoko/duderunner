"""
Normalize the hero spritesheet frame widths.
Extracts each running frame, pads them to uniform width, and saves a new spritesheet.
"""
from PIL import Image

# Load the spritesheet
input_path = r"c:\Users\Kumaresa pandiyan\OneDrive\Documents\duderunner\assets\pradeep_sheet.png"
output_path = r"c:\Users\Kumaresa pandiyan\OneDrive\Documents\duderunner\assets\hero_sheet_normalized.png"

img = Image.open(input_path)
print(f"Original spritesheet size: {img.size}")

# Frame coordinates from the code (x, y, width, height)
# These are the original frames from the 1696x2528 spritesheet
frames_data = [
    # Run frames (Row 1)
    {"name": "run0", "x": 25, "y": 58, "w": 407, "h": 637},
    {"name": "run1", "x": 504, "y": 58, "w": 263, "h": 637},
    {"name": "run2", "x": 811, "y": 58, "w": 387, "h": 637},
    {"name": "run3", "x": 1233, "y": 58, "w": 439, "h": 637},
    # Jump frame (Row 2)
    {"name": "jump", "x": 101, "y": 833, "w": 296, "h": 878},
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
    
    # Center the cropped frame in the padded image
    x_offset = (max_width - frame["w"]) // 2
    y_offset = max_height - frame["h"]  # Align to bottom
    padded.paste(cropped, (x_offset, y_offset))
    
    normalized_frames.append(padded)
    print(f"Processed {frame['name']}: {frame['w']}x{frame['h']} -> {max_width}x{max_height}")

# Create new spritesheet with frames in a row
# Run frames in row 1, jump frame in row 2
num_run_frames = 4
sheet_width = max_width * num_run_frames
sheet_height = max_height * 2  # 2 rows

new_sheet = Image.new("RGBA", (sheet_width, sheet_height), (0, 0, 0, 0))

# Place run frames in row 1
for i, frame in enumerate(normalized_frames[:4]):
    new_sheet.paste(frame, (i * max_width, 0))

# Place jump frame in row 2 (centered)
jump_x = (sheet_width - max_width) // 2
new_sheet.paste(normalized_frames[4], (jump_x, max_height))

# Save the new spritesheet
new_sheet.save(output_path)
print(f"\nSaved normalized spritesheet to: {output_path}")
print(f"New spritesheet size: {new_sheet.size}")
print(f"\nNew frame coordinates (all {max_width}x{max_height}):")
print(f"  run0: x=0, y=0")
print(f"  run1: x={max_width}, y=0")
print(f"  run2: x={max_width*2}, y=0")
print(f"  run3: x={max_width*3}, y=0")
print(f"  jump: x={jump_x}, y={max_height}")
