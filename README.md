# 🌍 HealthDashboard-BI

Un tableau de bord interactif développé avec **Streamlit**, permettant d’explorer et d’analyser la population mondiale à travers des graphiques dynamiques, cartes et comparaisons entre pays.

---

## 📌 Objectifs du projet

- Offrir une **visualisation claire et interactive** des données de population mondiale.
- Mettre en avant des **KPIs clés** (population totale, croissance moyenne, pays le plus peuplé).
- Permettre une **exploration personnalisée** (sélection de pays, comparaison, filtrage).
- Démontrer des compétences en **Business Intelligence (BI)** avec Python et Streamlit.

---

## 📂 Structure du projet

HealthDashboard-BI/
│── app.py # Script principal Streamlit
│── data/
│ └── world_population.csv # Jeu de données utilisé
│── requirements.txt # Dépendances Python
│── README.md # Documentation du projet
│── screenshots/ # Captures d’écran du dashboard

yaml
Copy
Edit

---

## 🗂️ Jeu de données

- Source : [Our World in Data](https://ourworldindata.org/) / [Kaggle - Global Population](https://www.kaggle.com/)
- Exemple de colonnes :
  - `Country` : Nom du pays
  - `Year` : Année
  - `Population` : Population totale

---

## 🚀 Installation et exécution

### 1. Cloner le dépôt
```bash
git clone https://github.com/meryemelfatine/HealthDashboard-BI.git
cd HealthDashboard-BI
2. Créer un environnement virtuel (optionnel mais recommandé)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
3. Installer les dépendances
bash
Copy
Edit
pip install -r requirements.txt
4. Lancer l’application
bash
Copy
Edit
streamlit run app.py
Puis ouvrir http://localhost:8501 dans le navigateur.

📊 Fonctionnalités du Dashboard
KPIs globaux :

Population totale

Croissance moyenne

Pays le plus peuplé

Visualisations interactives :

📈 Évolution de la population mondiale (courbe)

🏆 Top 10 des pays les plus peuplés (bar chart)

🗺️ Carte interactive mondiale (Plotly choropleth)

⚔️ Comparaison entre deux pays (graphique comparatif)

💡 Insights possibles
Identifier les pays avec la croissance démographique la plus rapide.

Comparer l’évolution entre pays développés et en développement.

Visualiser les tendances mondiales sur plusieurs décennies.

🔧 Technologies utilisées
Python 🐍

Streamlit – création du dashboard

Pandas – manipulation des données

Plotly Express – visualisations interactives

Matplotlib – graphiques complémentaires

📌 Prochaines améliorations
Ajouter d’autres indicateurs (espérance de vie, natalité, mortalité).

Intégrer plusieurs datasets santé (OMS, Our World in Data).

Déploiement sur Streamlit Cloud ou Heroku pour un accès en ligne.

👩‍💻 Auteur
Projet développé par Meryem El Fatine dans le cadre d’un portfolio Data/BI.
N’hésite pas à ⭐ le repo si tu trouves ce projet utile !