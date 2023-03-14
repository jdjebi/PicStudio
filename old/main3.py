""" Dessine des formes geometriques sur une image de façon generique sur la base d'un fichier avec une nouvelle structutre du code """

import random
from PIL import Image, ImageDraw
import json

# Classes
class ImageDataLoader:
    _data = None
    width_img = None
    height_img = None
    background_color = None
    img_size = None
    forms = []

    def __init__(self,data):
        self._data = data
        self.set_values()
    
    def __str__(self):
        return f"ImageDataLoader(width={self.width_img},height={self.height_img},background={self.ImageDataLoader})"
    
    def set_values(self):
        """ Parametres de l'image """
        self.width_img = self._data["img_params"]["width_img"]
        self.height_img = self._data["img_params"]["height_img"]
        self.background_color = tuple(self._data["img_params"]["background_vector_RGB"])
        self.img_size = (self.width_img,self.height_img)
        self.forms = self.prepare_forms(self._data["drawing_board"]["forms"])
    
    def prepare_forms(self,forms_list):
        """ Collecte les données des formes """
        results = []
        for form in forms_list:
            form["position"] = tuple(form["position"])
            form["fill"] = tuple(form["fill"])
            if form.get("outline"):
                form["outline"] = tuple(form["outline"])
            results.append(form)
        return results

class FormDrawer:
    imageDraw = None

    def __init__(self,imageDraw):
        self.imageDraw = imageDraw
    
    def draw(self,form_data):
        name = form_data["form"]
        if name == "ellipse":
            return self.create_ellipse(form_data)
        elif name == "rectangle":
            return self.create_rectangle(form_data)
        elif name == "line":
            return self.create_line(form_data)
    
    def create_ellipse(self,form_data):
        position = form_data["position"]
        fill = form_data["fill"]
        outline = form_data["outline"]
        return self.imageDraw.ellipse(position,fill=fill,outline=outline)

    def create_rectangle(self,form_data):
        position = form_data["position"]
        fill = form_data["fill"]
        outline = form_data["outline"]
        return self.imageDraw.rectangle(position,fill=fill,outline=outline)

    def create_line(self,form_data):
        position = form_data["position"]
        fill = form_data["fill"]
        width = form_data["width"]
        return self.imageDraw.line(position,fill=fill,width=width)
    
    def __str__(self):
        return f"{self._name}"

    
# Initilisation

# Chargement du fichier de description des dessins
draw_file = open("basic_geoforme.json")
draw_data = json.load(draw_file)

# Creation de l'instance des donnees de l'image
imageData = ImageDataLoader(draw_data)

# Creation d'une image
im = Image.new('RGB',imageData.img_size,imageData.background_color)

# Creation d'une instance de dessin
imDraw = ImageDraw.Draw(im)

# Creation d'une instance de construction et dessin de forme sur l'image
formDrawer = FormDrawer(imDraw)

# Ajout des dessins sur l'image
for form in imageData.forms:
    formDrawer.draw(form)

# Enregistrement de l'image
im.save('main3_formegeo.jpg')

# Affichage de l'image
# im.show()