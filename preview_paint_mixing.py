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
    
    paints, ratio, mixed_colour, distance = find_closest_two_paint_mix(colour)
    
    print(f"Target colour: {colour}")
    print(f"Closest single paint: {single_paint.name}")
    print()
    
    print("Suggested two-paint mixture:")
    print(f"  {ratio[0]} part(s) {paints[0].name}")
    print(f"  {ratio[1]} part(s) {paints[1].name}")
    print()

    print(f"Estimated mixed colour: {mixed_colour}")
    print()