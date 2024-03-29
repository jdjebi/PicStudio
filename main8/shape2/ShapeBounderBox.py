""" 
    Cette classe est composant, une shape qui d'embarquer tous les élements 
    permettant de modifier les dimensions d'une Shape graphiquement 
"""
from main8.tkinter import *
from main8.log import logger
from main8.fonctions import hexaColorFromRGB

class ShapeBounderBox:

    canvas:tk.Canvas=None
    canvas_id:int
    canvas_tag:str

    offset:int = 8

    # BoxResizerShapeId
    topboxResizerShapeId:int
    bottomboxResizerShapeId:int
    leftboxResizerShapeId:int
    rightboxResizerShapeId:int

    def __init__(self,shape,canvas):
        self.shape=shape
        self.canvas=canvas
        
        # Créé la bounderbox
        self.create_bounderbox()

        # Créé la topbox qui permet de modifier la taille sur
        self.create_topbox_resizer()
  
    def hide(self):
        self.canvas.itemconfigure(self.canvas_id,state="hidden")
        self.canvas.itemconfigure(self.topboxResizerShapeId,state="hidden")

    def show(self):
        self.canvas.itemconfigure(self.canvas_id,state="normal")
        self.canvas.itemconfigure(self.topboxResizerShapeId,state="normal")
    
    def shape_updated(self):
        # Mise a jour de la BounderBox
        rect_bounderbox = self.get_rect_from_shape()
        self.canvas.coords(self.canvas_id,rect_bounderbox)

        # Mise a jour de TopBox
        rect_bounderbox = self.get_topbox_rect_from_bounderbox()
        self.canvas.coords(self.topboxResizerShapeId,rect_bounderbox)

        logger.debug(f"Mise a jour de la BounderBox de la forme {self.shape}")
    
    """ BounderBox """
    def create_bounderbox(self):
        rect = self.get_rect_from_shape()
        self.canvas_id = self.canvas.create_rectangle(rect,dash=(2,),outline="blue",state="hidden",width=1)
    
    def get_rect_from_shape(self) -> tuple:
        """ Calcul la nouvelle de forme en fonction de la shape"""
        x1, y1, x2, y2 = self.shape.get_rect()
        x1 = x1 - self.offset
        y1 = y1 - self.offset
        x2 = x2 + self.offset
        y2 = y2 + self.offset
        rect = x1, y1, x2, y2
        return rect

    """ TopBoxResizer """
    def create_topbox_resizer(self):
        outline_color = hexaColorFromRGB((0,0,0))
        # hexaColorFromRGB((41,182,242))
        rect = self.get_topbox_rect_from_bounderbox()
        self.topboxResizerShapeId = self.canvas.create_rectangle(rect,fill="blue",outline=outline_color,width=1,state="hidden")

    def get_topbox_rect_from_bounderbox(self) -> tuple:
        """ Calcul la nouvelle de rect de topbox en fonction de de bounderbox """
        shape_size = 6
        x1, y1, x2, y2 = self.canvas.coords(self.canvas_id)  
        x1 = x1 + (x2 - x1) / 2 - (shape_size / 2)
        y1 = y1 - (shape_size / 2)
        x2 = x1 + shape_size
        y2 = y1 + shape_size
        rect = x1, y1, x2, y2
        return rect

    




