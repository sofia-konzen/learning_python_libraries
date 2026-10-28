import sys
import qrcode
from PIL import Image, ImageFont, ImageText, ImageDraw


if len(sys.argv) < 3:
    print("Please provide something to encode")
    exit()

# CREATE A QR CODE GENERATOR (FOR PLAIN IMAGE, NO BORDER)
# you can also only do qrcode.make("text inside here"),
# but values such as border will be the defaults (border=4)
qr_gen = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # L < M(default) < Q < H
    border=0
)
qr_gen.add_data(sys.argv[1])
qr_gen.make(fit=True)

# GENERATE THE QR CODE AND GET ITS PILLOW'S IMAGE OBJECT
qrcode = qr_gen.make_image(fill_color="black", back_color="white").get_image()
w, h = qrcode.size

# CREATE A CANVAS WITH THE SIZES YOU WANT (FOR BORDER, TEXT...)
border = 80
text_space = 70
canvas = Image.new("RGB", (w + border, h + border + text_space), "white")
draw = ImageDraw.Draw(canvas)

# ADD BORDER
box1 = [(3, 3), (w + border - 3, h + border - 3 + text_space)]
box2 = [(3, 3), (w + border - 3, h + border - 3)]
draw.rounded_rectangle(box1, radius=32, fill="black", outline="black", width=15)
draw.rounded_rectangle(box2, radius=32, fill="white", outline="black", width=15)

# ADD QR CODE TO THE CANVAS
canvas.paste(qrcode, (border // 2, border // 2))

# ADD TEXT AT BOTTOM
font = ImageFont.truetype("fonts/Open_Sans/OpenSans-Bold.ttf", 54)
text = ImageText.Text(sys.argv[2], font)
text.embed_color()
# text.stroke(1, "#000")  # adds a border
draw.text(
    ((w - text.get_length() + border) // 2, h + 25 + border // 2),
    text, "#fff")

# DISPLAY / SAVE IMAGE
canvas.show()  # open image
canvas.save(f"{sys.argv[2]}.png")

# SOURCES:
# https://pypi.org/project/qrcode/
# https://pillow.readthedocs.io/en/stable/index.html