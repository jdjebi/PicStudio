from main8.tkinter import *
from main8.shape2.ShapeBounderBox import ShapeBounderBox

class Shape:

    canvas=None
    type=None
    name="Shape"

    # ShapeBounderBox
    bounderBox=None

    # Dictionnaire representant les caracteristiques de la form
    form:dict 
    id:int
    x1:float
    y1:float
    x2:float
    y2:float
    center_x:float
    center_y:float
    width:float
    height:float

    fill = None
    outline = None

    def __init__(self,canvas,id:int,name:str,form:dict):
        self.canvas = canvas
        self.id = id
        self.type = name
        self.name = name.title()
        self.form = form
        self.x1, self.y1, self.x2, self.y2 =self.canvas.coords(id)
        self.fill = canvas.itemcget(id,"fill")
        if self.type=="line":
            self.outline = ""
        else:
            self.outline = canvas.itemcget(id,"outline")
        
        print("Color Map : ",self.name,"-",self.fill,"-",self.outline)

        self.bounderBox = ShapeBounderBox(self,self.canvas)

    def __str__(self):
        return f"{self.name} #{self.id}"

    def internal_update_position_by_canvas(self):
        position = self.canvas.coords(self.id)
        x1, y1, x2, y2 = position
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.width = x2 - x1
        self.height = y2 - y1
        self.center_x =  x1 + (self.width / 2)
        self.center_y = y2 - (self.height / 2)
        self.bounderBox.shape_updated()

    def get_rect(self):
        return self.canvas.coords(self.id)
    
    def selected(self):
        self.bounderBox.show()
    
    def unselected(self):
        self.bounderBox.hide()
