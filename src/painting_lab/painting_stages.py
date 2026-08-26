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
    
    
def create_colour_block_in(
    image: Image.Image,
    colours: int = 8,
) -> Image.Image:
    
    rgb_image = image.convert("RGB")
    
    block_in = rgb_image.quantize(colors=colours).convert("RGB")
    
    return block_in


def extract_palette(
    image: Image.Image,
    colours: int=8,
) -> list[tuple[int, int, int]]:
    
    rgb_image = image.convert("RGB")
    
    quantized = rgb_image.quantize(colors=colours)
    
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
