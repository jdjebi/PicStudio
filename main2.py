""" Dessine des formes geometriques sur une image de façon generique sur la base d'un fichier """

import random
from PIL import Image, ImageDraw
import json

# Classes
class FormBuilder:
    _data = None
    _name = None
    drawObject = None
    imageDraw = None
    _form = None

    def __init__(self,imageDraw,form_data):
        self.imageDraw = imageDraw
        self._data = form_data
        self.build_form()
    
    def build_form(self):
        self._name = self._data["form"]
        name = self._name
        if name == "ellipse":
            self.create_ellipse()
        elif name == "rectangle":
            self.create_rectangle()
        elif name == "line":
            self.create_line()
    
    def create_ellipse(self):
        position = self._data["position"]
        fill = tuple(self._data["fill"])
        outline = tuple(self._data["outline"])
        self.imageDraw.ellipse(position,fill=fill,outline=outline)

    def create_rectangle(self):
        position = self._data["position"]
        fill = tuple(self._data["fill"])
        outline = tuple(self._data["outline"])
        self.imageDraw.rectangle(position,fill=fill,outline=outline)

    def create_line(self):
        position = self._data["position"]
        fill = tuple(self._data["fill"])
        width = self._data["width"]
        self.imageDraw.line(position,fill=fill,width=width)
    
    def __str__(self):
        return f"{self._name}"

class ImageDataJsonContainer:
    """ Contient les données de l'image issus du format json """
    width_img = None
    height_img = None
    background_vector_RGB = None
    data_json_loaded = None
    img_size = None

    def __init__(self,data_json_dict):
        self.data_json_loaded = data_json_dict
        self.set_img_values()
    
    def set_img_values(self):
        """ Chargement des informations de l'image """
        self.width_img = self.data_json_loaded["img_params"]["width_img"]
        self.height_img = self.data_json_loaded["img_params"]["height_img"]
        self.background_vector_RGB = tuple(self.data_json_loaded["img_params"]["background_vector_RGB"])
        self.img_size = (self.width_img,self.height_img)
    
    def build_forms(self, imageDraw):
        """ Chargement des formes """
        forms_list = self.data_json_loaded["drawing_board"]["forms"]
        for f in forms_list:
            form = FormBuilder(imageDraw,f)
            print(form)

    def __str__(self):
        return f"ImageDataJsonContainer(width={self.width_img},height={self.height_img},background={self.background_vector_RGB})"

# Initilisation

# Chargement du fichier de description des dessins
draw_file = open("basic_geoforme.json")
draw_data = json.load(draw_file)

# Creation de l'instance des donnees de l'image
imageContainer = ImageDataJsonContainer(draw_data)

# Creation d'une image
im = Image.new('RGB',imageContainer.img_size,imageContainer.background_vector_RGB)

# Creation d'une instance de dessin
draw = ImageDraw.Draw(im)

# Dessin des formes sur l'image
imageContainer.build_forms(draw)

# Affichage de l'image
im.show()