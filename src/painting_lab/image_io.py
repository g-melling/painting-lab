from PIL import Image


def load_image(path: str) -> Image.Image:
    image = Image.open(path)
    return image


def save_image(image: Image.Image, path: str) -> None:
    image.save(path)