import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import *
import pandas as pd
import os
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Data_Analyse import RegionStatistics
import random

class FactorsTab:
    def __init__(self, parent):

        self.frame = tk.Frame(parent, bg="white")
        self.frame.pack(fill="both", expand=True)
        self.frtab1 = tk.Frame(self.frame, width=1000, bg='white', bd=1, relief='solid')
        self.frtab1.pack(fill="both", expand=True)
        self.fr1tab1 = tk.Frame(self.frtab1, width=920, height=100, bg='white')
        self.fr1tab1.place(x=10, y=10)
        self.fr2tab1 = tk.Frame(self.frtab1, width=1000, bg='white')
        self.fr2tab1.grid(row=0, column=0, padx=10, pady=120, sticky="nsew")

        self.lab1 = tk.Label(self.fr1tab1, text="Les facteurs de risques :", fg="black", bg="white", font=("Arial", 16))
        self.lab1.place(x=1, y=10)

        self.cmbo1 = ttk.Combobox(
            self.fr1tab1,
            values=("Sexe", "Habitat", "Phototype", "Profession", "Exposition Solaire"),
            state='readonly',
            font=("Arial", 14)
        )
        self.cmbo1.place(x=500, y=15)

class Chi2Tab:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="white")
        self.frame.pack(fill="both", expand=True)
        self.frtab1 = tk.Frame(self.frame, width=1000, bg='white', bd=1, relief='solid')
        self.frtab1.pack(fill="both", expand=True)
        self.fr1tab1 = tk.Frame(self.frtab1, width=920, height=100, bg='white')
        self.fr1tab1.place(x=10, y=10)
        self.fr2tab1 = tk.Frame(self.frtab1, width=1000, bg='white')
        self.fr2tab1.grid(row=0, column=0, padx=10, pady=120, sticky="nsew")
        self.lab1 = tk.Label(self.fr1tab1, text="Le test de chi2 entre deux facteurs :", fg="black", bg="white", font=("Arial", 16))
        self.lab1.place(x=1, y=10)
        self.cmbo1 = ttk.Combobox(
            self.fr1tab1,
            values=[
                "Sexe & Habitat", "Sexe & Phototype", "Sexe & Profession", "Sexe & Exposition Solaire",
                "Habitat & Phototype", "Habitat & Profession", "Habitat & Exposition Solaire",
                "Phototype & Profession", "Phototype & Exposition Solaire", "Profession & Exposition Solaire"
            ],
            state='readonly',
            font=("Arial", 12)
        )
        self.cmbo1.place(x=600, y=15)

class AnovaTab:
    def __init__(self, parent):

        self.frame = tk.Frame(parent, bg="white")
        self.frame.pack(fill="both", expand=True)
        self.frtab1 = tk.Frame(self.frame, width=1000, bg='white', bd=1, relief='solid')
        self.frtab1.pack(fill="both", expand=True)
        self.fr1tab1 = tk.Frame(self.frtab1, width=920, height=100, bg='white')
        self.fr1tab1.place(x=10, y=10)

        self.fr2tab1 = tk.Frame(self.frtab1, width=1000, bg='white')
        self.fr2tab1.grid(row=0, column=0, padx=10, pady=110, sticky="nsew")
        self.lab1 = tk.Label(self.fr1tab1, text="Le test d'anova entre deux facteurs :", fg="black", bg="white", font=("Arial", 16))
        self.lab1.place(x=1, y=10)
        self.cmbo1 = ttk.Combobox(
            self.fr1tab1,
            values=[
                "Sexe & Habitat", "Sexe & Phototype", "Sexe & Profession", "Sexe & Exposition Solaire",
                "Habitat & Phototype", "Habitat & Profession", "Habitat & Exposition Solaire",
                "Phototype & Profession", "Phototype & Exposition Solaire", "Profession & Exposition Solaire"
            ],
            state='readonly',
            font=("Arial", 12)
        )
        self.cmbo1.place(x=600, y=15)

