from PIL import Image, ImageEnhance, ImageFilter
import matplotlib.pyplot as plt

# load picture
image_path = "honeyglas.jpeg"
original_image = Image.open(image_path)

# surreal changings
enhancer = ImageEnhance.Color(original_image)
color_enhanced = enhancer.enhance(2.5)  # Verstärkt die Farben

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

# save it 
final_image.save("Surrealistic_Filtered_Image.jpg")
print("Surrealistic image saved as 'Surrealistic_Filtered_Image.jpg'")