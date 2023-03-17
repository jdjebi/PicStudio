""" 
    Cette classe est composant, une shape qui d'embarquer tous les élements 
    permettant de modifier les dimensions d'une Shape graphiquement 
"""
from main8.tkinter import *

class ShapeBounderBox:

    canvas:tk.Canvas=None
    canvas_id:int
    canvas_tag:str

    offset:int = 2

    def __init__(self,shape,canvas):
        self.shape=shape
        self.canvas=canvas
        self.create_bounderbox()
    
    def create_bounderbox(self):
        rect = self.get_rect_from_shape()
        self.canvas_id = self.canvas.create_rectangle(rect,dash=(3,3),outline="blue",state="hidden")

    def get_rect_from_shape(self) -> tuple:
        """ Calcul la nouvelle de forme en fonction de la shape"""
        x1, y1, x2, y2 = self.shape.get_rect()
        x1 = x1 - self.offset
        y1 = y1 - self.offset
        x2 = x2 + self.offset
        y2 = y2 + self.offset
        rect = x1, y1, x2, y2
        return rect

    def hide(self):
        self.canvas.itemconfigure(self.canvas_id,state="hidden")

    def show(self):
        self.canvas.itemconfigure(self.canvas_id,state="normal")




