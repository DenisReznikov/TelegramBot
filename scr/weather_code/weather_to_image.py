from PIL import Image, ImageDraw, ImageFont
from io import BytesIO


def converter_text_in_image(text: str):
    font = ImageFont.truetype("ARLRDBD.TTF", 20)
    text_width, text_height = font.getsize(text)
    print(text_width, text_height)
    img = Image.new('RGB', (1920, 1080), "orange")
    draw = ImageDraw.Draw(img)
    draw.text((5, 5), text, 'black', font)
    bio = BytesIO()
    bio.name = 'image.jpg'
    img.save(bio, 'JPEG')
    bio.seek(0)
    print(bio)
    print(type(bio))
    return bio



