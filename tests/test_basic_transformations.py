from PIL import Image

from painting_lab.basic_transformations import mirror_image


def test_mirror_image_preserves_size():
    image = Image.new("RGB", (100, 50), "red")
    
    result = mirror_image(image)
    
    assert result.size == (100, 50)
    
    
def test_mirror_image_preserves_mode():
    image = Image.new("RGB", (100,50), "red")
    
    result = mirror_image(image)
    
    assert result.mode == "RGB"