import qrcode
img = qrcode.make('www.youtube.com')
type(img) 
img.save("myqrcode.png")
