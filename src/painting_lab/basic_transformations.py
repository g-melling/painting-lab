from PIL import Image, ImageOps


def mirror_image(image: Image.Image) -> Image.Image:
    return ImageOps.mirror(image)