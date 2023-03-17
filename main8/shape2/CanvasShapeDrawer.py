from main8.fonctions import hexaColorFromRGB

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