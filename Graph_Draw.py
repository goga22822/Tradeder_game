import Data
from PIL import Image, ImageDraw, ImageQt

im = Image.new('RGB', (500, 300), (219, 193, 27))
draw = ImageDraw.Draw(im)

# Рисуем красный эллипс с черной оконтовкой.
draw.ellipse((100, 100, 150, 200), fill='red', outline=(0, 0, 0))

# Рисуем синий прямоугольник с белой оконтовкой.
draw.rectangle((200, 100, 300, 200), fill='blue', outline=(255, 255, 255))

# Рисуем розовую линию с шириной в 10 пиксель.
draw.line((350, 200, 450, 100), fill='pink', width=10)

im.