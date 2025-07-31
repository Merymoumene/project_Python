import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class AboutPage:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.frame.pack(fill="both", expand=True)

        # Canvas for scrolling
        self.canvas = tk.Canvas(self.frame, bg="white")
        self.scroll_y = ttk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scroll_y.set)

        self.scrollable_frame = ttk.Frame(self.canvas, style="White.TFrame")
        # Add canvas and scrollbar to the frame
        self.scroll_y.pack(side="right", fill="y")
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        # Frame for background image
        self.image_frame = ttk.Frame(self.scrollable_frame, style="White.TFrame")
        self.image_frame.pack(fill="x")

        # Label for background image
        self.background_label = tk.Label(self.image_frame, bg="white")  # White background for the image label
        self.background_label.pack(fill="x")

        # background
        self.image_path = r"images/Melanome-header.jpg"  # Change this to the correct path if needed
        self.original_image = Image.open(self.image_path)

        # Update image based on window size
        self.frame.bind("<Configure>", self.resize_background)

        self.add_skin_exam_section()

        self.add_image_and_text_section()
        self.add_image_and_text_section2()
        self.add_image_and_text_section3()
        self.applyStyle()

    def resize_background(self, event):
        new_width = event.width
        new_height = int(self.original_image.height * (new_width / self.original_image.width))
        resized_image = self.original_image.resize((new_width, new_height))
        self.tk_image = ImageTk.PhotoImage(resized_image)
        self.background_label.config(image=self.tk_image)

    def add_skin_exam_section(self):
        # Frame for "Le saviez-vous ?" section
        skin_exam_window = ttk.Frame(self.scrollable_frame, padding=10, style="White.TFrame")
        skin_exam_window.pack(fill="both", expand=True, pady=20)

        # Frame for the image and text
        image_t_frame = ttk.Frame(self.scrollable_frame, padding=10, style="White.TFrame")  # White background
        image_t_frame.pack(fill="x", pady=20)

        # Add first image (Capture1.png)
        image_path = r"images/Capture2.jpg"  # Change this to your image path
        left_image = Image.open(image_path)
        left_image = left_image.resize((400, 400))  # Resize the image
        tk_left_image = ImageTk.PhotoImage(left_image)

        image_label = tk.Label(image_t_frame, image=tk_left_image, bg="white")  # White background
        image_label.image = tk_left_image  # Prevent garbage collection of the image
        image_label.pack(side="left", padx=10)

        # Add title and text to the right of the image
        t_frame = ttk.Frame(image_t_frame, style="White.TFrame")  # White background
        t_frame.pack(side="left", fill="both", expand=True, padx=10)

        title_label = tk.Label(t_frame, text="C'est quoi le mélanome ?", font=("Georgia", 15, "bold"), fg="black",
                               bg="white")
        title_label.pack(anchor="w", pady=5)

        text_label = ttk.Label(t_frame, style="White.TLabel")
        text_label = tk.Label(
            t_frame,
            text="Un cancer de la peau se manifeste par la prolifération incontrôlée et anormale de cellules de la peau, et plus précisément de l'épiderme, la couche externe de la peau. Cette multiplication pathologique est causée par des lésions non réparées de l'ADN, qui entraînent des mutations de ces cellules, venant à former une tumeur maligne."

                 "8 mélanomes sur 10 se développent sur une peau saine, qui ne présente pas de lésion ni de tache. Ce qui rend leur diagnostic délicat.",
            font=("Georgia", 15),
            fg="#333333",
            wraplength=800,
            justify="left",
            bg="white"
        )
        text_label.pack(anchor="w", pady=5)

        # Title for "Le saviez-vous ?"
        title_label = tk.Label(skin_exam_window, text="Le saviez-vous ?", font=("Georgia", 24, "bold"), fg="black",
                               bg="white")
        title_label.pack(pady=20)

        # List of messages to display
        messages = [
            "Le mélanome cutané est une tumeur maligne du système pigmentaire qui se développe à partir des mélanocytes (cellules qui fabriquent la mélanine, responsable de la pigmentation de la peau)\n Une transformation des mélanocytes peut conduire à une prolifération anormale.",
            "Le mélanome représente entre 2 % et 3 % de l'ensemble des cancers. Le mélanome cutané se situe au 8ème rang des cancers chez l'homme et au 6ème rang chez la femme. C'est une tumeur potentiellement agressive surtout lorsqu'elle est prise à un stade tardif et qui peut donner des métastases mettant en jeu le pronostic vital.",
            "De 65 % à 95 % des mélanomes cutanés sont causés par l'exposition aux rayonnements UV. Les radiations solaires et les rayonnements UV émis par des installations de bronzage sont deux des cancérogènes certains pour l'homme pour le mélanome cutané (groupe 1 du CIRC). Le risque cancérogène des UV naturels et artificiels se cumule, et c'est la dose totale d'UV reçue qui détermine le risque cancérogène global.",
            "Le mélanome cutané est une maladie multifactorielle qui dépend principalement de l'interaction entre le type de peau et l'exposition aux UV (période et intensité), ainsi que de facteurs individuels\n (origines ethniques, facteurs génétiques, pigmentation de la peau, comportement).",
            "L'enfance et l'adolescence sont des périodes critiques : une forte exposition\n  au soleil tôt dans la vie augmente le risque de mélanome. \nLes précautions prises tôt réduisent donc ce risque.",
            "Le fait d'avoir été exposé au moins une fois dans sa vie à un appareil émettant des UV artificiels entraîne\n  une augmentation de 15 % du risque de développer un mélanome cutané. Ces appareils sont des cancérogènes avérés, \n et leur danger s’ajoute à celui des rayons UV naturels déjà présents."
        ]

        current_message_index = 0

        # Message label
        message_label = tk.Label(skin_exam_window, text=messages[current_message_index], font=("Calibri", 16),
                                 wraplength=1200, justify="center", bg="#F2D2B2")
        message_label.pack(fill="both", padx=20, pady=20)

        # Function to display a message based on the index
        def show_message(index):
            nonlocal current_message_index
            current_message_index = index
            message_label.config(text=messages[current_message_index])

        # Dash buttons
        dash_buttons_frame = tk.Frame(skin_exam_window, bg="white")
        dash_buttons_frame.pack(pady=10)

        # Function to update dash button color on click
        def update_dash_colors(clicked_index):
            for i, button in enumerate(dash_buttons):
                if i == clicked_index:
                    button.config(fg="black")
                else:
                    button.config(fg="#F2D2B2")

        # Function to create a dash button
        def create_dash_button(index):
            dash_button = tk.Button(dash_buttons_frame, text='\u2014', command=lambda: handle_dash_click(index),
                                    font=("Times New Roman", 20, "bold"), fg="#F2D2B2", borderwidth=0, relief="flat",
                                    bg="white")
            dash_button.pack(side="left", padx=5)
            return dash_button

        # Function to handle dash button clicks
        def handle_dash_click(index):
            update_dash_colors(index)
            show_message(index)

        # Create dash buttons for each message
        dash_buttons = [create_dash_button(i) for i in range(len(messages))]

    def add_image_and_text_section(self):
        # Frame for the image and text section
        image_text_frame = ttk.Frame(self.scrollable_frame, padding=10, style="White.TFrame")
        image_text_frame.pack(fill="x", pady=20)

        # Left image (image1.png)
        image_path = r"images/image1.jpg"
        left_image = Image.open(image_path)
        left_image = left_image.resize((400, 400))
        tk_left_image = ImageTk.PhotoImage(left_image)

        image_label = tk.Label(image_text_frame, image=tk_left_image, bg="white")
        image_label.image = tk_left_image
        image_label.pack(side="left", padx=10)

        # Add title and text to the right of the image
        text_frame = ttk.Frame(image_text_frame, style="White.TFrame")
        text_frame.pack(side="left", fill="both", expand=True, padx=10)

        title_label = ttk.Label(text_frame, text="À quoi ressemble le cancer de la peau ?",
                                font=("Georgia", 15, "bold"), style="White.TLabel")
        title_label.pack(anchor="w", pady=5)

        text_label = ttk.Label(text_frame, style="White.TLabel")
        text_label = tk.Label(
            text_frame,
            text="Cancer de la peau peut arriver à n'importe qui, à n'importe quel âge, sur n'importe quelle partie du corps. Et parce que les cancers de la peau se présentent sous de nombreuses formes et tailles, ils peuvent être difficiles à identifier. Apprendre à connaître votre propre peau et comprendre ce qu'il faut chercher peut vous aider à détecter le cancer à un stade précoce, au moment où il est le plus facile à guérir. "
                 "C'est pourquoi vous devriez examinez votre peau une fois par mois. Si vous voyez quelque chose NOUVEAU ou CHANGEANT n'attendez pas ! Faites-le vérifier par un dermatologue tout de suite. Le dépistage et le traitement précoces du cancer de la peau peuvent vous sauver la vie.",
            font=("Georgia", 15),
            fg="#333333",
            wraplength=800,
            justify="left",
            bg="white"
        )
        text_label.pack(anchor="w", pady=5)

    def add_image_and_text_section2(self):
        # Frame for the image and text section
        image_text_frame = ttk.Frame(self.scrollable_frame, padding=10, style="White.TFrame")  # White background
        image_text_frame.pack(fill="x", pady=20)

        image_path = r"images/Capture4.jpg"
        left_image = Image.open(image_path)
        left_image = left_image.resize((400, 400))
        tk_left_image = ImageTk.PhotoImage(left_image)

        image_label = tk.Label(image_text_frame, image=tk_left_image, bg="white")
        image_label.image = tk_left_image
        image_label.pack(side="left", padx=10)

        # Add title and text to the right of the image
        text_frame = ttk.Frame(image_text_frame, style="White.TFrame")
        text_frame.pack(side="left", fill="both", expand=True, padx=10)

        title_label = ttk.Label(text_frame, text="Quels sont les premiers symptômes d’un cancer de la peau ?",
                                font=("Georgia", 15, "bold"), style="White.TLabel")
        title_label.pack(anchor="w", pady=5)

        text_label = tk.Label(
            text_frame,
            text="Les symptômes du cancer de la peau varient en fonction de son type. Toutefois, les mélanomes et carcinomes se manifestent tous en général par:  "
                 "l’apparition de taches pigmentaires sur la peau, soit sous la forme de tâches de rousseur ou soit par des grains de beauté qui changent de couleur, d'épaisseur ou de forme en quelques semaines ou quelques mois ."
                 "la formation de petites blessures qui semblent ne pas guérir au niveau des paumes des mains ou d’autres emplacements du corps.",
            font=("Georgia", 15),
            fg="#333333",
            wraplength=800,
            justify="left",
            bg="white"
        )
        text_label.pack(anchor="w", pady=5)

    def add_image_and_text_section3(self):
        # Frame for the image and text section
        image_text_frame = ttk.Frame(self.scrollable_frame, padding=10, style="White.TFrame")
        image_text_frame.pack(fill="x", pady=20)

        # Left image (image1.png)
        image_path = r"images/Capture3.jpg"  # Path to your image
        left_image = Image.open(image_path)
        left_image = left_image.resize((400, 400))
        tk_left_image = ImageTk.PhotoImage(left_image)

        image_label = tk.Label(image_text_frame, image=tk_left_image, bg="white")
        image_label.image = tk_left_image
        image_label.pack(side="left", padx=10)

        # Add title and text to the right of the image
        text_frame = ttk.Frame(image_text_frame, style="White.TFrame")
        text_frame.pack(side="left", fill="both", expand=True, padx=10)

        title_label = tk.Label(text_frame, text="Quels sont les causes et facteurs de risque d’un mélanome ?",
                               font=("Georgia", 15, "bold"),
                               bg="white")
        title_label.pack(anchor="w", pady=5)

        text_label = ttk.Label(text_frame, style="White.TLabel")
        text_label = tk.Label(
            text_frame,
            text="Le mélanome de la peau est favorisé par l’exposition aux facteurs de risque suivants :   "
                 "- L'exposition aux rayonnements ultraviolets du soleil ou artificiels sans protection et/ou de manière excessive, en particulier pendant l’enfance.\n"
                 "- Avoir une peau claire : le mélanome touche plus fréquemment les personnes à la peau claire, aux yeux clairs et aux cheveux clairs ou roux.\n"
                 "- Présenter de nombreux grains de beauté est également un facteur de risque : plus une personne possède de grains de beauté, plus le risque de cancer est élevé. Par ailleurs, avoir des grains de beauté d’un diamètre supérieur à 5 mm ou des grains de beauté atypiques augmente le risque de mélanome.\n"
                 "- Être immunodéprimé en raison d'une pathologie ou de la prise de certains médicaments."
                 "- Avoir des antécédents de cancer de la peau : les personnes ayant déjà souffert d’un cancer cutané, qu’il s’agisse d’un des types de mélanomes de la peau ou d’un carcinome, présentent un plus grand risque de développer un mélanome.\n"
                 "- Avoir des antécédents familiaux : avoir dans sa famille une personne qui a eu un cancer de la peau augmente le risque d’en souffrir personnellement. Il s'agit aussi d'un facteur de risque.\n",
            font=("Georgia", 15),
            fg="#1a1a1a",
            wraplength=800,
            justify="left",
            bg="white"
        )
        text_label.pack(anchor="w", pady=5)

    def applyStyle(self):
        style = ttk.Style()

        # style général pour les frames
        style.configure("White.TFrame", background="white")

        # Style général pour les labels
        style.configure("White.TLabel", background="white", foreground="black")

        # Style spécifique pour le notebook (si utilisé ailleurs dans votre application)
        style.configure("TNotebook", background="white")
        style.configure("TNotebook.Tab", background="white", foreground="black")

        # Style pour le scrollbar
        style.configure("Vertical.TScrollbar", troughcolor="white", background="white", arrowcolor="black")