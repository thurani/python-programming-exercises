import qrcode.main

data = input("Enter the data or URL: ").strip()
filename = input("Enter the filename: ").strip()

qr = qrcode.main.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill='black', back_color='white')
image.save(filename)
print(f"QR code saved as {filename}")