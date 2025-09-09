from PIL import Image
import os
import sys

def convert_image(input_path, output_format):
    """
    Converts an image file to the specified format using Pillow.

    Args:
        input_path (str): Path to the input image file.
        output_format (str): Desired output format (e.g., 'png', 'jpg', 'webp').
    """
    # Get file name and directory
    file_dir, file_name = os.path.split(input_path)
    base_name, _ = os.path.splitext(file_name)
    output_file = os.path.join(file_dir, f"{base_name}.{output_format.lower()}")

    # Open and convert image
    with Image.open(input_path) as img:
        # Pillow requires 'JPEG', 'PNG', etc.
        img = img.convert("RGB") if output_format.lower() in ["jpg", "jpeg"] else img
        img.save(output_file, output_format.upper())
        print(f"Converted '{input_path}' to '{output_file}'.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python image_converter.py <input_image> <output_format>")
        print("Example: python image_converter.py photo.jpg png")
        sys.exit(1)

    input_image = sys.argv[1]
    output_format = sys.argv[2]

    convert_image(input_image, output_format)
