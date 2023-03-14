class ImageData:
    _data = None
    width_img = 500
    height_img = 500
    background_color = (128, 128, 128)
    img_size = (500,500)
    forms = []

    def __init__(self):
        pass

    def load(self,data):
        self._data = data
        self.set_values()
    
    def __str__(self):
        return f"ImageData(width={self.width_img},height={self.height_img},background={self.background_color})"
