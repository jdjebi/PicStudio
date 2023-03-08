import tkinter as tk
from tkinter import ttk

class StatusBarFrame(tk.Frame):

    # Label affichant les coordonnées du curseur dans le canvas
    cursorPositionLabel:ttk.Label
    cursorPositionStrVar:tk.StringVar

    def __init__(self,editor,**kwargs):
        super().__init__(editor,relief=tk.GROOVE,borderwidth=2,pady=3,padx=8)

        self.cursorPositionStrVar = tk.StringVar(self)
        self.cursorPositionLabel = ttk.Label(self,textvariable=self.cursorPositionStrVar)
        self.cursorPositionLabel.pack(side="right")
    
    def updateCursorPosition(self,cursor):
        x, y = cursor.current_position.get()
        cursorPositionStatus = f"X: {x}px, Y: {y}px" 
        self.cursorPositionStrVar.set(cursorPositionStatus)


