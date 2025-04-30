import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("UrbanSound8K.csv")

print("Aperçu des données :")
print(data.head())

data.drop_duplicates(inplace=True)

print("\nValeurs manquantes par colonne :")
print(data.isnull().sum())

data.dropna(inplace=True)

print("\nInfos sur les données :")
print(data.info())

print("\nStatistiques descriptives :")
print(data.describe())

numeric_data = data.select_dtypes(include=['number'])
if numeric_data.shape[1] > 1:
    plt.figure(figsize=(10, 6))
    sns.heatmap(numeric_data.corr(), annot=True, cmap="viridis", fmt=".2f")
    plt.title("Matrice de corrélation")
    plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(data=data, x="class", order=data["class"].value_counts().index)
plt.xticks(rotation=45)
plt.title("Distribution des classes sonores")
plt.tight_layout()
plt.show()

data.to_csv("UrbanSound8K_Cleaned.csv", index=False)
print("\n✅ Fichier 'UrbanSound8K_Cleaned.csv' sauvegardé avec succès.")



