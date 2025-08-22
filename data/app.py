import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Charger les données
df = pd.read_csv("data/health_data.csv")

# Créer l'app Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("📊 Tableau de données santé"),
    dcc.Graph(
        figure=px.scatter(df, x="age", y="bmi", color="gender", title="Age vs BMI")
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
