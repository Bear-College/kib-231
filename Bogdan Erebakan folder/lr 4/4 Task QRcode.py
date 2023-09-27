import qrcode
url = "https://www.youtube.com/watch?v=QX3FNE6xbco&t=11s"
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4,
    )
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="black")
save = r"C:\Users\user\Desktop\CUM ZONE\PythonBachelor\Bogdan Erebakan folder\lr 4\rammstein.png"
img.save (save)
