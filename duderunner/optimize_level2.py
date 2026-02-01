from PIL import Image
import os

assets_dir = r"c:\Users\Kumaresa pandiyan\OneDrive\Documents\duderunner\assets"

def resize_image(filename, target_height=None, target_width=None):
    path = os.path.join(assets_dir, filename)
    if not os.path.exists(path):
        print(f"Skipping {filename}: Not found")
        return

    try:
        img = Image.open(path)
        w, h = img.size
        
        new_w, new_h = w, h
        
        if target_height:
            scale = target_height / h
            new_h = target_height
            new_w = int(w * scale)
        elif target_width:
             scale = target_width / w
             new_w = target_width
             new_h = int(h * scale)

        print(f"Resizing {filename}: {w}x{h} -> {new_w}x{new_h}")
        img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        img.save(path) # Overwrite
        print(f"Saved {filename}")

    except Exception as e:
        print(f"Error processing {filename}: {e}")

# Run Optimizations
# Sky: reasonable height
resize_image("bg_sky2.png", target_height=1080)

# Ground: Reduce to 150 to make texture thinner
resize_image("bg_ground2.png", target_height=150)

# Obstacles: Reduce to 80px (much smaller)
resize_image("obstacle_car.png", target_height=80)
resize_image("obstacle_bike.png", target_height=80)
