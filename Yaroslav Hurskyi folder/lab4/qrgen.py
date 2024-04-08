import qrcode
img = qrcode.make('https://www.binance.com/en/price/meme')
type(img)  # qrcode.image.pil.PilImage
img.save("Yaroslav Hurskyi folder/lab4/qr.png")