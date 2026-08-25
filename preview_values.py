from painting_lab.image_io import load_image, save_image
from painting_lab.basic_transformations import create_value_study


image = load_image("sample_images/image3.jpg")

three_values = create_value_study(image, levels=3)
five_values = create_value_study(image, levels=5)

save_image(three_values, "sample_images/image3_3_values.png")
save_image(five_values, "sample_images/image3_5_values.png")

print("Value studies created successfully")