from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import os
import random

# load picture
image_path = "honeyglas.jpeg"
original_image = Image.open(image_path)

# apply dual-tone filter
color1 = "#FF84C3"  # pink
color2 = "#035FA5"  # blue
grayscale = ImageOps.grayscale(original_image)  # convert to grayscale
dual_tone_image = ImageOps.colorize(grayscale, black=color2, white=color1)  # apply colors


# rearrange image into a grid and shuffle parts
def rearrange_image(image, rows, cols):
    width, height = image.size
    tile_width = width // cols
    tile_height = height // rows

    # split image into tiles
    tiles = []
    for row in range(rows):
        for col in range(cols):
            left = col * tile_width
            upper = row * tile_height
            right = left + tile_width
            lower = upper + tile_height
            tile = image.crop((left, upper, right, lower))  # crop tile
            tiles.append(tile)

    # shuffle tiles
    random.shuffle(tiles)

    # create new image
    rearranged = Image.new('RGB', (width, height))
    for index, tile in enumerate(tiles):
        row = index // cols
        col = index % cols
        left = col * tile_width
        upper = row * tile_height
        rearranged.paste(tile, (left, upper))  # paste tile in new position

    return rearranged


# rearrange with 3x6 grid
rearranged_image = rearrange_image(dual_tone_image, 3, 6)

# show original and processed images
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(original_image)
axes[0].set_title("Original Image")
axes[0].axis("off")

axes[1].imshow(rearranged_image)
axes[1].set_title("Dual-Tone & Rearranged Image")
axes[1].axis("off")

plt.tight_layout()
plt.show()

# dynamic folder relative to script
script_dir = os.path.dirname(os.path.abspath(__file__))  # script directory
output_folder = os.path.join(script_dir, "output")  # output folder

# ensure folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# function to create unique filenames
def get_unique_filename(folder, base_name, extension):
    i = 1
    while True:
        file_name = f"{base_name}_{i}.{extension}"  # increment file name
        file_path = os.path.join(folder, file_name)
        if not os.path.exists(file_path):
            return file_path
        i += 1


# generate unique file path
output_path = get_unique_filename(output_folder, "Dual_Tone_Rearranged_Image", "jpg")

# save image
rearranged_image.save(output_path)
print(f"Dual-tone and rearranged image saved as '{output_path}'")
