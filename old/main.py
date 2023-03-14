import random
from PIL import Image, ImageDraw

# Constantes

WIDTH_IMG  = 200
HEIGHT_IMG = 200
SIZE_IMG   = 200

# Creation d'une image

im = Image.new('RGB',(WIDTH_IMG,HEIGHT_IMG))

pix = im.load()

for i in range(WIDTH_IMG):
    for j in range(HEIGHT_IMG):
        pix[i,j] = (red,green,blured = i
        green = int(i*0.5 + random.randint(0,127))
        blue = int(j*0.5 + random.randint(0,127)))

# Enregistrement de l'image

im.save('main_img_1.png')

# Affichage de l'image

im.show()
