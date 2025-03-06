import qrcode
from PIL import Image

def generate_qr(data, filename='qrcode.png', fill_color='black', back_color='white', save_as_jpg=False):
    """Generates a QR code for the given data and saves it as an image."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    
    if save_as_jpg:
        filename = filename.replace('.png', '.jpg')
        img = img.convert('RGB')  # Convert to RGB for JPG format
    
    img.save(filename)
    print(f'QR code saved as {filename}')

if __name__ == "__main__":
    user_data = input("Enter the text or URL for the QR code: ")
    file_name = input("Enter the filename (or press Enter for default 'qrcode.png'): ")
    fill_color = input("Enter the QR code color (default: black): ") or 'black'
    back_color = input("Enter the background color (default: white): ") or 'white'
    save_as_jpg = input("Save as JPG instead of PNG? (yes/no, default: no): ").strip().lower() == 'yes'
    
    if not file_name:
        file_name = 'qrcode.png'
    
    generate_qr(user_data, file_name, fill_color, back_color, save_as_jpg)
