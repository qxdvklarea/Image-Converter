# Image Converter

A simple Python script for converting images between formats (e.g., JPG to PNG) using [Pillow](https://python-pillow.org/).

## Features

- Convert images to popular formats: JPG, PNG, WEBP, BMP, TIFF, etc.
- Command-line interface for easy usage.

## Requirements

- Python 3.x
- Pillow library

Install Pillow with:

```bash
pip install Pillow
```

## Usage

```bash
python image_converter.py <input_image> <output_format>
```

**Examples:**

Convert JPG to PNG:

```bash
python image_converter.py photo.jpg png
```

Convert PNG to WEBP:

```bash
python image_converter.py logo.png webp
```

The converted image will be saved in the same directory with the new extension.

## License

MIT
