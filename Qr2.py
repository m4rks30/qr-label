import qrcode
import tkinter as tk

def generate_qr():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text.get())
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")

root = tk.Tk()
root.geometry("300x150")
root.title("QR Code Generator")

label = tk.Label(root, text="Enter text to generate QR code:")
label.pack()

text = tk.Entry(root)
text.pack()

button = tk.Button(root, text="Generate QR Code", command=generate_qr)
button.pack()

root.mainloop()
