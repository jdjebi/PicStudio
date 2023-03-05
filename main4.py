import logging
import json
import random
import tkinter as tk
from main4.fonctions import hexaColorFromRGB
from main4.ImageDataLoader import ImageDataLoader
from main4.fonctions import save_with_pillow

# Configuration du logger
logging.basicConfig(format='[%(levelname)s] : %(module)s : %(message)s')
logger = logging.getLogger("main")
logger.setLevel(logging.DEBUG)

# Fonction de positionnement
def centerize_placement(x,y,w,h,offset=(0,0)):
        """ 
            Calcul est position de placement de sorte a simulter un positionnement au centre de gravite.
            L'offset permet de creer un decalage pour bien ajuster la forme par rapport au curseur.
        """
        w_middle = int(w/2)
        h_middle = int(h/2)
        x1 = x - w_middle + offset[0]
        y1 = y - h_middle + offset[1]
        x2 = x1 + w
        y2 = y1 + h
        return x1, y1, x2, y2

# Fonction 
def canvas_mouve_move(event):
    #logger.debug(f"Canvas MouseMove ({event})")
    pass
    
def canvas_mouse_left_click(event, canvas, imageDataLoader):
    logger.info(f"Canvas MouseLeftClick ({event})")
    rect_default_width = 50
    rect_default_height = 50
    rect_pos = centerize_placement(event.x,event.y,rect_default_width,rect_default_height,offset=(3,5))
    # Enregistrement de la dans le imageDataLoader
    form = {
        "form":"rectangle",
        "position": rect_pos,
        "fill": None,
        "outline": (0,0,0)
    }
    imageDataLoader.forms.append(form)
    # Normalement on doit memoriser la forme ici
    # cform = canvas.create_rectangle(rect_pos)

    canvas.create_rectangle(rect_pos) 

    logger.info(f"Set Rectangle at {rect_pos} avec {form}")

# Instance de chargement des données
imageDataLoader = ImageDataLoader()

# Creation de la fenetere
WINDOW_GEOMETRY = "500x500"
window = tk.Tk()
window.geometry(WINDOW_GEOMETRY)
logger.info("Fenetre crée")

# Creation de la zone de dessin de la fenetre
canvas_width = 350
canvas_height = 350
canvas_size = canvas_width, canvas_height
canvas_bg_color = hexaColorFromRGB((128,128,128))
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, background=canvas_bg_color)
canvas.focus_set()
canvas.bind("<Motion>",canvas_mouve_move)
canvas.bind("<Button-1>",lambda event: canvas_mouse_left_click(event, canvas, imageDataLoader))
canvas.pack()
logger.info("Canvas crée")

# Bouton d'enregistrement
def save_btn_cmd():
    save_with_pillow(canvas_size,imageDataLoader)
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

# Dessination des formes de l'image sur la canvas
canvas_forms = []
for form in imageDataLoader.forms:
    if form["form"] in ["rectangle","ellipse","line"]:
        logger.info(f"Creation de la forme : '{form['form']}' avec : {form}")
        position = form['position']
        fill = hexaColorFromRGB(form['fill'])
        outline = hexaColorFromRGB(form['outline'])
        width = form['width']
        if(form["form"]=="rectangle"):
            cform = canvas.create_rectangle(position,fill=fill,outline=outline)
        elif(form["form"]=="ellipse"):
            cform = canvas.create_oval(position,fill=fill,outline=outline)
        elif(form["form"]=="line"):
            cform = canvas.create_line(position,fill=fill,width=width)
        canvas_forms.append(cform)
    else:
        logger.warning(f"Form {form['form']} non pris en charge")

# Generation d'un fichier postscripts et conversion du postscripts en png avec PIL

window.mainloop()