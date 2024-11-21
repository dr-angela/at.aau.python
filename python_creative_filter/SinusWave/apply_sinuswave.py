from PIL import Image, ImageFilter
import numpy as np

# Load the image
image_path = "honigglas_header.png"  # Replace with your image path
original_image = Image.open(image_path)


# Apply distortion effect using a sinusoidal wave pattern
def apply_distortion(image, amplitude=30, frequency=0.05):
    image_array = np.array(image)
    height, width, channels = image_array.shape
    distorted_array = np.zeros_like(image_array)

    for y in range(height):
        # Calculate the horizontal offset using a sinusoidal wave
        offset = int(amplitude * np.sin(2 * np.pi * frequency * y))
        for x in range(width):
            new_x = (x + offset) % width  # Wrap around the image width
            distorted_array[y, new_x] = image_array[y, x]

    distorted_image = Image.fromarray(distorted_array)
    return distorted_image


# Apply distortion to the image
distorted_image = apply_distortion(original_image, amplitude=30, frequency=0.02)

# Save the distorted image
distorted_image.save("Distorted_Honeyglass_Image.jpeg")
print("Distorted image saved as 'Distorted_Honeyglass_Image.jpeg'")