from painting_lab.image_io import load_image, save_image
from painting_lab.painting_stages import create_verdaccio


image = load_image("sample_images/image1.jpg")

verdaccio_8 = create_verdaccio(image)
verdaccio_16 = create_verdaccio(image, tones=16)

save_image(verdaccio_8, "sample_images/verdaccio_image1_8_tones.png")
save_image(verdaccio_16, "sample_images/verdaccio_image1_16_tones.png")

print("Verdaccio preview saved successfully")
