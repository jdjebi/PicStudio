from main7.tkinter import *
from main7.log import logger


class ShapeInspectorFrame(tk.Frame):
    window=None
    editor=None
    shape_id_var = None
    shape_name_var = None

    def __init__(self, editor, **kwargs):
        super().__init__(editor,**kwargs)
        self.editor = editor
        self.shape_id_var = tk.StringVar(self)
        self.shape_name_var = tk.StringVar(self)

        frame = tk.Frame(self,width=200,bg="red",borderwidth=2,relief="groove")
        frame.pack()

        block_description = tk.Frame(self,width=100)
        block_description.pack(anchor="w")

        # Bloc de description

        block_name_label = tk.Label(block_description,text="General ")
        block_name_label.grid(row=0,column=0,sticky="w")

        shape_id_label = tk.Label(block_description,text="Forme ID: ")
        shape_id_label.grid(row=1,column=0,sticky="w")
        self.shape_id_label_value = tk.Label(block_description,textvariable=self.shape_id_var)
        self.shape_id_label_value.grid(row=1,column=1,sticky="w")

        shape_name_label = tk.Label(block_description,text="Nom : ")
        shape_name_label.grid(row=2,column=0,sticky="w")
        self.shape_name_label_value = tk.Label(block_description,textvariable=self.shape_name_var)
        self.shape_name_label_value.grid(row=2,column=1,sticky="w")

    def inspect(self,shape):
        logger.info(f"Inspect shape : {shape}")
        self.shape_id_var.set(shape.id)
        self.shape_name_var.set(shape.name)