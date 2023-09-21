import qrcode
img = qrcode.make('https://www.youtube.com')
type(img)  # qrcode.image.pil.PilImage
img.save("Dima Shchensnevych's folder/lab4/code.png")