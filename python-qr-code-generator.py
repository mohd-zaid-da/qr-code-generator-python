import qrcode
import datetime
import sys
from PIL import Image

# Take numeric inputs safely
try:
    box_size = int(input("Enter Box Size (e.g. 10): ").strip() or 10) 
    border_size = int(input("Enter Border Size (e.g. 4): ").strip() or 4) 
except ValueError:
    print("Please enter valid numbers!")
    sys.exit(1)

# Create QR object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=box_size,
    border=border_size
)

# Add data
data = input("Enter URL or Text: ").strip()
if not data:
    print("QR data cannot be empty!")
    sys.exit(1)
qr.add_data(data)
qr.make(fit=True)

# Colors
fill_color = input("Enter QR color (e.g. black): ").strip() or "black"
back_color = input("Enter background color (e.g. white): ").strip() or "white"

# Generate image
img = qr.make_image(fill_color=fill_color, back_color=back_color)

# File name
filename = input("Enter output file name (leave blank for auto name): ").strip()

if not filename:
    timestamp=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename =f"qr_{timestamp}.png"
    
if not filename.endswith(".png"):
     filename +=".png"

img.save(filename)
print("DONE ✅")












