from PIL import Image, ImageDraw

from painting_lab.image_io import load_image, save_image
from painting_lab.painting_stages import (
    create_colour_block_in,
    extract_palette,
)
from painting_lab.paint_mixing import find_best_paint_mix


image = load_image("sample_images/image1.jpg")

# Extract the palette ONCE
palette = extract_palette(
    image,
    colours=8,
)

# Create colour block-in
block_in = create_colour_block_in(
    image,
    colours=8,
)

save_image(
    block_in,
    "sample_images/image1_colour_block_in.png",
)


# -----------------------------
# Create labelled palette image
# -----------------------------

swatch_width = 120
swatch_height = 120
label_height = 40

palette_image = Image.new(
    "RGB",
    (
        swatch_width * len(palette),
        swatch_height + label_height,
    ),
    "white",
)

draw = ImageDraw.Draw(palette_image)

for index, colour in enumerate(palette):
    left = index * swatch_width
    right = left + swatch_width

    draw.rectangle(
        [
            left,
            0,
            right,
            swatch_height,
        ],
        fill=colour,
    )

    draw.text(
        (
            left + 10,
            swatch_height + 10,
        ),
        f"Colour {index + 1}",
        fill="black",
    )


save_image(
    palette_image,
    "sample_images/image1_labelled_palette.png",
)


# -----------------------------
# Print mixing recommendations
# -----------------------------

print("Paint mixing recommendations:\n")

for index, colour in enumerate(
    palette,
    start=1,
):

    paints, ratio, mixed_colour, distance = (
        find_best_paint_mix(colour)
    )

    print(f"Colour {index}")
    print(f"Target RGB: {colour}")

    print("Suggested starting mixture:")

    for paint, parts in zip(
        paints,
        ratio,
    ):
        print(
            f"  {parts} part(s) "
            f"{paint.name}"
        )

    print(
        f"Estimated mixed colour: "
        f"{mixed_colour}"
    )

    print(
        f"Colour distance: "
        f"{distance:.2f}"
    )

    print()