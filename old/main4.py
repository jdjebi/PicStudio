import logging
import json
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


# Classes
class PicCanvas(tk.Canvas):
    imageData = None
    canvas_forms_id = []
    canvas_width = 350
    canvas_height = 350
    canvas_bg_color = hexaColorFromRGB((128,128,128))

    def __init__(self, parent, **kwargs):
        super().__init__(
            parent,
            width=self.canvas_width, 
            height=self.canvas_height, 
            background=self.canvas_bg_color,
            **kwargs
        )
        self.config_events()

    def init(self):
        self.canvas_size = self.canvas_width, self.canvas_height

    def config_events(self):
        self.bind("<Motion>",self.canvas_mouve_move)
        self.bind("<Button-1>",self.canvas_mouse_left_click)
    
    def add_imageData(self, imageData):
        """ Permet de definit l'instance contenant les donnees de l'image """
        self.imageData = imageData
    
    def draw_image_data(self):
        """ Dessination des formes de l'image sur la canvas """
        canvas_forms_id = []
        for form in self.imageData.forms:
            if form["form"] in ["rectangle","ellipse","line"]:
                logger.info(f"Creation de la forme : '{form['form']}' avec : {form}")
                position = form['position']
                fill = hexaColorFromRGB(form['fill'])
                outline = hexaColorFromRGB(form['outline'])
                width = form['width']
                if(form["form"]=="rectangle"):
                    cform = self.create_rectangle(position,fill=fill,outline=outline)
                elif(form["form"]=="ellipse"):
                    cform = self.create_oval(position,fill=fill,outline=outline)
                elif(form["form"]=="line"):
                    cform = self.create_line(position,fill=fill,width=width)
                canvas_forms_id.append(cform)
            else:
                logger.warning(f"Form {form['form']} non pris en charge")
    
    def canvas_mouve_move(self,event):
        #logger.debug(f"Canvas MouseMove ({event})")
        pass

    def canvas_mouse_left_click(self,event):
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
        self.create_rectangle(rect_pos) 
        logger.info(f"Set Rectangle at {rect_pos} avec {form}")

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