from tkinter import ttk
from .log import logger
from .canvas import PicCanvas

class EditorFrame(ttk.Frame):
    canvas = None
    def __init__(self, parent, **kwargs):
        super().__init__(parent,**kwargs)

        # Creation de la zone de dessin de la fenetre
        self.canvas = PicCanvas(self)
        self.canvas.pack(side="right")