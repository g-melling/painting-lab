from PIL import Image

from painting_lab.image_io import load_image


def test_load_image_returns_image(tmp_path):
    test_file = tmp_path / "test_image.png"
    
    image = Image.new("RGB", (100, 100), "red")
    image.save(test_file)
    
    result = load_image(test_file)
    
    assert isinstance(result, Image.Image)