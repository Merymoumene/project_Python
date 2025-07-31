import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class HomePage:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.frame.pack(fill="both", expand=True)

        # Image de fond
        image_path = r"images/skin.jpg"
        original_image = Image.open(image_path)

        # Label pour afficher l'image de fond
        background_label = tk.Label(self.frame)
        background_label.place(relwidth=1, relheight=1)

        def resize_background(event):
            try:
                # Obtenir les dimensions de la fenêtre
                new_width = self.frame.winfo_width()
                new_height = self.frame.winfo_height()

                # Redimensionner l'image
                resized_image = original_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
                new_background_image = ImageTk.PhotoImage(resized_image)

                # Mettre à jour le label avec la nouvelle image
                background_label.config(image=new_background_image)
                background_label.image = new_background_image  # Référence persistante pour éviter la suppression
            except Exception as e:
                print(f"Erreur lors du redimensionnement : {e}")

        self.frame.bind("<Configure>", resize_background)

        # Ajouter un titre principal et un texte descriptif à gauche, sans fond
        title_label = tk.Label(self.frame, text="L'étude du cancer de la peau, un geste simple, un avenir plus sûr.", font=("Stencil", 23, "bold"), bg = "#F2D2B2",fg="black")
        title_label.place(relx=0.05, rely=0.7, anchor="w")  # Position en bas à gauche

        subtitle_label = tk.Label(self.frame, text=" Pour en savoir plus sur le cancer de peau, consultez notre page About us.", font=("Revue", 14),  bg = "#F2D2B2",fg="black", justify="left")
        subtitle_label.place(relx=0.05, rely=0.8, anchor="w")  # Texte descriptif en dessous