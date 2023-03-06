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
window =  Window("PicStudio","650x550")

# Frame de l'editeur
editorFrame = EditorFrame(window,relief=tk.GROOVE)


# Frame des boutons de formes
shapesSelectorFrame = ttk.Frame(editorFrame,borderwidth=2, relief=tk.GROOVE)
shapesSelectorFrame.pack(side="left",fill="y",padx=4,pady=4)

## Boutons de selections des formes
rectangle_btn = ShapeSelectorButton(shapesSelectorFrame,editorFrame.canvas,"rectangle",text="Rectangle")
ellipse_btn = ShapeSelectorButton(shapesSelectorFrame,editorFrame.canvas,"ellipse",text="Ellipse")
line_btn = ShapeSelectorButton(shapesSelectorFrame,editorFrame.canvas,"line",text="Ligne")
rectangle_btn.pack()
ellipse_btn.pack()
line_btn.pack()

# Bouton d'enregistrement
def save_btn_cmd():
    save_with_pillow(editorFrame.canvas_size,editorFrame.imageData)
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
# canvas.set_imageData(imageDataLoader)
# canvas.draw_image_data()

save_btn.pack()
editorFrame.pack(side="right",padx=30)

editorFrame.canvas.update()

shape_id = editorFrame.canvas.create_shape("rectangle")

logger.debug("Ajout des données")

treeview = ttk.Treeview(window) 
treeview.pack(side="left") 

for fid in editorFrame.canvas.canvas_forms_id:
    treeview.insert('', 'end', fid,text=f'Shape #{fid}')
   
window.mainloop()