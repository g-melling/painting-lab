from PIL import Image, ImageDraw

from painting_lab.image_io import load_image, save_image
from painting_lab.painting_stages import create_colour_block_in, extract_palette


image = load_image("sample_images/image1.jpg")

block_in = create_colour_block_in(
    image, 
    colours=8,
)

palette = extract_palette(
    image, 
    colours=8
)

save_image(block_in, "sample_images/image1_colour_block_in.png")

swatch_width = 120
swatch_height = 120

palette_image = Image.new(
    "RGB",
    (swatch_width * len(palette), swatch_height),
    "white",
)

draw = ImageDraw.Draw(palette_image)

for index, colour in enumerate(palette):
    left = index * swatch_width
    right = left + swatch_width
    
    draw.rectangle(
        [left, 0, right, swatch_height],
        fill=colour,
    )

save_image(palette_image, "sample_images/image1_palette.png")

print("Extracted palette:")

for colour in palette:
    print(colour)
    
print("Colour block-in and palette created successfully.")
