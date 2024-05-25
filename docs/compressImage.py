from PIL import Image
import os

def compress_image(input_image_path, scale_factor=0.5):
    # Open the original image
    original_image = Image.open(input_image_path)

    # Calculate the new size
    new_size = (
        int(original_image.width * scale_factor),
        int(original_image.height * scale_factor)
    )

    # Resize the image
    compressed_image = original_image.resize(new_size, Image.DEFAULT_STRATEGY)

    # Generate the output image path
    base, ext = os.path.splitext(input_image_path)
    output_image_path = f"{base} compressed{ext}"

    # Save the compressed image
    compressed_image.save(output_image_path, "PNG", optimize=True)

    print(f"Compressed image saved to {output_image_path}")

# Example usage 
compress_image("tese4 001.png", scale_factor=0.25)
