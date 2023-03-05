""" Dessine des formes geometriques sur une image """

import random
from PIL import Image, ImageDraw

# Constantes

WIDTH_IMG  = 200
HEIGHT_IMG = 200
SIZE_IMG   = 500

# Constates variables

IMG_SHAPE_VECTOR = (SIZE_IMG,SIZE_IMG)
BACKGROUND_VECTOR_RGB = (128, 128, 128)

# Creation d'une image

im = Image.new('RGB',IMG_SHAPE_VECTOR,BACKGROUND_VECTOR_RGB)

# Creation d'une instance de dessin

draw = ImageDraw.Draw(im)

# Dessin des formes

draw.ellipse((100, 100, 150, 200), fill=(255, 0, 0), outline=(0, 0, 0))
draw.rectangle((200, 100, 300, 200), fill=(0, 192, 192), outline=(255, 255, 255))
draw.line((350, 200, 450, 100), fill=(255, 255, 0), width=10)

# Enregistrement de l'image

im.save('main1_formegeometriques.jpg', quality=95)

# Affichage de l'image

im.show()