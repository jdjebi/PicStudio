from main8.tkinter import *
from main8.log import logger
from main8.fonctions import hexaColorFromRGB
from main8.shape import Shape
from main8.fonctions import compute_distance_euclidian_for_2_position

class ShapeInspectorFrame(tk.Frame):
    window=None
    editor=None

    # Description
    shape_id_var:tk.StringVar
    shape_name_var:tk.StringVar

    # Positionnement
    blk_PX_var:tk.IntVar
    blk_PY_var:tk.IntVar
    blk_CX_var:tk.IntVar
    blk_CY_var:tk.IntVar

    # Dimensionnement
    blk_W_var:tk.IntVar
    blk_H_var:tk.IntVar
    blk_B_var:tk.IntVar
    blk_L_var:tk.IntVar

    # Coloration
    block_fill_selector:tk.Label
    block_outline_selector:tk.Label


    def __init__(self, editor, **kwargs):
        super().__init__(editor,**kwargs)
        self.editor = editor

        # Description
        self.shape_id_var = tk.StringVar(self,"?")
        self.shape_name_var = tk.StringVar(self,"?")

        # Positionnement
        self.blk_PX_var = tk.DoubleVar(self,0)
        self.blk_PY_var = tk.DoubleVar(self,0)
        self.blk_CX_var = tk.DoubleVar(self,0)
        self.blk_CY_var = tk.DoubleVar(self,0)

        # Dimensionnement
        self.blk_W_var = tk.DoubleVar(self,0)
        self.blk_H_var = tk.DoubleVar(self,0)
        self.blk_B_var = tk.DoubleVar(self,0)
        self.blk_L_var = tk.DoubleVar(self,0)

        # Frame principale
        frame = tk.Frame(self,width=200,bg="red",borderwidth=2,relief="groove")
        frame.pack()

        # Bloc de description
        block_description = tk.LabelFrame(self,text="General",width=100)
        block_description.pack(anchor="w",fill="x")

        block_name_label = tk.Label(block_description,text="# General ")
        block_name_label.grid(row=0,column=0,sticky="w")

        shape_id_label = tk.Label(block_description,text="Forme ID: ")
        shape_id_label.grid(row=1,column=0,sticky="w")

        self.shape_id_label_value = tk.Label(block_description,textvariable=self.shape_id_var)
        self.shape_id_label_value.grid(row=1,column=1,sticky="w")

        shape_name_label = tk.Label(block_description,text="Nom : ")
        shape_name_label.grid(row=2,column=0,sticky="w")

        self.shape_name_label_value = tk.Label(block_description,textvariable=self.shape_name_var)
        self.shape_name_label_value.grid(row=2,column=1,sticky="w")

        # Bloc de position
        block_position = tk.LabelFrame(self,text="Positionnement",width=100)
        block_position.pack(anchor="w",fill="x")
        # Label Position
        block_position_Position_label = tk.Label(block_position,text="Position")
        block_position_Position_label.grid(row=0,column=0,sticky="w")
        # X
        block_position_X_label = tk.Label(block_position,text="X")
        block_position_X_label.grid(row=0,column=1,sticky="w")
        # X Entry
        block_position_X_entry = ttk.Entry(block_position,width=5,textvariable=self.blk_PX_var)
        block_position_X_entry.grid(row=0,column=2,sticky="w",padx=2)
        # Y
        block_position_Y_label = tk.Label(block_position,text="Y")
        block_position_Y_label.grid(row=0,column=3,sticky="w")
        # Y Entry
        block_position_Y_entry = ttk.Entry(block_position,width=5,textvariable=self.blk_PY_var)
        block_position_Y_entry.grid(row=0,column=4,sticky="w",padx=2)

        # Label Centre
        block_position_Center_label = tk.Label(block_position,text="Centre")
        block_position_Center_label.grid(row=1,column=0,sticky="w")
        # X
        block_position_CX_label = tk.Label(block_position,text="X")
        block_position_CX_label.grid(row=1,column=1,sticky="w",pady=5)
        # X Entry
        block_position_CX_entry = ttk.Entry(block_position,width=5,textvariable=self.blk_CX_var)
        block_position_CX_entry.grid(row=1,column=2,sticky="w",padx=2)
        # Y
        block_position_CY_label = tk.Label(block_position,text="Y",pady=5)
        block_position_CY_label.grid(row=1,column=3,sticky="w")
        # Y Entry
        block_position_CY_entry = ttk.Entry(block_position,width=5,textvariable=self.blk_CY_var)
        block_position_CY_entry.grid(row=1,column=4,sticky="w",padx=2)

        # Block de dimensionnement
        block_dimension = tk.LabelFrame(self,text="Dimension")
        block_dimension.pack(anchor="w",fill="x")
        # Label Taille forme
        block_dim_label = tk.Label(block_dimension,text="Taille forme",pady=5)
        block_dim_label.grid(row=0,column=0,sticky="w")
        # Largeur
        block_width_label = tk.Label(block_dimension,text="Width")
        block_width_label.grid(row=0,column=1,sticky="w")
        # Largeur Entry
        block_width_entry = ttk.Entry(block_dimension,width=5,textvariable=self.blk_W_var)
        block_width_entry.grid(row=0,column=2,sticky="w")
        # Longueur
        block_height_label = tk.Label(block_dimension,text="Height")
        block_height_label.grid(row=0,column=3,sticky="w")
        # Longueur Entry
        block_height_entry = ttk.Entry(block_dimension,width=5,textvariable=self.blk_H_var)
        block_height_entry.grid(row=0,column=4,sticky="w",padx=2)
        # Label Taille borbure 
        block_border_label = tk.Label(block_dimension,text="Taille bordure",pady=5)
        block_border_label.grid(row=1,column=0,sticky="w")
        # Taille borbure Entry
        block_border_entry = ttk.Entry(block_dimension,width=5,textvariable=self.blk_B_var)
        block_border_entry.grid(row=1,column=1,sticky="w",padx=2)
         # Label Lonngueur ligne  
        block_longer_label = tk.Label(block_dimension,text="Longueur ligne",pady=5)
        block_longer_label.grid(row=1,column=0,sticky="w")
        # Taille borbure Entry
        block_longer_entry = ttk.Entry(block_dimension,width=5,textvariable=self.blk_L_var)
        block_longer_entry.grid(row=1,column=1,sticky="w",padx=2)

        # Block de coloration
        block_coloration = tk.LabelFrame(self,text="Coloration")
        block_coloration.pack(anchor="w",fill="x")
        # Couleur de fond
        block_fill_label = tk.Label(block_coloration,text="Couleur de fond",pady=5)
        block_fill_label.grid(row=0,column=0,sticky="w")
        # Fond Entry
        self.block_fill_selector = tk.Label(block_coloration,width=15,borderwidth=2, relief="groove")
        self.block_fill_selector.grid(row=0,column=1,sticky="w",padx=10)
        # Couleur de bordure
        block_outline_label = tk.Label(block_coloration,text="Couleur de bordure",pady=5)
        block_outline_label.grid(row=1,column=0,sticky="w")
        # Bordure Entry
        self.block_outline_selector = tk.Label(block_coloration,width=15,borderwidth=2, relief="groove")
        self.block_outline_selector.grid(row=1,column=1,sticky="w",padx=10)


    def inspect(self,shape:Shape):
        logger.info(f"Inspect shape : {shape}")
        self.update_description(shape)
        self.update_position(shape)
        self.update_coloration(shape)
        self.update_dimension(shape)
    
    def update_description(self,shape:Shape):
        self.shape_id_var.set(shape.id)
        self.shape_name_var.set(shape.name)
    
    def update_position(self,shape:Shape):
        self.blk_PX_var.set(shape.x1)
        self.blk_PY_var.set(shape.y1)
        self.blk_CX_var.set(shape.center_x)
        self.blk_CY_var.set(shape.center_y)
    
    def update_dimension(self,shape:Shape):
        self.blk_W_var.set(shape.width)
        self.blk_H_var.set(shape.height)
        if shape.type == "line":
            true_height = compute_distance_euclidian_for_2_position((shape.x1,shape.y1),(shape.x2,shape.y2))
            self.blk_L_var.set(true_height)
        else:

            if shape.height > shape.width:
                true_height = shape.height
            else:
                true_height = shape.width

            self.blk_L_var.set(true_height)
    
    def update_coloration(self,shape:Shape):
        if(not shape.fill):
            self.block_fill_selector.config(bg=hexaColorFromRGB((128,128,128)))
        else:
            self.block_fill_selector.config(bg=shape.fill)
        if(not shape.outline):
            self.block_outline_selector.config(bg=hexaColorFromRGB((128,128,128)))
        else:
            self.block_outline_selector.config(bg=shape.outline)