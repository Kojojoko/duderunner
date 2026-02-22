"""
Create a comparison visualization of both normalized character sheets.
Shows hero and mamitha side by side for verification.
"""
from PIL import Image, ImageDraw, ImageFont
import os

assets_dir = r"c:\Users\Kumaresa pandiyan\OneDrive\Documents\duderunner\assets"
hero_path = os.path.join(assets_dir, "hero_sheet_normalized.png")
mamitha_path = os.path.join(assets_dir, "mamitha_sheet_normalized.png")
output_path = os.path.join(assets_dir, "characters_comparison.png")

print("Creating character comparison...")
print("-" * 60)

# Load both sheets
hero = Image.open(hero_path)
mamitha = Image.open(mamitha_path)

print(f"Hero sheet: {hero.size}")
print(f"Mamitha sheet: {mamitha.size}")

# Create comparison image
padding = 50
label_height = 60
width = hero.size[0] + mamitha.size[0] + padding * 3
height = max(hero.size[1], mamitha.size[1]) + padding * 2 + label_height

comparison = Image.new("RGBA", (width, height), (40, 40, 40, 255))
draw = ImageDraw.Draw(comparison)

# Add labels
try:
    # Try to use a nice font
    font = ImageFont.truetype("arial.ttf", 40)
    small_font = ImageFont.truetype("arial.ttf", 24)
except:
    # Fallback to default
    font = ImageFont.load_default()
    small_font = ImageFont.load_default()

# Title
title = "Character Sprite Sheets Comparison"
title_bbox = draw.textbbox((0, 0), title, font=font)
title_width = title_bbox[2] - title_bbox[0]
draw.text(((width - title_width) // 2, 10), title, fill=(255, 255, 255), font=font)

# Hero label
hero_label = "HERO (Pradeep)"
hero_x = padding
hero_y = padding + label_height
draw.text((hero_x + 20, padding + 30), hero_label, fill=(100, 200, 255), font=small_font)

# Mamitha label  
mamitha_label = "MAMITHA (Player 2)"
mamitha_x = hero_x + hero.size[0] + padding
mamitha_y = padding + label_height
draw.text((mamitha_x + 20, padding + 30), mamitha_label, fill=(255, 150, 200), font=small_font)

# Paste character sheets
comparison.paste(hero, (hero_x, hero_y), hero)
comparison.paste(mamitha, (mamitha_x, mamitha_y), mamitha)

# Add frame indicators
def draw_frame_boxes(x_offset, y_offset, color):
    frame_width = 439
    frame_height = 878
    
    # Row 1: 4 run frames
    for i in range(4):
        x = x_offset + i * frame_width
        y = y_offset
        draw.rectangle([(x, y), (x + frame_width, y + frame_height)], outline=color, width=2)
        draw.text((x + 5, y + 5), f"run{i}", fill=color, font=small_font)
    
    # Row 2: 1 jump frame (centered)
    jump_x = x_offset + 658
    jump_y = y_offset + frame_height
    draw.rectangle([(jump_x, jump_y), (jump_x + frame_width, jump_y + frame_height)], outline=color, width=2)
    draw.text((jump_x + 5, jump_y + 5), "jump", fill=color, font=small_font)

# Draw frame indicators
draw_frame_boxes(hero_x, hero_y, (100, 200, 255))
draw_frame_boxes(mamitha_x, mamitha_y, (255, 150, 200))

# Add info at bottom
info_y = height - 40
info_text = f"Both sheets: 1756x1756 pixels | Frame size: 439x878 | Scale in game: 0.18"
info_bbox = draw.textbbox((0, 0), info_text, font=small_font)
info_width = info_bbox[2] - info_bbox[0]
draw.text(((width - info_width) // 2, info_y), info_text, fill=(200, 200, 200), font=small_font)

# Save
comparison.save(output_path)
print(f"\n✓ Comparison saved to: {output_path}")
print(f"  Size: {comparison.size[0]}x{comparison.size[1]}")
print("\nBoth character sheets are now normalized and ready for two-player mode!")
