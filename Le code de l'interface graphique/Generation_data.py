import pandas as pd
import numpy as np

# Nombre d'exemples à générer
n_samples = 5000

# Génération des données
np.random.seed(42)

data = []
for _ in range(n_samples):
    # Habitat
    habitat = np.random.choice(["Rural", "Urbain"], p=[0.56, 0.44])

    # Region
    region = np.random.choice(["Fes", "Meknes", "Rabat"], p=[0.898, 0.014, 0.088])

    # Sexe et Phototype en fonction de la région
    if region == "Fes":
        sexe = np.random.choice(["Homme", "Femme"], p=[0.374, 0.626])
        phototype = np.random.choice(["I", "II", "III", "IV", "V"], p=[0, 0, 0.132, 0.698, 0.17])
    elif region == "Meknes":
        sexe = np.random.choice(["Homme", "Femme"], p=[0.55, 0.45])
        phototype = np.random.choice(["I", "II", "III", "IV", "V"], p=[0, 0.095, 0.63, 0.18, 0.095])
    elif region == "Rabat":
        sexe = np.random.choice(["Homme", "Femme"], p=[0.21, 0.79])
        phototype = np.random.choice(["I", "II", "III", "IV", "V"], p=[0, 0.044, 0.279, 0.574, 0.103])

    # Age en fonction du sexe
    if sexe == "Homme":
        age = np.random.choice(["[0, 15]", "[15, 45]", "[45, 90]"], p=[0.02, 0.612, 0.368])
    else:
        age = np.random.choice(["[0, 15]", "[15, 45]", "[45, 90]"], p=[0.05, 0.801, 0.149])

    # Profession en fonction de l'âge
    if age == "[0, 15]":
        profession = np.random.choice(["Agriculteur", "Autre", "Sans"], p=[0, 0.1, 0.9])
    elif age == "[15, 45]":
        profession = np.random.choice(["Agriculteur", "Autre", "Sans"], p=[0.17, 0.71, 0.12])
    else:  # age == "[45, 90]"
        profession = np.random.choice(["Agriculteur", "Autre", "Sans"], p=[0.16, 0.23, 0.61])

    # Exposition solaire en fonction de la profession
    if profession == "Agriculteur":
        exposition_solaire = np.random.choice(["Forte", "Moyenne", "Faible"], p=[0.93, 0.06, 0.01])
    elif profession == "Autre":
        exposition_solaire = np.random.choice(["Forte", "Moyenne", "Faible"], p=[0.04, 0.56, 0.4])
    else:  # profession == "Sans"
        exposition_solaire = np.random.choice(["Forte", "Moyenne", "Faible"], p=[0.03, 0.47, 0.5])

    # Ajout des données
    data.append([region, sexe, age,habitat, phototype, profession, exposition_solaire])

# Création du DataFrame
columns = ["Region", "Sexe", "Age", "Habitat", "Phototype", "Profession", "Exposition Solaire"]
df = pd.DataFrame(data, columns=columns)

# Sauvegarde au format CSV
df.to_csv("dataset1.csv", index=False, encoding="utf-8-sig")

print("Dataset généré et sauvegardé dans 'dataset.csv'.")
