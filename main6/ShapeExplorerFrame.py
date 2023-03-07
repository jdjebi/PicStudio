from tkinter import ttk
from .log import logger

class ShapeExplorerFrame(ttk.Frame):
    editor = None
    treeview = None
    def __init__(self,editor,**kwargs):
        super().__init__(editor,**kwargs)
        self.editor = editor

        # Creation de la treeview
        self.treeview = ttk.Treeview(editor) 
        self.treeview.pack(side="left") 
        self.initTreeViewData()
    
    def initTreeViewData(self):
        logger.debug("Init ShapeExplorer TreeView")
        for item in self.editor.canvas.canvas_forms_id:
            self.add_item_id(item)
    
    def add_item_id(self, item):
        logger.debug(item)
        logger.debug("Add Shape #{item} to ShapeExplorer TreeView")
        self.treeview.insert('', 'end', item,text=f'Shape #{item }')