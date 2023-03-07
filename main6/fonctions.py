""" Fonctions """
from PIL import Image, ImageDraw
from .FormDrawer import FormDrawer


def hexaColorFromRGB(rgb_vector):
    """ Converti une list ou tupe correspondant au format rgb en chaine hexadecimale"""
    if rgb_vector is None:
        return None
    r, g, b = rgb_vector
    return f'#{r:02x}{g:02x}{b:02x}'

def save_with_canvas(canvas):
    """ 
        Enregistre le canvas dans un fichier png l'aide postscript.
        Cette methode exige l'installation de GhostScript pour la conversion postscript en png
    """
    canvas.postscript(file="canvas_tmp.eps")
    img = Image.open("canvas.eps")
    img.save("canvas_postscript.png", "png")

def save_with_pillow(canvas):
    """ Sauvegarde avec pillow en creant une image à partir des données """
    im = Image.new('RGB',canvas.canvas_size,canvas.imageData.background_color)
    imDraw = ImageDraw.Draw(im)
    formDrawer = FormDrawer(imDraw)
    for form in canvas.imageData.forms:
        formDrawer.draw(form)
    im.save('canvas_pillow.png','PNG')