import tkinter as tk
import qrcode

class QRCodeGenerator:
    def __init__(self, master):
        self.master = master
        master.title("QR Code Generator")

        self.label = tk.Label(master, text="Enter text to generate QR code:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Generate QR Code", command=self.generate_qr)
        self.button.pack()

        self.qr_image = tk.Label(master)
        self.qr_image.pack()

    def generate_qr(self):
        # Get text from entry widget
        text = self.entry.get()

        # Generate QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(text)
        qr.make(fit=True)

        # Convert QR code to image
        img = qr.make_image(fill_color="black", back_color="white")

        # Display QR code image
        photo = tk.PhotoImage(data=img.tobytes())
        self.qr_image.configure(image=photo)
        self.qr_image.image = photo

root = tk.Tk()
qrgen = QRCodeGenerator(root)
root.mainloop()