class CorrelationTab:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="white")
        self.frame.pack(fill="both", expand=True)
        self.frtab1 = tk.Frame(self.frame, width=1000, bg='white', bd=1, relief='solid')
        self.frtab1.pack(fill="both", expand=True)
        self.fr1tab1 = tk.Frame(self.frtab1, width=920, height=50, bg='white')
        self.fr1tab1.place(x=10, y=10)
        self.fr2tab1 = tk.Frame(self.frtab1, width=1000, bg='white')
        self.fr2tab1.grid(row=0, column=0, padx=10, pady=60, sticky="nsew")
        self.lab1 = tk.Label(self.fr1tab1, text="la regression linéaire :", fg="black", bg="white",
                             font=("Arial", 16))
        self.lab1.place(x=1, y=10)

class RegionsTab:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="white")
        self.frame.pack(fill="both", expand=True)
        self.frtab1 = tk.Frame(self.frame, width=1000, bg='white', bd=1, relief='solid')
        self.frtab1.pack(fill="both", expand=True)
        self.fr1tab1 = tk.Frame(self.frtab1, width=920, height=100, bg='white')
        self.fr1tab1.place(x=10, y=10)
        self.fr2tab1 = tk.Frame(self.frtab1, width=1000, bg='white')
        self.fr2tab1.grid(row=0, column=0, padx=10, pady=120, sticky="nsew")
        self.lab1 = tk.Label(self.fr1tab1, text="Les regions :", fg="black", bg="white",
                             font=("Arial", 16))
        self.lab1.place(x=1, y=10)
        self.cmbo2 = ttk.Combobox(
            self.fr1tab1,
            values=[
                "Rabat & Fes", "Rabat & Meknes", "Fes & Meknes"],
            state='readonly',
            font=("Arial", 12)
        )
        self.cmbo2.place(x=150, y=14)
        self.lab2 = tk.Label(self.fr1tab1, text="Les facteurs :", fg="black", bg="white",
                             font=("Arial", 16))
        self.lab2.place(x=400, y=10)
        self.cmbo1 = ttk.Combobox(
            self.fr1tab1,
            values=["Sexe", "Habitat", "Phototype", "Profession", "Exposition Solaire"],
            state='readonly',
            font=("Arial", 12)
        )
        self.cmbo1.place(x=550, y=15)

class RapportTab:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="white")
        self.frame.pack(fill="both", expand=True)
        self.frtab1 = tk.Frame(self.frame, width=1000, bg='white', bd=1, relief='solid')
        self.frtab1.pack(fill="both", expand=True)
        tk.Label(self.frtab1, text="Télécharger le rapport sous forme PDF                                                                                                                                                                                                  . "
                 , font=("Arial", 14, "bold"), bg='white',
                 fg='black').pack(pady=10)
        self.cmbo2 = ttk.Combobox(
            self.frtab1,
            values=[
                "Fes", "Meknes", "Rabat","Rabat & Fes", "Rabat & Meknes", "Fes & Meknes"],
            state='readonly',
            font=("Arial", 12)
        )
        self.cmbo2.place(x=500, y=14)
        self.fr1tab1 = tk.Frame(self.frtab1, width=1000, height=600, bg='white')
        self.fr1tab1.pack(pady=10,fill="both", expand=True)
        self.lab1 = tk.Label(self.fr1tab1, text="Veuillez selectionné une région. ",font=("Arial", 14), bg='white', fg='black')
        self.lab1.pack(padx=30,pady=30)


