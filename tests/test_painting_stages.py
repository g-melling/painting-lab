import pytest

from PIL import Image
from painting_lab.painting_stages import create_grisaille, create_imprimatura, create_colour_block_in, extract_palette


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
    
    
def test_colour_block_in_preserves_size():
    image = Image.new("RGB", (100, 50), "red")
    
    result = create_colour_block_in(image)
    
    assert result.size == (100, 50)
    
    
def test_colour_block_in_returns_rgb():
    image = Image.new("RGB", (100, 50), "red")
    
    result = create_colour_block_in(image)
    
    assert result.mode == "RGB"
    
    
def test_colour_block_in_limits_colours():
    image = Image.new("RGB", (256, 1))
    
    for x in range(256):
        image.putpixel((x, 0), (x, 255-x, x // 2))
        
    result = create_colour_block_in(image, colours=8)
    
    unique_colours = set(result.get_flattened_data())
    
    assert len(unique_colours) <= 8
    
    
def test_extract_palette_returns_list():
    image = Image.new("RGB", (100, 100), "red")
    
    palette = extract_palette(image, colours=8)
    
    assert isinstance(palette, list)
    
    
def test_extract_palette_limits_number_of_colours():
    image = Image.new("RGB", (100, 100))
    
    for x in range(100):
        for y in range(100):
            image.putpixel(
                (x, y),
                (x * 2, y * 2, 100),
            )
            
    palette = extract_palette(image, colours=8)
    
    assert len(palette) <= 8
    
    
def test_extract_palette_returns_rgb_tuples():
    image = Image.new("RGB", (100, 100), "blue")
    
    palette = extract_palette(image, colours=8)
    
    for colour in palette:
        assert len(colour) == 3
        
        for channel in colour:
            assert 0 <= channel <= 255
    