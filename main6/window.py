import tkinter as tk
from .log import logger

class Window(tk.Tk):
    window_geometry = "500x500"
    win_title = "PicStudio"
    def __init__(self,title,win_size,**kwargs):
        super().__init__(**kwargs)
        self.win_title = title
        self.window_geometry = win_size
        self.title(title)
        self.geometry(self.window_geometry)
        logger.info("Fenetre crée")