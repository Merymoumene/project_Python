import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy.stats import chi2_contingency

class RegionStatistics:
    def __init__(self, dataset_path):
        self.data = pd.read_csv(dataset_path, sep=',')
        self._preprocess_data()

    def _preprocess_data(self):
        def convert_age_range(age_range):
            if pd.isna(age_range):
                return None
            age_range = age_range.strip("[]").split(",")
            return (int(age_range[0]) + int(age_range[1])) / 2

        self.data['Age'] = self.data['Age'].apply(convert_age_range)

    def plot_single_factor(self, region_data, variable):
        variable_counts = region_data[variable].value_counts(normalize=True) * 100
        fig, ax = plt.subplots(figsize=(6, 4))
        variable_counts.plot.pie(autopct='%1.1f%%', cmap="Oranges", ax=ax)
        ax.set_title(f"Répartition de {variable}")
        ax.set_ylabel("")
        interpretation = f"Distribution de {variable} : {', '.join([f'{k} ({v:.1f}%)' for k, v in variable_counts.items()])}."
        return fig, interpretation

    def regression_analysis(self, region_data, target_variable, predictors):
        # Remplacer les espaces par des underscores dans les noms de colonnes
        region_data.columns = region_data.columns.str.replace(' ', '_')

        # Assurez-vous que la colonne cible est numérique
        region_data[target_variable] = pd.to_numeric(region_data[target_variable], errors='coerce')

        # Créez la formule pour la régression
        formula = f"{target_variable} ~ {' + '.join(predictors)}"

        # Appliquer la régression
        model = ols(formula, data=region_data).fit()
        summary = model.summary()

        # Trace des résidus
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.residplot(x=model.fittedvalues, y=model.resid, lowess=True, ax=ax, line_kws={'color': 'red'})
        ax.set_title("Graphique des résidus")
        ax.set_xlabel("Valeurs prédites")
        ax.set_ylabel("Résidus")

        # Interprétation automatique basée sur le modèle
        r_squared = model.rsquared
        p_values = model.pvalues
        coefficients = model.params
        significant_predictors = [predictor for predictor, p_val in p_values.items() if p_val < 0.05]

        # Construction de l'interprétation
        interpretation = f"""
        Analyse de régression pour la variable cible '{target_variable}':
        - R² (proportion de variance expliquée) : {r_squared:.3f}.
        - Prédicteurs significatifs au niveau de 5% : {', '.join(significant_predictors) if significant_predictors else "aucun"}.
        - Coefficients estimés des variables :
        """
        for predictor, coef in coefficients.items():
            p_val = p_values[predictor]
            significance = " (significatif)" if p_val < 0.05 else ""
            interpretation += f"\n    * {predictor} : {coef:.3f} (p-value = {p_val:.3f}){significance}."

        # Note explicative ajoutée
        interpretation += """
        Notes :
        - Une p-value < 0.05 indique que le prédicteur a un effet significatif sur la variable cible.
        - Les coefficients représentent l'effet moyen d'une unité de variation de la variable sur la cible.
        - Vérifiez les hypothèses de la régression (normalité des résidus, homoscédasticité) pour valider les résultats.
        """

        return summary, fig, interpretation

    def chi2_tests(self, region_data, var1, var2):
        contingency_table = pd.crosstab(region_data[var1], region_data[var2])
        chi2, p_value, _, _ = chi2_contingency(contingency_table)

        # Trace des données croisées
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.heatmap(contingency_table, annot=True, fmt="d", cmap="Oranges", ax=ax)
        ax.set_title(f"Tableau de contingence entre {var1} et {var2}")
        ax.set_xlabel(var2)
        ax.set_ylabel(var1)

        interpretation = f"Test du chi² entre {var1} et {var2} : p-value = {p_value}. "
        if p_value < 0.05:
            interpretation += f"Association significative entre {var1} et {var2}."
        else:
            interpretation += f"Aucune association significative entre {var1} et {var2}."
        return fig, interpretation

    # Fonction pour effectuer un test ANOVA
    def anova_test(self, data, dependent_var, independent_var):
        # Renommer les colonnes pour éviter les espaces
        temp_dependent_var = dependent_var.replace(" ", "_")  # Remplacer les espaces par des underscores
        temp_independent_var = independent_var.replace(" ", "_")  # Idem pour la variable indépendante

        # Renommer les colonnes dans le DataFrame
        data = data.rename(columns={dependent_var: temp_dependent_var, independent_var: temp_independent_var})

        # Créer le modèle OLS avec les nouveaux noms de colonnes sans espaces
        model = ols(f'{temp_dependent_var} ~ C({temp_independent_var})', data=data).fit()
        anova_table = sm.stats.anova_lm(model, typ=2)

        # Tracer un graphique
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.boxplot(x=temp_independent_var, y=temp_dependent_var, data=data, ax=ax, palette="Set3",
                    hue=temp_independent_var,
                    dodge=False,
                    legend=False)
        ax.set_title(f"Boxplot de {temp_dependent_var} par {temp_independent_var}")

        # Retourner le tableau ANOVA, l'interprétation et le graphique (fig)
        interpretation = f"Test ANOVA entre {temp_dependent_var} et {temp_independent_var} : "
        if anova_table["PR(>F)"].iloc[0] < 0.05:
            interpretation += f"Différence significative trouvée (p-value = {anova_table['PR(>F)'].iloc[0]})."
        else:
            interpretation += "Pas de différence significative."

        # Retourner le tableau ANOVA, l'interprétation et l'objet graphique (fig)
        return anova_table, interpretation, fig

    def compare_regions(self, regions, factors):
        results = []
        plots = []  # Liste pour stocker les objets Figure de Matplotlib

        for factor in factors:
            for i in range(len(regions)):
                for j in range(i + 1, len(regions)):
                    region1, region2 = regions[i], regions[j]

                    # Filtrage des données pour les deux régions
                    data1 = self.data[self.data["Region"] == region1][factor]
                    data2 = self.data[self.data["Region"] == region2][factor]

                    # Calcul des pourcentages
                    counts1 = data1.value_counts(normalize=True) * 100
                    counts2 = data2.value_counts(normalize=True) * 100

                    # Test Chi²
                    contingency_table = pd.concat([counts1, counts2], axis=1).fillna(0)
                    chi2_stat, p_value, _, _ = chi2_contingency(contingency_table)

                    # Résultat textuel
                    results.append({
                        "Region 1": region1,
                        "Region 2": region2,
                        "Factor": factor,
                        "Percentages Region 1": counts1.to_dict(),
                        "Percentages Region 2": counts2.to_dict(),
                        "Chi2 Statistic": chi2_stat,
                        "P-value": p_value,
                    })

                    # Création de la figure pour Matplotlib
                    fig, ax = plt.subplots()
                    contingency_table.plot.bar(ax=ax, legend=True, cmap="Oranges")
                    ax.set_title(f"Comparaison : {region1} vs {region2}")
                    ax.set_ylabel("Pourcentage")
                    ax.set_xlabel(factor)
                    fig.tight_layout()

                    # Ajouter la figure à la liste des plots
                    plots.append(fig)

        return results, plots

