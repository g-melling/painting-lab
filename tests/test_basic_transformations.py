from PIL import Image

from painting_lab.basic_transformations import mirror_image, grayscale_image


def test_mirror_image_preserves_size():
    image = Image.new("RGB", (100, 50), "red")
    
    result = mirror_image(image)
    
    assert result.size == (100, 50)
    
    
def test_mirror_image_preserves_mode():
    image = Image.new("RGB", (100,50), "red")
    
    result = mirror_image(image)
    
    assert result.mode == "RGB"
    
    
def test_mirror_image_flips_pixels():
    image = Image.new("RGB", (2, 1))
    
    image.putpixel((0, 0), (255, 0, 0))
    image.putpixel((1, 0), (0, 0, 255))
    
    result = mirror_image(image)
    
    assert result.getpixel((0, 0)) == (0, 0, 255)
    assert result.getpixel((1, 0)) == (255, 0, 0)
    
    

def test_grayscale_image_returns_grayscale_mode():
    image = Image.new("RGB", (100, 50), "red")
    
    result = grayscale_image(image)
    
    assert result.mode == "L"
    
    
def test_grayscale_image_preserves_size():
    image = Image.new("RGB", (100, 50), "red")

    result = grayscale_image(image)

    assert result.size == (100, 50)
    
    
def test_grayscale_image_converts_pixels(): 
    image = Image.new("RGB", (1, 1), (255, 0, 0))
    
    result = grayscale_image(image)
    
    pixel = result.getpixel((0, 0))
    
    assert isinstance(pixel, int)
    assert 0 <= pixel <= 255