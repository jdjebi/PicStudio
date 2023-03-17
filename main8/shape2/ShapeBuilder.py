from main8.positionners import centerize_placement

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
            new_form["fill"] = (255,255,255)
            new_form["outline"] = (0,0,0)   
        elif(shape_name == "ellipse"):
            rect_default_width = 50
            rect_default_height = 50
            canvas_x_center = self.canvas.winfo_width() // 2
            canvas_y_center = self.canvas.winfo_height() // 2
            rect_pos = centerize_placement(canvas_x_center,canvas_y_center,rect_default_width,rect_default_height,offset=(3,4))
            new_form["form"] = "ellipse"
            new_form["position"] = rect_pos  
            new_form["fill"] = (255,255,255)  
            new_form["outline"] = (0,0,0)   
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