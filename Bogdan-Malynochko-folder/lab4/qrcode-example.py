import qrcode
img = qrcode.make('https://www.youtube.com/')
type(img)  # qrcode.image.pil.PilImage
img.save("Bogdan Malynochko's folder/lab4/some_file.png")