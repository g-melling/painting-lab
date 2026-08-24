import pytest
from PIL import Image

from painting_lab.basic_transformations import mirror_image, grayscale_image, create_value_study


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
    
    
def test_value_study_preserves_size():
    image = Image.new("RGB", (100, 50), "red")
    
    result = create_value_study(image, levels=3)
    
    assert result.size == (100, 50)
    
    
def test_value_study_returns_grayscale_image():
    image = Image.new("RGB", (100, 50), "red")
    
    result = create_value_study(image, levels=3)
    
    assert result.mode == "L"
    
    
def test_value_study_reduces_number_of_values():
    image = Image.new("L", (256, 1))
    
    for x in range(256):
        image.putpixel((x, 0), x)
    
    result = create_value_study(image, levels=3)
    
    values = set(result.get_flattened_data())
    
    assert len(values) <= 3
    
    
def test_value_study_rejects_too_few_levels():
    image = Image.new("RGB", (10, 10), "red")
    
    with pytest.raises(ValueError):
        create_value_study(image, levels=1)