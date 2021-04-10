import qrcode
# create png qr code
qr = qrcode.QRCode(version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=2)

qr.add_data("君に恋をしているんだ")
qr.make(fit=True)

img = qr.make_image(fill_color="purple", back_color="white")
img.save("MyQR.png")

# create svg qr code 

import qrcode.image.svg
factory = qrcode.image.svg.SvgPathImage
svg_img = qrcode.make("hello world", image_factory=factory)
svg_img.save("myqr.svg")

