import qrcode
img = qrcode.make('https://www.youtube.com/')
type(img)  # qrcode.image.pil.PilImage
img.save("Artem Sheigets folder\lab4\qrcode.png")