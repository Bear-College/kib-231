import qrcode
img = qrcode.make('https://www.youtube.com')
type(img)  # qrcode.image.pil.PilImage
img.save("Bogdan Pirozhok folder\lab4\code.png")