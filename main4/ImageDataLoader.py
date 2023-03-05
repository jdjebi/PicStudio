class ImageDataLoader:
    _data = None
    width_img = None
    height_img = None
    background_color = None
    img_size = None
    forms = []

    def __init__(self):
        pass

    def load(self,data):
        self._data = data
        self.set_values()
    
    def __str__(self):
        return f"ImageDataLoader(width={self.width_img},height={self.height_img},background={self.ImageDataLoader})"
    
    def set_values(self):
        """ Parametres de l'image """
        self.width_img = self._data["img_params"]["width_img"]
        self.height_img = self._data["img_params"]["height_img"]
        self.background_color = tuple(self._data["img_params"]["background_vector_RGB"])
        self.img_size = (self.width_img,self.height_img)
        self.forms = self.prepare_forms(self._data["drawing_board"]["forms"])
    
    def prepare_forms(self,forms_list):
        """ Collecte les données des formes """
        results = []
        for form in forms_list:
            form["position"] = tuple(form["position"])
            form["fill"] = tuple(form["fill"])
            if form.get("outline"):
                form["outline"] = tuple(form["outline"])
            else:
                form["outline"] = None
            if not form.get("width"):
                form["width"] = None
            results.append(form)
        return results