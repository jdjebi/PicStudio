import json
from main8.log import logger
from main8.ImageDataLoader import ImageDataLoader
from main8.window import Window

import tkinter as tk
from tkinter import ttk

# Creation de la fenetre
window =  Window("PicStudio","900x500")

window.editorFrame.canvas.update()

shape = window.editorFrame.canvas.create_shape("rectangle")

def resize_by_adding(x):
    print(x)
    print(shape)
    # La modification directe des proprietes n'a pas d'effet sur le positionnement
    # Il faudra mettre a jour la forme dans le canvas, et faire une mise a jour interne de ses proprietes
    x1 = shape.x1
    y1 = shape.y1
    x2 = shape.x2
    y2 = shape.y2 
    rect = (x1,y1,x2,y2)
    print(rect)
    rect = (x1,y1,x2+1,y2)
    print(rect)
    window.editorFrame.canvas.coords(shape.id,rect)
    shape.internal_update_position_by_canvas()
    window.editorFrame.shapeInspector.inspect(shape)

value = tk.DoubleVar()

scale = tk.Scale(window.editorFrame.shapeInspector, variable=value,command=resize_by_adding)
scale.pack()

window.mainloop()