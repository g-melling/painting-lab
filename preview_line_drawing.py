from painting_lab.image_io import load_image, save_image
from painting_lab.drawing import create_detailed_line_drawing, create_simple_line_drawing, create_value_based_line_drawing


image = load_image("sample_images/image2.jpg")

detailed = create_detailed_line_drawing(image)
simple = create_simple_line_drawing(image)
value_based = create_value_based_line_drawing(image)

save_image(detailed, "sample_images/detailed_line_drawing.png")
save_image(simple, "sample_images/simple_line_drawing.png")
save_image(value_based, "sample_images/value_based_line_drawing.png")

print("Line drawings created successfully")
