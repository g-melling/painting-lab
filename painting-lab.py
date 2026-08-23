from PIL import Image, ImageOps

def load_image(path):
    return Image.open(path)

def mirror_image(image):
    return ImageOps.mirror(image)

def grayscale_image(image):
    return ImageOps.grayscale(image)