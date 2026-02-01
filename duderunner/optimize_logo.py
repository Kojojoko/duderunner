from PIL import Image
import os

assets_dir = r"c:\Users\Kumaresa pandiyan\OneDrive\Documents\duderunner\assets"

def resize_image(filename, target_width=None):
    path = os.path.join(assets_dir, filename)
    if not os.path.exists(path):
        print(f"Skipping {filename}: Not found")
        return

    try:
        img = Image.open(path)
        w, h = img.size
        
        if w > target_width:
            scale = target_width / w
            new_w = target_width
            new_h = int(h * scale)
            print(f"Resizing {filename}: {w}x{h} -> {new_w}x{new_h}")
            img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
            img.save(path) # Overwrite
            print(f"Saved {filename}")
        else:
            print(f"{filename} is already small enough ({w}px)")

    except Exception as e:
        print(f"Error processing {filename}: {e}")

# Resize Logo 
resize_image("logo.png", target_width=800)
