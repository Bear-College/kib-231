import qrcode
img = qrcode.make('https://www.youtube.com/')
type(img)  # qrcode.image.pil.PilImage
img.save("Maksym Shek's folder\lab4\qrcode.png")