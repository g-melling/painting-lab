from painting_lab.image_io import load_image
from painting_lab.painting_stages import extract_palette
from painting_lab.paint_mixing import find_best_paint_mix

image = load_image("sample_images/image1.jpg")

palette = extract_palette(
    image,
    colours=8,
)

print("Recommended Paint Mixes:\n")

for colour in palette:
    paints, ratio, mixed_colour, distance = find_best_paint_mix(colour)
    
    print(f"Target colour: {colour}")
    print("Recommended mixture:")
    
    for paint, parts in zip(paints, ratio):
        print(f"  {parts} part(s) {paint.name}")
    
    print(f"Estimated mixed colour: {mixed_colour}")
    print(f"Colour distance: {distance: .2f}")
    print()
    