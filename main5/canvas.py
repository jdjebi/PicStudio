import logging
import tkinter as tk
from .fonctions import hexaColorFromRGB
from .positionners import centerize_placement
from .shape import ShapeBuilder, CanvasShapeDrawer
from .canvas_shape import naive_shape_drap_discrete_position_computer
from .cursor import CursorPosition

logging.basicConfig(format='[%(levelname)s] : %(module)s : %(message)s')
logger = logging.getLogger("PicCanvas")
logger.setLevel(logging.DEBUG)

class PicCanvas(tk.Canvas):
    imageData = None
    canvas_forms_id = []
    canvas_width = 350
    canvas_height = 350
    canvas_size = None
    canvas_bg_color = hexaColorFromRGB((128,128,128))
    canvas_shape_database = {}
    cursor = CursorPosition()
    shapeBuilder = None

    def __init__(self, parent, **kwargs):
        super().__init__(
            parent,
            width=self.canvas_width, 
            height=self.canvas_height, 
            background=self.canvas_bg_color,
            **kwargs
        )
        self.canvas_size = (self.canvas_width,self.canvas_height)
        self.shapeBuilder = ShapeBuilder(self)
        self.canvasShapeDrawer = CanvasShapeDrawer(self)
        self.config_events()
    
    def ping(self):
        print("Yo! I'm PicCanvas")

    def init(self):
        self.canvas_size = self.canvas_width, self.canvas_height

    def config_events(self):
        self.bind("<Motion>",self.canvas_mouve_move)
        #self.bind("<Button-1>",self.canvas_mouse_left_click)
        pass
    
    def add_imageData(self, imageData):
        """ Permet de definit l'instance contenant les donnees de l'image """
        self.imageData = imageData
    
    def draw_image_data(self):
        """ Dessination des formes de l'image sur la canvas """
        self.canvas_forms_id = []
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
                self.canvas_forms_id.append(cform)
            else:
                logger.warning(f"Form {form['form']} non pris en charge")
    
    def create_shape(self,shape_name):
        form = self.shapeBuilder.build(shape_name)
        cform_id = self.canvasShapeDrawer.draw(form)
        self.canvas_forms_id.append(cform_id)
        self.imageData.forms.append(form)
        logger.info(f"Creation de la forme : '{form['form']}' avec : {form}")
        self.config_shape_event(cform_id)
        return cform_id

    def canvas_mouve_move(self,event):
        self.cursor.update(event.x,event.y)

    def canvas_mouse_left_click(self,event):
        logger.info(f"Canvas MouseLeftClick ({event})")
        rect_default_width = 50
        rect_default_height = 50
        rect_pos = centerize_placement(event.x,event.y,rect_default_width,rect_default_height,offset=(3,5))
        # Enregistrement de la forme dans le imageDataLoader
        form = {
            "form":"rectangle",
            "position": rect_pos,
            "fill": None,
            "outline": (0,0,0)
        }
        self.imageData.forms.append(form)
        # Normalement on doit memoriser la forme ici
        # cform = canvas.create_rectangle(rect_pos)
        self.create_rectangle(rect_pos) 
        logger.info(f"Set Rectangle at {rect_pos} avec {form}")
    
    """ Modification effectuee sur les formes """
    
    """ Evenements associes aux formes """

    def get_current_shape_id(self):
        return self.find_withtag('current')[0]
    
    def log_shape_event(self,shape_id,event):
        logger.debug(f"Shape #{shape_id}: {event}")


    def config_shape_event(self,shape_id):
        """ Permet de configurer les evenements associes aux formes """
        self.tag_bind(shape_id,"<Enter>", self.shape_mouse_enter_event)
        self.tag_bind(shape_id,"<B1-Motion>", self.shape_drag_event)

    def shape_mouse_enter_event(self,event):
        shape_id = self.get_current_shape_id()
        self.log_shape_event(shape_id,event)
    
    def shape_drag_event(self,event):
        shape_id = self.get_current_shape_id()
        self.log_shape_event(shape_id,event)
        dx, dy = naive_shape_drap_discrete_position_computer(event,self,shape_id)
        self.move(shape_id,dx,dy)
        logger.debug(f"Move Shape #{shape_id} with {(dx, dy)}")   

        # Mise a jour de ImageData (La mise est local) | Ce traitenement ne pas de faire ici
        position = self.coords(shape_id)
        self.imageData.forms[0]["position"] = tuple(position)
        logger.debug(f"Shape #{shape_id} is now at {position}")   
