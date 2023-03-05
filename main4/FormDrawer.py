class FormDrawer:
    imageDraw = None

    def __init__(self,imageDraw):
        self.imageDraw = imageDraw
    
    def draw(self,form_data):
        name = form_data["form"]
        if name == "ellipse":
            return self.create_ellipse(form_data)
        elif name == "rectangle":
            return self.create_rectangle(form_data)
        elif name == "line":
            return self.create_line(form_data)
    
    def create_ellipse(self,form_data):
        position = form_data["position"]
        fill = form_data["fill"]
        outline = form_data["outline"]
        return self.imageDraw.ellipse(position,fill=fill,outline=outline)

    def create_rectangle(self,form_data):
        position = form_data["position"]
        fill = form_data["fill"]
        outline = form_data["outline"]
        return self.imageDraw.rectangle(position,fill=fill,outline=outline)

    def create_line(self,form_data):
        position = form_data["position"]
        fill = form_data["fill"]
        width = form_data["width"]
        return self.imageDraw.line(position,fill=fill,width=width)
    
    def __str__(self):
        return f"{self._name}"