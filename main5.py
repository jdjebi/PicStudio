import logging
import json
import tkinter as tk
from main5.fonctions import hexaColorFromRGB
from main5.ImageDataLoader import ImageDataLoader
from main5.fonctions import save_with_pillow
from main5.canvas import PicCanvas

# Configuration du logger
logging.basicConfig(format='[%(levelname)s] : %(module)s : %(message)s')
logger = logging.getLogger("main")
logger.setLevel(logging.DEBUG)

# Classes

# Instance de chargement des données
imageDataLoader = ImageDataLoader()

# Creation de la fenetre
WINDOW_GEOMETRY = "500x500"
window = tk.Tk()
window.geometry(WINDOW_GEOMETRY)
logger.info("Fenetre crée")

# Creation de la zone de dessin de la fenetre
canvas = PicCanvas(window)
canvas.pack()
logger.info("Canvas crée")

# Bouton d'enregistrement
def save_btn_cmd():
    save_with_pillow(canvas.canvas_size,canvas.imageData)
    logger.info("Canvas exporter!")

save_btn = tk.Button(window, text="Exporter", command=save_btn_cmd)
save_btn.pack()

# Chargement des données de l'image depuis json
logger.info("Chargement direct de données de basic_geoforme.json")
draw_file = open("basic_geoforme.json")
draw_data = json.load(draw_file)

# Preparation des données
logger.info("Préparation des données")
imageDataLoader.load(draw_data)

# Ajout des données 
logger.info("Ajout des données")
canvas.add_imageData(imageDataLoader)
canvas.draw_image_data()

canvas.focus_set()

window.mainloop()