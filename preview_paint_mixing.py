from painting_lab.image_io import load_image
from painting_lab.painting_stages import extract_palette
from painting_lab.paint_mixing import suggest_paint_mix


image = load_image("sample_images/image1.jpg")

palette = extract_palette(
    image,
    colours=8,
)

print("Paint Mixing Suggestions:")


mix = suggest_paint_mix(
    (170, 120, 80)
)

print(mix.name)
print(mix.suggestion)
