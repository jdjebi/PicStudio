import json
from main7.log import logger
from main7.ImageDataLoader import ImageDataLoader
from main7.window import Window

# Creation de la fenetre
window =  Window("PicStudio","900x550")

window.save_btn.pack()
window.editorFrame.pack(fill="x")
window.statusBarFrame.pack(side="bottom",fill="x")
window.editorFrame.canvas.update()

# Chargement des données de l'image depuis json
logger.info("Chargement direct de données de basic_geoforme.json")
draw_file = open("basic_geoforme.json")
draw_data = json.load(draw_file)

# Preparation des données
logger.info("Préparation des données")
# Instance de chargement des données
imageDataLoader = ImageDataLoader()
imageDataLoader.load(draw_data)
# Ajout des données 
window.editorFrame.canvas.set_imageData(imageDataLoader)
window.editorFrame.canvas.draw_image_data()

window.editorFrame.canvas.create_shape("rectangle")
window.editorFrame.canvas.create_shape("line")
window.editorFrame.canvas.create_shape("ellipse")

window.mainloop()