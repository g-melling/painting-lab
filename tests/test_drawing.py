import numpy as np

from PIL import Image

from painting_lab.drawing import (
    original_line_drawing,
    create_detailed_line_drawing,
    create_simple_line_drawing,
    create_value_based_line_drawing,
)


# --------------------------------------------------
# Original line drawing
# --------------------------------------------------

def test_original_line_drawing_preserves_size():
    image = Image.new("RGB", (100, 50), "white")

    result = original_line_drawing(image)

    assert result.size == (100, 50)


def test_original_line_drawing_returns_grayscale():
    image = Image.new("RGB", (100, 50), "white")

    result = original_line_drawing(image)

    assert result.mode == "L"


# --------------------------------------------------
# Detailed line drawing
# --------------------------------------------------

def test_detailed_line_drawing_preserves_size():
    image = Image.new("RGB", (100, 50), "white")

    result = create_detailed_line_drawing(image)

    assert result.size == (100, 50)


def test_detailed_line_drawing_returns_grayscale():
    image = Image.new("RGB", (100, 50), "white")

    result = create_detailed_line_drawing(image)

    assert result.mode == "L"


# --------------------------------------------------
# Simple line drawing
# --------------------------------------------------

def test_simple_line_drawing_preserves_size():
    image = Image.new("RGB", (100, 50), "white")

    result = create_simple_line_drawing(image)

    assert result.size == (100, 50)


def test_simple_line_drawing_returns_grayscale():
    image = Image.new("RGB", (100, 50), "white")

    result = create_simple_line_drawing(image)

    assert result.mode == "L"


def test_simple_line_drawing_detects_edge():
    image = Image.new("RGB", (100, 100), "white")

    # Create a large black square
    for x in range(30, 70):
        for y in range(30, 70):
            image.putpixel((x, y), (0, 0, 0))

    result = create_simple_line_drawing(image)

    pixels = np.array(result)

    assert pixels.min() == 0
    assert pixels.max() == 255


# --------------------------------------------------
# Value-based line drawing
# --------------------------------------------------

def test_value_based_line_drawing_preserves_size():
    image = Image.new("RGB", (100, 50), "white")

    result = create_value_based_line_drawing(image)

    assert result.size == (100, 50)


def test_value_based_line_drawing_returns_grayscale():
    image = Image.new("RGB", (100, 50), "white")

    result = create_value_based_line_drawing(image)

    assert result.mode == "L"


def test_value_based_line_drawing_uniform_image_is_white():
    image = Image.new(
        "RGB",
        (100, 100),
        (128, 128, 128),
    )

    result = create_value_based_line_drawing(image)

    pixels = np.array(result)

    assert pixels.min() == 255
    assert pixels.max() == 255


def test_value_based_line_drawing_detects_value_boundary():
    image = Image.new(
        "RGB",
        (100, 100),
        "white",
    )

    # Make the left half dark and right half light
    for x in range(50):
        for y in range(100):
            image.putpixel(
                (x, y),
                (20, 20, 20),
            )

    result = create_value_based_line_drawing(
        image,
        levels=5,
    )

    pixels = np.array(result)

    # There should be some non-white pixels where
    # the two value regions meet.
    assert pixels.min() < 255


def test_value_based_line_drawing_accepts_different_levels():
    image = Image.new(
        "RGB",
        (100, 100),
        (100, 100, 100),
    )

    result_4 = create_value_based_line_drawing(
        image,
        levels=4,
    )

    result_5 = create_value_based_line_drawing(
        image,
        levels=5,
    )

    assert result_4.size == image.size
    assert result_5.size == image.size