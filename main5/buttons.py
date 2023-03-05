import tkinter as ttk
from .log import logger

class ShapeSelectorButton(ttk.Button):
    shape_name = "shape"
    canvas = None

    def __init__(self,parent,canvas,shape_name,**kwargs):
        super().__init__(parent,command=self.addToCanvasShape,**kwargs)
        self.canvas = canvas
        self.shape_name = shape_name

    def addToCanvasShape(self):
        logger.info(f"Add '{self.shape_name}' request to canvas")
        self.canvas.create_shape(self.shape_name)