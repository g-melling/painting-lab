from painting_lab.image_io import load_image
from painting_lab.painting_stages import extract_palette
from painting_lab.paint_mixing import find_closest_paint, find_closest_two_paint_mix

image = load_image("sample_images/image1.jpg")

palette = extract_palette(
    image,
    colours=8,
)

print("Paint Mix Suggestions:\n")

for colour in palette:
    single_paint = find_closest_paint(colour)
    
    paints, mixed_colour, distance = find_closest_two_paint_mix(colour)
    
    print(f"Target colour: {colour}")
    print(f"Closest single paint: {single_paint.name}")
    print()
    
    print(f"Closest 1:1 mixture: {paints[0].name} + {paints[1].name}")
    print()
    
    print(f"Estimated mixed colour: {mixed_colour}")
    print()
    