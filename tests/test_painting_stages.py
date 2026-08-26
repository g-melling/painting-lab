from PIL import Image

from painting_lab.painting_stages import create_grisaille


def test_grisaille_preserves_size():
    image = Image.new("RGB", (100, 50), "red")
    
    result = create_grisaille(image)
    
    assert result.size == (100, 50)
    
    
def test_grisaille_returns_grayscale_image():
    image = Image.new("RGB", (100, 50), "red")
    
    result = create_grisaille(image)
    
    assert result.mode == "L"
    