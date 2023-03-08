import tkinter as tk

# Crée une fenêtre principale
root = tk.Tk()

# Crée une frame avec une largeur initiale de 200 pixels
my_frame = tk.Frame(root, width=200, height=100, bg="blue")
my_frame.pack()

# Crée plusieurs Labels et les ajoute à la Frame avec la méthode pack
label1 = tk.Label(my_frame, text="Label 1", bg="red")
label1.pack(fill="x",expand=True)
label2 = tk.Label(my_frame, text="Label 2", bg="green")
label2.pack(fill="x",expand=True)
label3 = tk.Label(my_frame, text="Label 3", bg="yellow")
label3.pack(fill="x",expand=True)

# Lance la boucle principale de la fenêtre
root.mainloop()





