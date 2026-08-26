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
