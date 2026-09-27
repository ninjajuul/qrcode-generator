import qrcode
import os
from urllib.parse import urlparse

def get_filename_from_url(data):
    parsed = urlparse(data)
    domain = parsed.netloc or parsed.path

    if not domain:
        return "qrcode.png"

    domain = domain.replace("www.", "")
    domain = domain.split("/")[0]
    safe_name = "".join(c if c.isalnum() or c in ".-" else "_" for c in domain)

    return f"{safe_name}.png"

def generate_qr(data, filename=None):
    if filename is None:
        filename = get_filename_from_url(data)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(script_dir, filename)

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr.print_ascii(invert=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(full_path)
    print(f"\nQR code saved to: {full_path}")

if __name__ == "__main__":
    text = input("Enter text or URL to encode: ")
    generate_qr(text)
    input("\nPress Enter to close...")