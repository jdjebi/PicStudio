from tkinter import ttk
import tkinter as tk
from .log import logger
from .canvas import PicCanvas
from .buttons import ShapeSelectorButton
from .ShapeExplorerFrame import ShapeExplorerFrame

class EditorFrame(ttk.Frame):
    canvas = None
    shapeExplorer = None
    
    def __init__(self, parent, **kwargs):
        super().__init__(parent,**kwargs)

        # Creation de la zone de dessin de la fenetre
        self.canvas = PicCanvas(self)
        self.canvas.pack(side="right")

        # Shape
        self.shapeExplorer = ShapeExplorerFrame(self)
        self.shapeExplorer.pack(side="left")

        # Frame des boutons de formes
        shapesSelector = ttk.Frame(self,borderwidth=2, relief=tk.GROOVE)
        shapesSelector.pack(side="left",fill="y",padx=4,pady=4)
        ## Boutons de selections des formes
        rectangle_btn = ShapeSelectorButton(shapesSelector,self.canvas,"rectangle",text="Rectangle")
        rectangle_btn.pack()
        ellipse_btn = ShapeSelectorButton(shapesSelector,self.canvas,"ellipse",text="Ellipse")
        ellipse_btn.pack()
        line_btn = ShapeSelectorButton(shapesSelector,self.canvas,"line",text="Ligne")
        line_btn.pack()
