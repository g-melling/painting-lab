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
