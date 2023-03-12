from .positionners import centerize_placement
from .fonctions import hexaColorFromRGB

class Shape:

    canvas=None
    type=None
    name="Shape"

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

        self.fill = canvas.itemcget(id,"fill")

        if self.type=="line":
            self.outline = ""
        else:
            self.outline = canvas.itemcget(id,"outline")
        
        print("Color Map : ",self.name,"-",self.fill,"-",self.outline)



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


class ShapeBuilder:
    """ Construit les formes avec une logique JSON donc de dictionnaire """

    form = {
        "form": None,
        "position": None,
        "fill": None,
        "outline": (0,0,0),
        "width": None
    }

    canvas = None
     
    def __init__(self,canvas):
        self.canvas = canvas

    def build(self,shape_name):
        new_form = self.form.copy()
        if(shape_name == "rectangle"):
            rect_default_width = 50
            rect_default_height = 50
            canvas_x_center = self.canvas.winfo_width() // 2
            canvas_y_center = self.canvas.winfo_height() // 2
            rect_pos = centerize_placement(canvas_x_center,canvas_y_center,rect_default_width,rect_default_height,offset=(3,4))
            new_form["form"] = "rectangle"
            new_form["position"] = rect_pos
            #new_form["fill"] = (0,0,0)
        elif(shape_name == "ellipse"):
            rect_default_width = 50
            rect_default_height = 50
            canvas_x_center = self.canvas.winfo_width() // 2
            canvas_y_center = self.canvas.winfo_height() // 2
            rect_pos = centerize_placement(canvas_x_center,canvas_y_center,rect_default_width,rect_default_height,offset=(3,4))
            new_form["form"] = "ellipse"
            new_form["position"] = rect_pos  
            #new_form["fill"] = (0,0,0)    
        elif(shape_name == "line"):
            rect_default_width = 50
            rect_default_height = 50
            canvas_x_center = self.canvas.winfo_width() // 2
            canvas_y_center = self.canvas.winfo_height() // 2
            rect_pos = centerize_placement(canvas_x_center,canvas_y_center,rect_default_width,rect_default_height,offset=(3,4))
            new_form["form"] = "line"
            new_form["fill"] = (0,0,0)
            new_form["position"] = rect_pos
            new_form["width"] = 1
        else:
            raise Exception("Forme '{shape_name}' inconnue")
        return new_form


class CanvasShapeDrawer:

    canvas = None
     
    def __init__(self,canvas):
        self.canvas = canvas

    def draw(self,form):
        position = form['position']
        fill = hexaColorFromRGB(form['fill'])
        outline = hexaColorFromRGB(form['outline'])
        width = form['width']
        if(form["form"]=="rectangle"):
            cform_id = self.canvas.create_rectangle(position,fill=fill,outline=outline)
        elif(form["form"]=="ellipse"):
            cform_id = self.canvas.create_oval(position,fill=fill,outline=outline)
        elif(form["form"]=="line"):
            cform_id = self.canvas.create_line(position,fill=fill,width=width)
        return cform_id

