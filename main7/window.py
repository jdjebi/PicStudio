import tkinter as tk
from .log import logger
from main7.editor.EditorFrame import EditorFrame
from .StatusBarFrame import StatusBarFrame
from main7.fonctions import save_with_pillow

class Window(tk.Tk):
    window_geometry = "500x500"
    win_title = "PicStudio"

    # Frame de la barre d'etat
    statusBarFrame:StatusBarFrame

    # Frame de l'editeur
    editorFrame:EditorFrame

    # Bouton d'exportation des images
    save_btn:tk.Button

    def __init__(self,title:str,win_size:str,**kwargs):
        super().__init__(**kwargs)
        self.win_title = title
        self.window_geometry = win_size
        self.title(title)
        self.geometry(self.window_geometry)

        self.editorFrame = EditorFrame(self,relief=tk.GROOVE)
        self.statusBarFrame = StatusBarFrame(self)
        self.save_btn = tk.Button(self, text="Exporter", command=self.save_btn_cmd)

        logger.info("Fenetre crée")
    
    """ Evenement """
    def save_btn_cmd(self):
        save_with_pillow(self.editorFrame.canvas)
        logger.info("Canvas exporter!")