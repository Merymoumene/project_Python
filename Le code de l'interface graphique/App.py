import tkinter as tk
from tkinter import ttk
from Page_Map import MapPage
from Page_Statistic import StatisticsPage
from Page_Home import HomePage
from Page_About import AboutPage

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Carte dynamique")
        self.root.geometry("1920x1080")
        self.apply_styles()
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        self.home_page = HomePage(self.notebook)
        self.about_page = AboutPage(self.notebook)
        self.map_page = MapPage(self.notebook, self)
        self.stats_page = StatisticsPage(self.notebook)

        self.notebook.add(self.home_page.frame, text="Home")
        self.notebook.add(self.about_page.frame, text="About")
        self.notebook.add(self.map_page.frame, text="Map")
        self.notebook.add(self.stats_page.frame, text="Statistics")

    def apply_styles(self):
        style = ttk.Style()

        # Personnalisation de l'apparence des onglets
        style.configure("TNotebook",
                        background="white")  # Couleur de fond du notebook

        style.configure("TNotebook.Tab",
                        background="white",  # Couleur de fond des onglets
                        padding=[10, 5],  # Espacement du texte
                        font=("Arial", 12))  # Police de l'onglet

        # Personnalisation de l'onglet sélectionné
        style.map("TNotebook.Tab",
                  background=[("selected", "lightgreen")],  # Couleur de fond de l'onglet sélectionné
                  foreground=[("selected", "orange")])  # Couleur du texte de l'onglet sélectionné

    def show_statistics_page(self, region):
        self.notebook.select(self.stats_page.frame)
        self.stats_page.on_combobox_select_region1(region)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()