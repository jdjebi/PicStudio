from tkinter import ttk
import tkinter as tk
from main8.log import logger
from main8.canvas import PicCanvas
from main8.buttons import ShapeSelectorButton
from main8.ShapeExplorerFrame import ShapeExplorerFrame
from main8.editor.ShapeInspectorFrame import ShapeInspectorFrame

class EditorFrame(ttk.Frame):
    window=None
    canvas:PicCanvas
    shapeExplorer:ShapeExplorerFrame
    shapesSelector:ttk.Frame
    shapeInspector:ShapeInspectorFrame
    
    def __init__(self, window, **kwargs):
        super().__init__(window,**kwargs)

        self.window = window

        # Creation de la zone de dessin de la fenetre
        self.canvas = PicCanvas(self)

        # Shape
        self.shapeExplorer = ShapeExplorerFrame(self)

        # Frame des boutons de formes
        self.shapesSelector = ttk.Frame(self,borderwidth=2, relief=tk.GROOVE)
        ## Boutons de selections des formes
        rectangle_btn = ShapeSelectorButton(self.shapesSelector,self.canvas,"rectangle",text="Rectangle")
        rectangle_btn.pack()
        ellipse_btn = ShapeSelectorButton(self.shapesSelector,self.canvas,"ellipse",text="Ellipse")
        ellipse_btn.pack()
        line_btn = ShapeSelectorButton(self.shapesSelector,self.canvas,"line",text="Ligne")
        line_btn.pack()

        # Creation de la frame de l'inspecteur de formes
        self.shapeInspector = ShapeInspectorFrame(self,borderwidth=2,relief=tk.GROOVE,padx=4,pady=4)
        self.shapeInspector.configure(width=300)

        # Placement des frames
        self.shapesSelector.pack(side="left",fill="y",padx=4,pady=4)
        self.shapeExplorer.pack(side="left")
        self.canvas.pack(side="left")
        self.shapeInspector.pack(side="right",fill="y")

    

