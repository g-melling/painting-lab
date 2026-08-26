import pytest

from PIL import Image
from painting_lab.painting_stages import create_grisaille, create_imprimatura


def test_grisaille_preserves_size():
    image = Image.new("RGB", (100, 50), "red")
    
    result = create_grisaille(image)
    
    assert result.size == (100, 50)
    
    
def test_grisaille_returns_grayscale_image():
    image = Image.new("RGB", (100, 50), "red")
    
    result = create_grisaille(image)
    
    assert result.mode == "L"


def test_grisaille_reduces_tonal_values():
    image = Image.new("L", (256, 1))
    
    for x in range(256):
        image.putpixel((x, 0), x)
        
    image = image.convert("RGB")
    
    result = create_grisaille(image)
    
    values = set(result.get_flattened_data())
    
    assert len(values) <= 8
    

def test_imprimatura_preserves_size():
    image = Image.new("RGB", (100, 50), "white")
    
    result = create_imprimatura(image)
    
    assert result.size == (100, 50)
    

def test_imprimatura_returns_colour_image():
    image = Image.new("RGB", (100, 50), "white")
    
    result = create_imprimatura(image, tone="raw_umber")
    
    assert result.mode == "RGB"
    
    
def test_imprimatura_accepts_raw_umber():
    image = Image.new("RGB", (100, 50), "blue")
    
    result =  create_imprimatura(image, tone = "raw_umber")
    
    assert result.mode == "RGB"
    
    
def test_imprimatura_accepts_burnt_sienna():
    image = Image.new("RGB", (100, 50), "pink")
    
    result = create_imprimatura(image, tone="burnt_sienna")
    
    assert result.mode == "RGB"
    
    
def test_imprimatura_rejects_invalid_tone():
    image = Image.new("RGB", (100, 50), "white")
    
    with pytest.raises(ValueError):
        create_imprimatura(image, tone="purple")
        
        
def test_imprimatura_accepts_different_tone_counts():
    image = Image.new("RGB", (100, 50), "white")
    
    result_8 = create_imprimatura(image, tones=8)
    result_16 = create_imprimatura(image, tones=16)
    
    assert result_8.size == image.size
    assert result_16.size == image.size
    