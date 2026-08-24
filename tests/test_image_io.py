import pytest
from PIL import Image, UnidentifiedImageError

from painting_lab.image_io import load_image, save_image


def test_load_image_returns_image(tmp_path):
    test_file = tmp_path / "test_image.png"
    
    image = Image.new("RGB", (100, 100), "red")
    image.save(test_file)
    
    result = load_image(test_file)
    
    assert isinstance(result, Image.Image)
    assert result.size == (100, 100)
    assert result.mode == ("RGB")
    
    
def test_load_image_missing_file():
    with pytest.raises(FileNotFoundError):
        load_image("this_file_does_not_exist.png")
        
        
def test_load_image_invalid_file(tmp_path):
    test_file = tmp_path / "not_an_image.txt"
    
    test_file.write_text("This is not an image.")
    
    with pytest.raises(UnidentifiedImageError):
        load_image(test_file)
        
        
def test_save_image_creates_file(tmp_path):
    image = Image.new("RGB", (50, 50), "blue")
    output_file = tmp_path / "saved_image.png"
    
    save_image(image, output_file)
    
    assert output_file.exists()
    
    saved_image = Image.open(output_file)
    
    assert saved_image.size == (50, 50)
    assert saved_image.mode == "RGB"