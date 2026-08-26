from painting_lab.image_io import load_image, save_image
from painting_lab.basic_transformations import grayscale_image
from painting_lab.painting_stages import create_grisaille


image = load_image("sample_images/image1.jpg")

grayscale = grayscale_image(image)
grisaille = create_grisaille(image)

save_image(grayscale, "sample_images/grayscale_image1.png")
save_image(grisaille, "sample_images/grisaille_image1.png")

print("Grayscale and Grisaille previews saved successfully.")