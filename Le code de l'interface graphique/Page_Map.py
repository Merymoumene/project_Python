from tkinter import ttk
import tkintermapview

class MapPage:
    def __init__(self, parent, app):
        self.app = app
        self.frame = ttk.Frame(parent)
        self.frame.pack(fill="both", expand=True)
        self.map_widget = tkintermapview.TkinterMapView(self.frame, width=1500, height=800, corner_radius=0)
        self.map_widget.set_position(34.020882, -6.84165)
        self.map_widget.set_zoom(8)
        self.map_widget.pack(fill="both", expand=True)
        self.add_markers()

    def add_markers(self):
        regions = {
            "Fes": (34.0331, -5.0003),
            "Meknes": (33.8955, -5.5473),
            "Rabat": (34.020882, -6.84165),
        }
        for region, coords in regions.items():
            self.map_widget.set_marker(coords[0], coords[1], text=region, command=self.create_callback(region))

    def create_callback(self, region):
        return lambda *args: self.app.show_statistics_page(region)
