import logging
import tkinter as tk
from .fonctions import hexaColorFromRGB
from .positionners import centerize_placement
from .canvas_shape import naive_shape_drap_discrete_position_computer
from .cursor import CursorPosition
from .ImageData import ImageData
from main8.shape import Shape, ShapeBuilder, CanvasShapeDrawer

logging.basicConfig(format='[%(levelname)s] : %(module)s : %(message)s')
logger = logging.getLogger("PicCanvas")
logger.setLevel(logging.DEBUG)

class PicCanvas(tk.Canvas):
    canvas_width = 350
    canvas_height = 350
    canvas_size:tuple
    canvas_bg_color = hexaColorFromRGB((128,128,128))
    canvas_forms_id = []
    canvas_shape_database_index = []
    canvas_shape_database_map = {}

    cursor = CursorPosition()
    imageData = ImageData()

    shapeBuilder:ShapeBuilder
    canvasShapeDrawer:CanvasShapeDrawer

    editor = None

    def __init__(self, editor, **kwargs):
        super().__init__(
            editor,
            width=self.canvas_width, 
            height=self.canvas_height, 
            background=self.canvas_bg_color,
            **kwargs
        )
        self.editor = editor
        self.canvas_size = (self.canvas_width,self.canvas_height)
        self.shapeBuilder = ShapeBuilder(self)
        self.canvasShapeDrawer = CanvasShapeDrawer(self)
        self.config_events()
        logger.info("Canvas crée")
    
    def ping(self):
        print("Yo! I'm PicCanvas")

    def init(self):
        self.canvas_size = self.canvas_width, self.canvas_height

    def config_events(self):
        self.bind("<Motion>",self.canvas_mouve_move)
    
    def set_imageData(self, imageData):
        """ Permet de definit l'instance contenant les donnees de l'image """
        self.imageData = imageData
    
    def draw_image_data(self):
        """ Dessination des formes de l'image sur la canvas """
        for form in self.imageData.forms:
            if form["form"] in ["rectangle","ellipse","line"]:
                logger.info(f"Creation de la forme : '{form['form']}' avec : {form}")
                position = form['position']
                fill = hexaColorFromRGB(form['fill'])
                outline = hexaColorFromRGB(form['outline'])
                width = form['width']
                if(form["form"]=="rectangle"):
                    shape_id = self.create_rectangle(position,fill=fill,outline=outline)
                elif(form["form"]=="ellipse"):
                    shape_id = self.create_oval(position,fill=fill,outline=outline)
                elif(form["form"]=="line"):
                    shape_id = self.create_line(position,fill=fill,width=width)
                self.canvas_forms_id.append(shape_id)
                shape = Shape(self,shape_id,form['form'],form)
                self.canvas_shape_database_index.append(id)
                self.canvas_shape_database_map[shape_id] = shape
                self.config_shape_event(shape_id)
                self.register_shape(shape_id,form,shape,form_append=False)
            else:
                logger.warning(f"Form {form['form']} non pris en charge")
    
    """ Manipulation de base des formes """

    def create_shape(self,shape_name) -> Shape:
        # Construit une forme avec une positionnement au centre de la scene
        form = self.shapeBuilder.build(shape_name) 
        logger.info(f"Creation de la forme : '{shape_name}' avec : {form}")
        id = self.canvasShapeDrawer.draw(form)
        shape = Shape(self,id,shape_name,form)
        logger.info(f"Enregistrement de : {shape}")
        self.canvas_shape_database_index.append(id)
        self.canvas_shape_database_map[id] = shape
        self.config_shape_event(id)
        self.register_shape(id,form,shape)
        return shape

    def register_shape(self,cform_id:int,form:dict,shape:Shape,form_append=True):
        """ Effectue toutes les actions neccessaires pour enregistrer et partager les données des objets """
        self.canvas_forms_id.append(cform_id)
        if form_append:
            self.imageData.forms.append(form)
        self.editor.shapeExplorer.add_shape(shape)

    """  Evenements associes aux canvas  """

    def canvas_mouve_move(self,event):
        self.cursor.update(event.x,event.y)
        self.editor.window.statusBarFrame.updateCursorPosition(self.cursor)

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
        
    """ Actions associes aux formes """

    def get_current_shape_id(self):
        return self.find_withtag('current')[0]
    
    def log_shape_event(self,shape_id,event):
        logger.debug(f"Shape #{shape_id}: {event}")

    def config_shape_event(self,shape_id):
        """ Permet de configurer les evenements associes aux formes """
        self.tag_bind(shape_id,"<Enter>", self.shape_mouse_enter_event)
        self.tag_bind(shape_id,"<Button-1>", self.shape_clicked)
        self.tag_bind(shape_id,"<B1-Motion>", self.shape_drag_event)

    def get_current_shape(self):
        id = self.get_current_shape_id()
        return self.get_shape(id)

    def get_shape(self,id) -> Shape:
        return self.canvas_shape_database_map[id]

    """ Evenements """

    def shape_clicked(self,event):
        shape = self.get_current_shape()
        logger.debug(f"{shape} clicked")
        # Mise a jour interne de la forme
        shape.internal_update_position_by_canvas()
        # Mise a jour de l'inspecteur
        self.editor.shapeInspector.inspect(shape)

    def shape_mouse_enter_event(self,event):
        shape_id = self.get_current_shape_id()
        self.log_shape_event(shape_id,event)
    
    def shape_drag_event(self,event):
        shape_id = self.get_current_shape_id()
        shape = self.get_shape(shape_id)
        self.log_shape_event(shape_id,event)
        dx, dy = naive_shape_drap_discrete_position_computer(event,self,shape_id)
        self.move(shape_id,dx,dy)
        logger.debug(f"Move Shape #{shape_id} with {(dx, dy)}") 

        # Mise a jour de ImageData (La mise est local) | Ce traitenement ne pas de faire ici
        position = self.coords(shape_id)
        self.imageData.forms[shape_id-1]["position"] = tuple(position)
        logger.debug(f"Shape #{shape_id} is now at {position}")  

        # Mise a jour interne de la forme
        shape.internal_update_position_by_canvas()

        # Mise a jour de l'inspecteur
        self.editor.shapeInspector.inspect(shape)