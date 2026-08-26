from painting_lab.image_io import load_image, save_image
from painting_lab.painting_stages import create_imprimatura


image = load_image("sample_images/image1.jpg")

imprimatura_sienna_8 = create_imprimatura(image, tones=8)
imprimatura_sienna_16 = create_imprimatura(image, tones=16)
imprimatura_umber_8 = create_imprimatura(image, tone="raw_umber")
imprimatura_umber_16 = create_imprimatura(image, tone="raw_umber", tones=16)

save_image(imprimatura_sienna_8, "sample_images/imprimatura_image1_sienna_8.png")
save_image(imprimatura_sienna_16, "sample_images/imprimatura_image1_sienna_16.png")
save_image(imprimatura_umber_8, "sample_images/imprimatura_image1_umber_8.png")
save_image(imprimatura_umber_16, "sample_images/imprimatura_image1_umber_16.png")


print("Imprimatura previews saved successfully.") 