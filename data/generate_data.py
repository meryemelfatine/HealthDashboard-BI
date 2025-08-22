import pandas as pd

# Création d'un petit dataset fictif
data = {
    "country": ["France", "France", "France", "Morocco", "Morocco", "Morocco", "USA", "USA", "USA"],
    "year": [2018, 2019, 2020, 2018, 2019, 2020, 2018, 2019, 2020],
    "life_expectancy": [82.5, 82.6, 82.4, 76.5, 76.7, 76.6, 78.7, 78.8, 78.5],
    "health_expenditure_per_capita": [4500, 4600, 4700, 1500, 1600, 1700, 10000, 10500, 11000],
    "infant_mortality_rate": [3.1, 3.0, 3.2, 18.0, 17.5, 17.8, 5.5, 5.4, 5.6]
}

df = pd.DataFrame(data)

# Sauvegarder dans le dossier data/
df.to_csv("data/health_data.csv", index=False)

print("✅ Dataset fictif créé dans data/health_data.csv")
