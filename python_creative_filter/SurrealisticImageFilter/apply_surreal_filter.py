from PIL import Image, ImageEnhance, ImageFilter
import matplotlib.pyplot as plt
import os

# load picture
image_path = "honeyglas.jpeg"
original_image = Image.open(image_path)

# surreal changings
enhancer = ImageEnhance.Color(original_image)
color_enhanced = enhancer.enhance(2.5)

# gaussian blur
blurred = color_enhanced.filter(ImageFilter.GaussianBlur(2))
final_image = blurred.filter(ImageFilter.EDGE_ENHANCE_MORE)

# show original and new
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(original_image)
axes[0].set_title("Original Image")
axes[0].axis("off")

axes[1].imshow(final_image)
axes[1].set_title("Surrealistic Filter Applied")
axes[1].axis("off")

plt.tight_layout()
plt.show()

# dynamic folder relativ addressed to the script
script_dir = os.path.dirname(os.path.abspath(__file__))  # Verzeichnis des aktuellen Skripts
output_folder = os.path.join(script_dir, "output")  # Ordner "output" für den Filter

# be safe that folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# function for incrementing
def get_unique_filename(folder, base_name, extension):
    i = 1
    while True:
        file_name = f"{base_name}_{i}.{extension}"
        file_path = os.path.join(folder, file_name)
        if not os.path.exists(file_path):
            return file_path
        i += 1


# generate data path wit increment
output_path = get_unique_filename(output_folder, "Surrealistic_Filtered_Image", "jpg")

# save it
final_image.save(output_path)
print(f"Surrealistic image saved as '{output_path}'")
