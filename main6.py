import json
import tkinter as tk
from tkinter import ttk
from main6.log import logger
from main6.fonctions import save_with_pillow
from main6.ImageDataLoader import ImageDataLoader
from main6.canvas import PicCanvas
from main6.window import Window
from main6.buttons import ShapeSelectorButton
from main6.ImageData import ImageData
from main6.editor import EditorFrame

# Fonctions

# Instance de chargement des données
imageDataLoader = ImageDataLoader()

# Creation de la fenetre
window =  Window("PicStudio","750x550")

# Frame de l'editeur
editorFrame = EditorFrame(window,relief=tk.GROOVE)

# Bouton d'enregistrement
def save_btn_cmd():
    save_with_pillow(editorFrame.canvas)
    logger.info("Canvas exporter!")

save_btn = tk.Button(window, text="Exporter", command=save_btn_cmd)

# Chargement des données de l'image depuis json
logger.info("Chargement direct de données de basic_geoforme.json")
draw_file = open("basic_geoforme.json")
draw_data = json.load(draw_file)

# Preparation des données
# logger.info("Préparation des données")
# imageDataLoader.load(draw_data)
# Ajout des données 
# editorFrame.canvas.set_imageData(imageDataLoader)
# editorFrame.canvas.draw_image_data()

save_btn.pack()

editorFrame.pack(fill="x")

editorFrame.canvas.update()

editorFrame.canvas.create_shape("rectangle")
editorFrame.canvas.create_shape("line")
editorFrame.canvas.create_shape("ellipse")

   
window.mainloop()