class StatisticsPage:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg='white')
        self.frame.pack(fill="both", expand=True)
        self.canvas = tk.Canvas(self.frame, bg='white')
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.inner_frame = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")
        self.inner_frame.bind("<Configure>", self._on_frame_configure)
        self.fr1 = tk.Frame(self.inner_frame, width=410, height=240, bg='white')
        self.fr1.grid(row=0, column=0, padx=1, pady=1, sticky="nsew")
        label1 = Label(self.fr1, text="DataSet", fg="black", bg="white", font=("Arial", 16))
        label1.place(x=6, y=8)

        button = Button(self.fr1, text="Télécharger le CSV", bg="white", font=("Arial", 10), command=self.save_csv)
        button.place(x=260, y=10)

        # Frame pour afficher les données avec scrollbars
        fr2 = tk.Frame(self.fr1, width=380, height=300, bg='white', bd=1, relief='solid')
        fr2.place(x=3, y=70)

        self.fr3 = tk.Frame(self.inner_frame, width=400, height=500, bg='white')
        self.fr3.grid(row=0, column=0, padx=1, pady=380, sticky="nsew")

        label2 = Label(self.fr3, text="Les régions étudiées :", fg="black", bg="white", font=("Arial", 16))
        label2.place(x=6, y=8)

        self.cmbo = ttk.Combobox(self.fr3,values=('Fes','Meknes','Rabat'),state = 'readonly', font=("Arial", 10))
        self.cmbo.place(x=230, y=13)
        self.cmbo.bind("<<ComboboxSelected>>", self.on_combobox_select_region)

        # Ajouter un canvas pour les scrollbars
        canvas1 = tk.Canvas(fr2, bg='white')
        scrollbar_x = ttk.Scrollbar(fr2, orient='horizontal', command=canvas1.xview)
        scrollbar_x.pack(side='bottom', fill='x')
        scrollbar_y = ttk.Scrollbar(fr2, orient='vertical', command=canvas1.yview)
        scrollbar_y.pack(side='right', fill='y')

        scrollable_frame = tk.Frame(canvas1)

        # Configurer le canvas
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas1.configure(
                scrollregion=canvas1.bbox("all")
            )
        )
        canvas1.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas1.configure(xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set)
        canvas1.pack(side="left", fill="both", expand=True)

        # Charger et afficher les premières lignes du dataset
        data = pd.read_csv("dataset1.csv", sep=',')
        dataset = data.copy()
        self.display_data(scrollable_frame, dataset.head(10))
        variable_counts = data["Region"].value_counts(normalize=True) * 100

        # Créez une figure Matplotlib et ajoutez-y un graphique
        fig, ax = plt.subplots(figsize=(4, 2))
        variable_counts.plot.pie(autopct='%1.1f%%', ax=ax)

        # Passez la figure à FigureCanvasTkAgg
        canvas = FigureCanvasTkAgg(fig, master=self.fr3)  # Utiliser la figure créée ici
        canvas.get_tk_widget().pack(pady=60)
        plt.close(fig)
        self._already_cleared = False
        self.lab = Label(self.fr3,text="Veuillez choisir une région.",font=("Arial", 10), bg="white", fg="black").place(x=1, y=55)
        self.fr4 = tk.Frame(self.inner_frame, width=1900, height=800, bg='white', bd=1, relief='solid')
        self.fr4.grid(row=0, column=1, padx=1, pady=1, sticky="nsew")

        # Créer l'objet notebook
        self.notebook1 = ttk.Notebook(self.fr4)
        self.notebook1.pack(fill="both", expand=True)

        self.tabs = {
            "Facteurs": FactorsTab(self.notebook1),
            "Chi2": Chi2Tab(self.notebook1),
            "ANOVA": AnovaTab(self.notebook1),
            "Regression": CorrelationTab(self.notebook1),
            "Entre deux Regions": RegionsTab(self.notebook1),
            "Télécharger le rapport": RapportTab(self.notebook1),
        }

        for name, tab in self.tabs.items():
            self.notebook1.add(tab.frame, text=name)

        self.par1 = self.tabs["Facteurs"].fr2tab1
        self.par2 = self.tabs["Chi2"].fr2tab1
        self.par3 = self.tabs["ANOVA"].fr2tab1
        self.par4 = self.tabs["Regression"].fr2tab1
        self.par5 = self.tabs["Entre deux Regions"].fr2tab1
        self.par6 = self.tabs["Télécharger le rapport"].fr1tab1
        self.tabs["Facteurs"].cmbo1.bind("<<ComboboxSelected>>", self.on_combobox_select_facteur1)
        self.tabs["Chi2"].cmbo1.bind("<<ComboboxSelected>>", self.on_combobox_select_facteur2)
        self.tabs["ANOVA"].cmbo1.bind("<<ComboboxSelected>>", self.on_combobox_select_facteur3)
        self.tabs["Entre deux Regions"].cmbo2.bind("<<ComboboxSelected>>", self.on_combobox_select_region6)
        self.tabs["Entre deux Regions"].cmbo1.bind("<<ComboboxSelected>>", self.on_combobox_select_facteur5)
        self.tabs["Télécharger le rapport"].cmbo2.bind("<<ComboboxSelected>>", self.on_combobox_select11)

    def on_combobox_select1(self, facteur, region):

        if not facteur or not region:
            tk.Label(self.par1, text="Veuillez sélectionner un facteur et une région.",
                     font=("Arial", 14), bg='white').place(x=10, y=30)
            return

        stats = RegionStatistics("dataset1.csv")
        if 'Region' not in stats.data.columns or 'Sexe' not in stats.data.columns:
            tk.Label(self.par1, text="Les colonnes 'Region' ou 'Sexe' sont absentes du dataset.",
                     font=("Arial", 14), bg='white').place(x=10, y=30)
            return
        self.tabs["Facteurs"].lab1.destroy()
        self.tabs["Facteurs"].lab1 = tk.Label(self.tabs["Facteurs"].fr1tab1, text="Les facteurs de risques de la region "+region+" :", fg="black", bg="white", font=("Arial", 16))
        self.tabs["Facteurs"].lab1.place(x=10, y=10)
        region_data = stats.data[stats.data['Region'] == region]
        plots, interpretation = stats.plot_single_factor(region_data, facteur)


        if plots:
            # Si plots contient une seule figure
            canvas = FigureCanvasTkAgg(plots, master=self.par1)
            canvas.get_tk_widget().pack(pady=10, fill='both',
                                        expand=True)  # Ajustement pour remplir l'espace disponible
            canvas.draw()
            plt.close(plots)

            # Afficher l'interprétation
            if interpretation:

                tk.Label(self.par1, text="Interpertation : "+ interpretation, wraplength=800, justify="left",font=("Arial", 12,"bold"), bg='white', fg='black').pack(pady=20)
            else:
                tk.Label(self.par1, text="Aucune interprétation disponible.", font=("Arial", 14),
                         bg='white').place(x=10, y=30)
        else:
            tk.Label(self.par1, text="Aucune donnée disponible.", font=("Arial", 14),
                     bg='white').place(x=10, y=30)

    def on_combobox_select2(self, facteur, region):
        self.tabs["Chi2"].lab1.destroy()
        self.tabs["Chi2"].lab1 = tk.Label(self.tabs["Chi2"].fr1tab1,
                                              text="Le test de chi2 entre deux facteurs dans la region " + region + " :", fg="black",
                                              bg="white", font=("Arial", 16))
        self.tabs["Chi2"].lab1.place(x=10, y=10)
        if not facteur or not region:
            tk.Label(self.par2, text="Veuillez sélectionner un facteur et une région.",
                     font=("Arial", 14), bg='white').place(x=10, y=30)
            return

        stats = RegionStatistics("dataset1.csv")
        if 'Region' not in stats.data.columns or facteur.split(" & ")[0] not in stats.data.columns or \
                facteur.split(" & ")[1] not in stats.data.columns:
            tk.Label(self.par2, text="Les colonnes nécessaires sont absentes du dataset.",
                     font=("Arial", 14), bg='white').place(x=10, y=30)
            return

        region_data = stats.data[stats.data['Region'] == region]
        facteur1, facteur2 = facteur.split(" & ")

        # Appel de la fonction qui effectue le test du chi2 sur les deux facteurs
        plots, interpretation = stats.chi2_tests(region_data, facteur1, facteur2)

        tk.Label(self.par2, text="Le test de chi2 entre les facteurs : "+ facteur1 + " et "+ facteur2,font=("Arial", 14,"bold"), bg='white', fg='black').pack(pady=10)

        if plots:
            # Si plots contient une seule figure
            canvas = FigureCanvasTkAgg(plots, master=self.par2)
            canvas.get_tk_widget().pack(pady=10, fill='both', expand=True)
            canvas.draw()
            plt.close(plots)

            # Afficher l'interprétation
            if interpretation:
                tk.Label(self.par2, text="Interprétation : " + interpretation, wraplength=800, justify="left",
                         font=("Arial", 12), bg='white', fg='black').pack(pady=20)
            else:
                tk.Label(self.par2, text="Aucune interprétation disponible.", font=("Arial", 14),
                         bg='white').place(x=10, y=30)
        else:
            tk.Label(self.par2, text="Aucune donnée disponible.", font=("Arial", 14),
                     bg='white').place(x=10, y=30)

    def display_anova_table(self, parent_frame, anova_table):

        # Créer un Treeview pour afficher la table
        tree = ttk.Treeview(parent_frame, columns=list(anova_table.columns), show="headings", height=3)
        tree.pack(fill="both", expand=True, pady=10)

        # Configurer les colonnes
        for col in anova_table.columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=200)

        # Insérer les données dans le tableau
        for row in anova_table.itertuples(index=False):
            tree.insert("", "end", values=row)

    def convert_age_to_numeric(self,age):
        age = age.strip("[]").split(",")
        return random.randint(int(age[0]), int(age[1]))

    def on_combobox_select4(self, region):
        self.tabs["Regression"].lab1.destroy()
        self.tabs["Regression"].lab1 = tk.Label(self.tabs["Regression"].fr1tab1,
                                           text="La regression linéaire dans la region " + region + " :",
                                           fg="black",
                                           bg="white", font=("Arial", 16))
        self.tabs["Regression"].lab1.place(x=10, y=10)
        for widget in self.par4.winfo_children():
            widget.destroy()
        stats = RegionStatistics("dataset1.csv")
        data = pd.read_csv("dataset1.csv", sep=',')

        # Filtrage des données pour la région spécifique
        region_data = data[data['Region'] == region]
        region_data['Age'] = region_data['Age'].apply(
            lambda x: (int(x.split(',')[0][1:]) + int(x.split(',')[1][:-1])) / 2)
        target_variable = 'Age'  # Remplacez par le nom de votre variable cible
        predictors = ['Sexe', 'Habitat', 'Phototype', 'Profession', 'Exposition_Solaire']

        summary, fig, interpretation = stats.regression_analysis(region_data, target_variable, predictors)

        if fig:
            # Si plots contient une seule figure
            canvas = FigureCanvasTkAgg(fig, master=self.par4)
            canvas.get_tk_widget().pack(pady=10, fill='both', expand=True)
            canvas.draw()
            plt.close(fig)

        if interpretation:
            tk.Label(self.par4, text="Interprétation : " + interpretation, wraplength=800, justify="left",
                     font=("Arial", 12), bg='white', fg='black').pack(pady=20)

        if summary:
            # Afficher le résumé complet si nécessaire
            tk.Label(self.par4, text=summary.as_text(), wraplength=800, justify="left", font=("Arial", 12), bg="white",
                     fg="black").pack(pady=20)

    def on_combobox_select_facteur1(self,event):
        # Effacer tout le contenu précédent dans fr2tab1
        for widget in self.par1 .winfo_children():
            widget.destroy()
        facteur = self.tabs["Facteurs"].cmbo1.get()
        region = self.cmbo.get()
        self.on_combobox_select1(facteur, region)

    def on_combobox_select_facteur2(self, event):
        # Effacer tout le contenu précédent dans fr2tab1
        for widget in self.par2.winfo_children():
            widget.destroy()

        facteur = self.tabs["Chi2"].cmbo1.get()  # Récupérer la valeur sélectionnée pour les deux facteurs
        region = self.cmbo.get()

        # Appeler la fonction qui gère spécifiquement les tests du Chi2
        self.on_combobox_select2(facteur, region)

    def on_combobox_select_facteur3(self, event):
        # Effacer tout le contenu précédent dans fr2tab1
        for widget in self.par3.winfo_children():
            widget.destroy()

        facteur = self.tabs["ANOVA"].cmbo1.get()  # Récupérer la valeur sélectionnée pour les deux facteurs
        region = self.cmbo.get()

        # Appeler la fonction qui gère spécifiquement les tests du Chi2
        self.on_combobox_select3(region, facteur)

    def on_combobox_select_region4(self):
        for widget in self.par5.winfo_children():
            widget.destroy()

        regions = ["Rabat & Fes", "Rabat & Meknes", "Fes & Meknes"]
        facteurs = ["Sexe", "Habitat", "Phototype", "Profession", "Exposition Solaire"]
        for region in regions:
            region_split = region.split(" & ")
            for facteur in facteurs:
                self.display_comparison_results(region_split, facteur)

    def on_combobox_select_region6(self,event):
        for widget in self.par5.winfo_children():
            widget.destroy()

        region = self.tabs["Entre deux Regions"].cmbo2.get()
        facteurs = ["Sexe", "Habitat", "Phototype", "Profession", "Exposition Solaire"]
        if region:
            region_split = region.split(" & ")
            for facteur in facteurs:
                self.display_comparison_results(region_split, facteur)

    def on_combobox_select_facteur5(self, event):
        for widget in self.par5.winfo_children():
            widget.destroy()

        facteur = self.tabs["Entre deux Regions"].cmbo1.get()

        if facteur:
            regions = ["Rabat & Fes", "Rabat & Meknes", "Fes & Meknes"]
            for region in regions:
                region_split = region.split(" & ")
                self.display_comparison_results(region_split, facteur)

    def on_combobox_select_facteur_region(self):
        for widget in self.par5.winfo_children():
            widget.destroy()

        facteur = self.tabs["Entre deux Regions"].cmbo1.get()
        region = self.tabs["Entre deux Regions"].cmbo2.get()

        region = region.split(" & ")
        self.display_comparison_results(region, facteur)

    def display_comparison_results(self, selected_regions, selected_factor):
        # Effacer les anciens résultats
        if not hasattr(self, '_already_cleared') or not self._already_cleared:
            for widget in self.par5.winfo_children():
                widget.destroy()
            self._already_cleared = True

        regions = selected_regions
        factors = [selected_factor]

        stats = RegionStatistics("dataset1.csv")

        # Appeler la fonction compare_regions pour obtenir les graphiques et interprétations
        results, plots = stats.compare_regions(regions, factors)

        # Afficher les graphiques directement
        for fig in plots:
            canvas = FigureCanvasTkAgg(fig, master=self.par5)
            canvas.get_tk_widget().pack(pady=10, fill='both', expand=True)
            canvas.draw()
            plt.close(fig)  # Fermer la figure pour libérer la mémoire

        # Afficher les interprétations textuelles
        for result in results:
            interpretation = (
                f"Région 1: {result['Region 1']} - Région 2: {result['Region 2']}\n"
                f"Facteur: {result['Factor']}\n"
                f"Chi2 Statistique: {result['Chi2 Statistic']:.2f}, P-value: {result['P-value']:.4f}\n"
                f"Pourcentages:\n"
                f"  {result['Region 1']}: {result['Percentages Region 1']}\n"
                f"  {result['Region 2']}: {result['Percentages Region 2']}\n"
            )
            label = tk.Label(self.par5, text=interpretation, font=("Arial", 12), bg="white", fg="black", justify="left")
            label.pack(pady=10)

    def on_combobox_select_region(self,event):
        selected_value = self.cmbo.get()
        if selected_value == "Fes":
            self.lab = Label(self.fr3,
                             text="Le nombre de patients dans la région est " + selected_value + " 700 patients",
                             font=("Arial", 10), bg="white", fg="black").place(x=1, y=55)
        elif selected_value == "Rabat":
            self.lab = Label(self.fr3,
                             text="Le nombre de patients dans la région est " + selected_value + " 68 patients",
                             font=("Arial", 10), bg="white", fg="black").place(x=1, y=55)
        else:
            self.lab = Label(self.fr3,
                             text="Le nombre de patients dans la région est " + selected_value + " 11 patients",
                             font=("Arial", 10), bg="white", fg="black").place(x=1, y=55)

        # Facteurs
        facteurs = ["Sexe", "Habitat", "Phototype", "Profession", "Exposition Solaire"]
        for widget in self.par1 .winfo_children():
            widget.destroy()
        for widget in self.par2 .winfo_children():
            widget.destroy()
        for widget in self.par3 .winfo_children():
            widget.destroy()
        for widget in self.par4 .winfo_children():
            widget.destroy()
        for facteur in facteurs:
            self.on_combobox_select1(facteur, selected_value)

        # Paires de facteurs
        facteurs2 = [
            "Sexe & Habitat", "Sexe & Phototype", "Sexe & Profession", "Sexe & Exposition Solaire",
            "Habitat & Phototype", "Habitat & Profession", "Habitat & Exposition Solaire",
            "Phototype & Profession", "Phototype & Exposition Solaire", "Profession & Exposition Solaire"
        ]


        for facteur in facteurs2:
            self.on_combobox_select2(facteur, selected_value)

        for facteur in facteurs2:
            self.on_combobox_select3(selected_value, facteur)

        # Appel à la dernière fonction
        self.on_combobox_select4(selected_value)
        self.on_combobox_select_region4()


    def on_combobox_select3(self, region, facteur):
        self.tabs["ANOVA"].lab1.destroy()
        self.tabs["ANOVA"].lab1 = tk.Label(self.tabs["ANOVA"].fr1tab1,
                                          text="Le test d'ANOVA entre deux facteurs dans la region " + region + " :",
                                          fg="black",
                                          bg="white", font=("Arial", 16))
        self.tabs["ANOVA"].lab1.place(x=10, y=10)
        # Charger et filtrer les données
        stats = RegionStatistics("dataset1.csv")
        ddata = pd.read_csv("dataset1.csv", sep=',')
        data = ddata[ddata['Region'] == region]
        facteur1, facteur2 = facteur.split(" & ")

        # Conversion des colonnes si nécessaire
        if 'Age' in data.columns:
            data['Age'] = data['Age'].apply(self.convert_age_to_numeric)
        if 'Sexe' in data.columns:
            data['Sexe'] = data['Sexe'].map({'Femme': 0, 'Homme': 1})
        if 'Habitat' in data.columns:
            data['Habitat'] = data['Habitat'].map({'Rural': 0, 'Urbain': 1})
        if 'Phototype' in data.columns:
            data['Phototype'] = data['Phototype'].map({'I': 0, 'II': 1, 'III': 2, 'IV': 3, 'V': 4})
        if 'Profession' in data.columns:
            data['Profession'] = data['Profession'].map({'Agriculteur': 0, 'Sans': 1, 'Autre': 2})
        if 'Exposition Solaire' in data.columns:
            valid_exposition_values = ['Forte', 'Moyenne', 'Faible']
            data = data[data['Exposition Solaire'].isin(valid_exposition_values)]
            data['Exposition Solaire'] = data['Exposition Solaire'].map({'Forte': 0, 'Moyenne': 1, 'Faible': 2})

        # Test ANOVA
        dependent_var = facteur1  # Ex : variable dépendante
        independent_var = facteur2  # Ex : variable indépendante

        try:
            # Exemple statique
            tk.Label(self.par3, text="Le test d'ANOVA entre les facteurs : "+ dependent_var + " et "+ independent_var,font=("Arial", 14,"bold"), bg='white', fg='black').pack(pady=10)
            lab1 = tk.Label(self.par3, text="Tableau d'ANOVA : ", font=("Arial", 12), bg="white", justify="center")
            lab1.pack(anchor="w", pady=10)  # Aligné à gauche

            anova_table, interpretation, fig = stats.anova_test(data, dependent_var, independent_var)

            # Afficher la table ANOVA dans un Treeview
            self.display_anova_table(self.par3, anova_table)

            # Afficher l'interprétation
            label_interpretation = tk.Label(self.par3, text=interpretation, font=("Arial", 12), bg="white",
                                            justify="left")
            label_interpretation.pack(pady=10)

            # Afficher le graphique
            canvas = FigureCanvasTkAgg(fig, master=self.par3)
            canvas.get_tk_widget().pack(pady=10, fill='both', expand=True)
            canvas.draw()
            plt.close(fig)  # Fermer la figure après affichage

        except Exception as e:
            error_label = tk.Label(self.par3, text=f"Erreur : {e}", font=("Arial", 12), bg="white", fg="red")
            error_label.pack(pady=20)

    def on_combobox_select11(self,event):
        region = self.tabs["Télécharger le rapport"].cmbo2.get()
        if not region:
            tk.Label(self.par6, text="Veuillez sélectionner un facteur et une région.",
                     font=("Arial", 14), bg='white').place(x=10, y=30)
            return

        self.tabs["Télécharger le rapport"].lab1.destroy()
        self.tabs["Télécharger le rapport"].lab1 = tk.Label(self.tabs["Télécharger le rapport"].fr1tab1, text="Télécharger la rapport PDF qui contient tout les statistiques sur le Cancer de la Peau dans la région "+region+".                                  .",font=("Arial", 14), bg='white', fg='black')
        self.tabs["Télécharger le rapport"].lab1.place(x=10, y=10)
        button3 = Button(self.par6, text="Télécharger le PDF", bg="orange", fg="white",font=("Arial", 16),bd=0, command=self.save_pdf)
        button3.place(x=400, y=200)

    def on_combobox_select_region1(self,selected_value):
        self.cmbo.set(selected_value)
        if selected_value == "Fes":
            self.lab = Label(self.fr3,
                             text="Le nombre de patients dans la région est " + selected_value + " 700 patients",
                             font=("Arial", 10), bg="white", fg="black").place(x=1, y=55)
        elif selected_value == "Rabat":
            self.lab = Label(self.fr3,
                             text="Le nombre de patients dans la région est " + selected_value + " 68 patients",
                             font=("Arial", 10), bg="white", fg="black").place(x=1, y=55)
        else:
            self.lab = Label(self.fr3,
                             text="Le nombre de patients dans la région est " + selected_value + " 11 patients",
                             font=("Arial", 10), bg="white", fg="black").place(x=1, y=55)

        # Facteurs
        facteurs = ["Sexe", "Habitat", "Phototype", "Profession", "Exposition Solaire"]
        for facteur in facteurs:
            self.on_combobox_select1(facteur, selected_value)

        # Paires de facteurs
        facteurs2 = [
            "Sexe & Habitat", "Sexe & Phototype", "Sexe & Profession", "Sexe & Exposition Solaire",
            "Habitat & Phototype", "Habitat & Profession", "Habitat & Exposition Solaire",
            "Phototype & Profession", "Phototype & Exposition Solaire", "Profession & Exposition Solaire"
        ]


        for facteur in facteurs2:
            self.on_combobox_select2(facteur, selected_value)

        for facteur in facteurs2:
            self.on_combobox_select3(selected_value, facteur)

        # Appel à la dernière fonction
        self.on_combobox_select4(selected_value)
        self.on_combobox_select_region4()

    def display_data(self, parent_frame, data):
        # Configurer la grille pour une adaptation automatique
        for i in range(len(data.columns)):
            parent_frame.grid_columnconfigure(i, weight=1)

        # Afficher les en-têtes des colonnes
        for i, col in enumerate(data.columns):
            header = Label(parent_frame, text=col, bg='lightgray', font=('Arial', 10, 'bold'), padx=5, pady=5)
            header.grid(row=0, column=i, sticky='nsew')

        # Afficher les lignes du DataFrame
        for i, row in data.iterrows():
            for j, value in enumerate(row):
                cell = Label(parent_frame, text=value, bg='white', font=('Arial', 10), padx=5, pady=5)
                cell.grid(row=i+1, column=j, sticky='nsew')

    def save_pdf(self):
        region = self.tabs["Télécharger le rapport"].cmbo2.get()
        # Chemin du fichier PDF existant dans le dossier du projet
        source_file_path = os.path.join(os.getcwd(), "PDF/"+region+".pdf")

        if not os.path.exists(source_file_path):
            print("Le fichier  n'existe pas dans le dossier du projet.")
            return

        # Ouvrir une boîte de dialogue pour choisir l'emplacement de sauvegarde
        destination_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("Fichier PDF", "*.pdf"), ("Tous les fichiers", "*.*")],
            title="Enregistrer le fichier PDF"
        )

        if destination_path:  # Si l'utilisateur choisit un chemin
            # Copier le fichier source vers le chemin de destination
            with open(source_file_path, 'rb') as src_file:  # Mode binaire pour la lecture
                with open(destination_path, 'wb') as dest_file:  # Mode binaire pour l'écriture
                    dest_file.write(src_file.read())
            print(f"Fichier PDF sauvegardé à : {destination_path}")
        else:
            print("Sauvegarde annulée.")

    def save_csv(self):
        # Chemin du fichier CSV existant dans le dossier du projet
        source_file_path = os.path.join(os.getcwd(), "dataset1.csv")

        if not os.path.exists(source_file_path):
            print("Le fichier dataset1.csv n'existe pas dans le dossier du projet.")
            return

        # Ouvrir une boîte de dialogue pour choisir l'emplacement de sauvegarde
        destination_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("Fichier CSV", "*.csv"), ("Tous les fichiers", "*.*")],
            title="Enregistrer le fichier CSV"
        )

        if destination_path:  # Si l'utilisateur choisit un chemin
            # Copier le fichier source vers le chemin de destination
            with open(source_file_path, 'r') as src_file:
                with open(destination_path, 'w') as dest_file:
                    dest_file.write(src_file.read())
            print(f"Fichier CSV sauvegardé à : {destination_path}")
        else:
            print("Sauvegarde annulée.")

    def _on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    plt.close('all')