import cv2
import numpy as np

from PIL import Image
from painting_lab.basic_transformations import create_value_study


def original_line_drawing(image: Image.Image) -> Image.Image:
    
    image_array = np.array(image)
    
    grayscale = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
    
    blurred = cv2.GaussianBlur(grayscale, (7, 7), 0)
    
    edges = cv2.Canny(blurred, 80, 180)
    
    inverted = cv2.bitwise_not(edges)
    
    return Image.fromarray(inverted)


def create_detailed_line_drawing(image: Image.Image) -> Image.Image:
    
    image_array = np.array(image)
    
    grayscale = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
    
    smoothed = cv2.bilateralFilter(
        grayscale,
        d=9,
        sigmaColor=75,
        sigmaSpace=75,
    )
    
    line_drawing = cv2.adaptiveThreshold(
        smoothed,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2,
    )
    
    return Image.fromarray(line_drawing)


def create_value_based_line_drawing(
    image: Image.Image,
    levels: int = 5,
) -> Image.Image:

    # Create simplified value study
    value_image = create_value_study(
        image,
        levels=levels,
    )

    value_array = np.array(value_image)

    # Start with a white canvas
    line_drawing = np.full_like(
        value_array,
        255,
    )

    # Find boundaries between neighbouring value regions
    horizontal_difference = (
        value_array[:, 1:] != value_array[:, :-1]
    )

    vertical_difference = (
        value_array[1:, :] != value_array[:-1, :]
    )

    # Draw black lines at those boundaries
    line_drawing[:, 1:][horizontal_difference] = 0
    line_drawing[1:, :][vertical_difference] = 0

    # Convert back to Pillow
    result = Image.fromarray(line_drawing)

    # Enlarge using a high-quality resampling filter
    large = result.resize(
        (result.width * 2, result.height * 2),
        Image.Resampling.LANCZOS,
    )

    # Resize back down to soften jagged pixel edges
    smooth = large.resize(
        result.size,
        Image.Resampling.LANCZOS,
    )

    return smooth


def create_simple_line_drawing(image: Image.Image) -> Image.Image:
    image_array = np.array(image)
    
    grayscale = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
    
    blurred = cv2.GaussianBlur(grayscale, (7, 7), 0)
    
    edges = cv2.Canny(blurred, 40, 100)
    
    contours, _ = cv2.findContours(
        edges,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE,
    )
    
    canvas = np.full_like(grayscale, 255)
    
    cv2.drawContours(
        canvas,
        contours,
        -1,
        0,
        thickness=2,
    )
    
    return Image.fromarray(canvas)
