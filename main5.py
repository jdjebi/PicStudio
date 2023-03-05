import logging
import json
import tkinter as tk
import tkinter as ttk
from main5.log import logger
from main5.fonctions import hexaColorFromRGB, save_with_pillow
from main5.ImageDataLoader import ImageDataLoader
from main5.canvas import PicCanvas
from main5.window import Window
from main5.buttons import ShapeSelectorButton
from main5 import ImageData

# Fonctions

def addToCanvasShape(event,shape_name):
    logger.info(f"Add {shape_name} : {event}")

# Classes

# Instance de chargement des données
imageDataLoader = ImageDataLoader()

# Creation de la fenetre
window =  Window("PicStudio","600x550")
logger.info("Fenetre crée")

# Frame de l'editeur
editorFrame = ttk.Frame(window,relief=tk.GROOVE)

# Creation de la zone de dessin de la fenetre
canvas = PicCanvas(editorFrame)
canvas.pack(side="right")
logger.info("Canvas crée")

# Frame des boutons de formes
shapesSelectorFrame  = ttk.Frame(editorFrame,borderwidth=2, relief=tk.GROOVE)
shapesSelectorFrame.pack(side="left",fill="y",padx=4,pady=4)

## Boutons de selections des formes
rectangle_btn = ShapeSelectorButton(shapesSelectorFrame,canvas,"rectangle",text="Rectangle")
ellipse_btn = ShapeSelectorButton(shapesSelectorFrame,canvas,"ellipse",text="Ellipse")
line_btn = ShapeSelectorButton(shapesSelectorFrame,canvas,"line",text="Ligne")
rectangle_btn.pack()
ellipse_btn.pack()
line_btn.pack()

# Bouton d'enregistrement
def save_btn_cmd():
    save_with_pillow(canvas.canvas_size,canvas.imageData)
    logger.info("Canvas exporter!")

save_btn = tk.Button(window, text="Exporter", command=save_btn_cmd)

# Chargement des données de l'image depuis json
logger.info("Chargement direct de données de basic_geoforme.json")
draw_file = open("basic_geoforme.json")
draw_data = json.load(draw_file)

# Preparation des données
logger.info("Préparation des données")
imageDataLoader.load(draw_data)

# Ajout des données 
logger.info("Ajout des données")
canvas.add_imageData(ImageData())
#canvas.draw_image_data()

canvas.focus_set()

save_btn.pack()
editorFrame.pack(padx=30)

window.mainloop()