import cv2
import numpy as np

from PIL import Image, ImageFilter, ImageOps


def create_grisaille(
    image: Image.Image,
    tones: int = 8,
) -> Image.Image:
    
    grayscale = ImageOps.grayscale(image)
    
    # Softens fine photographic details
    softened = grayscale.filter(ImageFilter.GaussianBlur(radius=1.5))
    
    # Slightly reduces number of tonal steps, removes too much fine detail
    # Improvement on 3/5 value study
    grisaille = softened.quantize(colors=tones).convert("L")
    
    return grisaille


def create_imprimatura(
    image: Image.Image,
    tone: str = "burnt_sienna",
    tones: int=8,
) -> Image.Image:
    
    grisaille = create_grisaille(image, tones=tones)
    
    if tone == "burnt_sienna":
        dark_colour = (90, 40, 20)
        
    elif tone == "raw_umber":
        dark_colour = (70, 55, 40)
        
    else:
        raise ValueError("Tone must be 'burnt_sienna' or 'raw_umber'")
    
    imprimatura = ImageOps.colorize(
        grisaille,
        black=dark_colour,
        white="white",
    )
    
    return imprimatura


def create_verdaccio(
    image: Image.Image,
    tones: int=8,
) -> Image.Image:
    
    grisaille = create_grisaille(image, tones=tones)
    
    verdaccio = ImageOps.colorize(
        grisaille,
        black=(45, 75, 35),
        white=(245, 245, 235),
    )
    
    return verdaccio


def _kmeans_colours(
    image: Image.Image,
    colours: int = 8,
    max_size: int = 400,
):
    rgb_image = image.convert("RGB")

    preview = rgb_image.copy()
    preview.thumbnail(
        (max_size, max_size),
        Image.Resampling.LANCZOS,
    )

    image_array = np.array(preview)

    lab_image = cv2.cvtColor(
        image_array,
        cv2.COLOR_RGB2LAB,
    )

    pixels = lab_image.reshape((-1, 3))
    pixels = np.float32(pixels)

    criteria = (
        cv2.TERM_CRITERIA_EPS
        + cv2.TERM_CRITERIA_MAX_ITER,
        30,
        1.0,
    )

    _, labels, centres = cv2.kmeans(
        pixels,
        colours,
        None,
        criteria,
        3,
        cv2.KMEANS_PP_CENTERS,
    )

    centres = np.uint8(centres)

    return labels, centres, lab_image.shape


def create_colour_block_in(
    image: Image.Image,
    colours: int=8,
) -> Image.Image:
    
    labels, centres, shape = _kmeans_colours(
        image,
        colours=colours,
    )

    clustered = centres[labels.flatten()]
    
    clustered = clustered.reshape(shape)
    
    # Converts LAB back to RGB
    rgb_result = cv2.cvtColor(
        clustered,
        cv2.COLOR_LAB2RGB,
    )
    
    return Image.fromarray(rgb_result)


def extract_palette(
    image: Image.Image,
    colours: int = 8,
) -> list[tuple[int, int, int]]:

    labels, centres, _ = _kmeans_colours(
        image,
        colours=colours,
    )

    # Count how many pixels belong to each cluster
    counts = np.bincount(
        labels.flatten(),
        minlength=colours,
    )

    # Convert LAB cluster centres back to RGB
    lab_palette = centres.reshape(
        (1, colours, 3)
    )

    rgb_palette = cv2.cvtColor(
        lab_palette,
        cv2.COLOR_LAB2RGB,
    )[0]

    # Sort colours from most common to least common
    order = np.argsort(counts)[::-1]

    palette = []

    for index in order:
        colour = tuple(
            int(channel)
            for channel in rgb_palette[index]
        )

        palette.append(colour)

    return palette

    
    """
def create_colour_block_in(
    image: Image.Image,
    colours: int = 8,
) -> Image.Image:
    
    rgb_image = image.convert("RGB")
    
    quantized = rgb_image.quantize(
        colors=colours,
        method=Image.Quantize.MEDIANCUT,
        dither=Image.Dither.NONE,
    )
    
    return quantized.convert("RGB")


def extract_palette(
    image: Image.Image,
    colours: int=8,
) -> list[tuple[int, int, int]]:
    
    rgb_image = image.convert("RGB")
    
    quantized = rgb_image.quantize(
        colors=colours,
        method=Image.Quantize.MEDIANCUT,
        dither=Image.Dither.NONE,
    )
    
    palette = quantized.getpalette()
    colour_counts = quantized.getcolors()
    
    if palette is None or colour_counts is None:
        return []
    
    extracted_colours = []
    
    for count, colour_index in colour_counts:
        start = colour_index * 3
        
        colour = tuple(palette[start:start+3])
        
        extracted_colours.append((count, colour))
        
    extracted_colours.sort(key=lambda item: item[0], reverse=True)
    
    return [colour for _, colour in extracted_colours]
"""
