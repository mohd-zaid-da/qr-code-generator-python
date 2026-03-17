import qrcode
import datetime
import tkinter as tk
from tkinter import messagebox

# Generate QR function
def generate_qr():
    try:
        box_size = int(entry_box.get() or 10)
        border = int(entry_border.get() or 4)
    except ValueError:
        messagebox.showerror("Error", "Box size and border must be numbers!")
        return

    data = entry_data.get().strip()
    if not data:
        messagebox.showerror("Error", "Enter URL or Text!")
        return

    fill_color = entry_fill.get() or "black"
    back_color = entry_bg.get() or "white"

    filename = entry_file.get().strip()
    if not filename:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"qr_{timestamp}.png"

    if not filename.endswith(".png"):
        filename += ".png"

    # Create QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(filename)

    messagebox.showinfo("Success", f"QR Code saved as {filename}")


# GUI setup
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x400")

# Labels & Inputs
tk.Label(root, text="Enter URL or Text").pack()
entry_data = tk.Entry(root, width=40)
entry_data.pack()

tk.Label(root, text="Box Size (default 10)").pack()
entry_box = tk.Entry(root)
entry_box.pack()

tk.Label(root, text="Border Size (default 4)").pack()
entry_border = tk.Entry(root)
entry_border.pack()

tk.Label(root, text="QR Color (default black)").pack()
entry_fill = tk.Entry(root)
entry_fill.pack()

tk.Label(root, text="Background Color (default white)").pack()
entry_bg = tk.Entry(root)
entry_bg.pack()

tk.Label(root, text="File Name (optional)").pack()
entry_file = tk.Entry(root)
entry_file.pack()

# Button
tk.Button(root, text="Generate QR", command=generate_qr).pack(pady=15)

root.mainloop()
