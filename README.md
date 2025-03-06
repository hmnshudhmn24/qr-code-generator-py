# QR Code Generator

## Overview
This is a simple QR Code Generator built using Python. It allows users to generate QR codes for any text or URL and save them as images.

## Features
- Generates QR codes for text or URLs.
- Saves QR codes as an image.
- Customizable QR code color and background color.
- Option to save as PNG or JPG.
- User-friendly command-line interface.

## Requirements
Ensure you have Python installed, then install the required package:

```sh
pip install qrcode[pil]
```

## How to Use
1. Run the script:
   ```sh
   python qr_code_generator.py
   ```
2. Enter the text or URL you want to convert into a QR code.
3. Provide a filename (or press Enter to use the default `qrcode.png`).
4. Choose QR code and background colors.
5. Decide whether to save the QR code as PNG or JPG.
6. The QR code image will be saved in the same directory.

## Example
```sh
Enter the text or URL for the QR code: https://example.com
Enter the filename (or press Enter for default 'qrcode.png'): my_qr.png
Enter the QR code color (default: black): blue
Enter the background color (default: white): yellow
Save as JPG instead of PNG? (yes/no, default: no): yes
QR code saved as my_qr.jpg
```

## License
This project is open-source and free to use.
