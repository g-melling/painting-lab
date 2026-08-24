from PIL import Image, ImageOps


def mirror_image(image: Image.Image) -> Image.Image:
    return ImageOps.mirror(image)


def grayscale_image(image: Image.Image) -> Image.Image:
    return ImageOps.grayscale(image)


def create_value_study(image: Image.Image, levels: int = 3) -> Image.Image:
    grayscale = ImageOps.grayscale(image)
    
    if levels < 2:
        raise ValueError("levels must be at least 2")
    
    step = 256 / levels
    
    return grayscale.point(
        lambda pixel: int(pixel // step) * int(255 / (levels - 1))
    )