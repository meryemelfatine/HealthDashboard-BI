import streamlit as st
import pandas as pd
import plotly.express as px

# --- Charger les données ---
df = pd.read_csv("data/world_population.csv")

# Renommer les colonnes pour simplifier
df.rename(columns={
    "Country/Territory": "Country",
    "2022 Population": "Population",
    "Density (per km²)": "Density",
    "Growth Rate": "GrowthRate"
}, inplace=True)

# Préparer le dataframe long pour les années
year_cols = ["Population", "2020 Population", "2015 Population", 
             "2010 Population", "2000 Population", "1990 Population", 
             "1980 Population", "1970 Population"]

df_long = df.melt(
    id_vars=["Country", "Continent"],
    value_vars=year_cols,
    var_name="Year",
    value_name="PopulationValue"
)

# Nettoyer la colonne Year
df_long["Year"] = df_long["Year"].str.replace(" Population", "")
df_long["Year"] = df_long["Year"].replace({"Population":"2022"}).astype(int)

# --- Configuration page ---
st.set_page_config(page_title="🌍 HealthDashboard", layout="wide")
st.title("🌍 HealthDashboard - World Population")

# --- Sidebar : filtre continent et sélection pays ---
st.sidebar.header("Filtres")
continents = ["All"] + sorted(df["Continent"].unique().tolist())
selected_continent = st.sidebar.selectbox("Filtrer par continent", continents)

if selected_continent != "All":
    df_filtered = df[df["Continent"] == selected_continent]
    df_long_filtered = df_long[df_long["Continent"] == selected_continent]
else:
    df_filtered = df
    df_long_filtered = df_long

countries = df_filtered["Country"].unique()
selected_countries = st.sidebar.multiselect("Choisir les pays à comparer", countries, default=[countries[0]])

# --- Slider année pour les graphiques temporels ---
min_year = df_long_filtered["Year"].min()
max_year = df_long_filtered["Year"].max()
selected_year = st.sidebar.slider("Sélectionner l'année", min_value=int(min_year), max_value=int(max_year), value=int(max_year))

# --- KPIs globaux ---
st.subheader("🌍 Indicateurs Globaux")
col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    st.metric("Population totale", f"{df_filtered['Population'].sum():,}")
with col2:
    st.metric("Population moyenne", f"{df_filtered['Population'].mean():,.0f}")
with col3:
    max_country = df_filtered.loc[df_filtered["Population"].idxmax(), "Country"]
    st.metric("Pays le plus peuplé", max_country)
with col4:
    dens_max_country = df_filtered.loc[df_filtered["Density"].idxmax(), "Country"]
    st.metric("Densité max", dens_max_country)
with col5:
    growth_max_country = df_filtered.loc[df_filtered["GrowthRate"].idxmax(), "Country"]
    st.metric("Croissance max", growth_max_country)
with col6:
    pop_continent = df_filtered.groupby("Continent")["Population"].sum().max()
    st.metric("Continent le plus peuplé", df_filtered.groupby("Continent")["Population"].sum().idxmax())

st.markdown("---")

# --- Top 10 pays les plus peuplés pour l'année sélectionnée ---
st.subheader(f"🏆 Top 10 pays les plus peuplés ({selected_year})")
df_year = df_long_filtered[df_long_filtered["Year"] == selected_year]
top10 = df_year.nlargest(10, "PopulationValue")
fig_top10 = px.bar(top10, x="Country", y="PopulationValue", text="PopulationValue",
                   title=f"Top 10 pays les plus peuplés en {selected_year}", color="PopulationValue")
st.plotly_chart(fig_top10, use_container_width=True)

st.markdown("---")

# --- Carte interactive ---
st.subheader(f"🗺️ Carte interactive - Population {selected_year}")
fig_map = px.choropleth(
    df_year,
    locations="Country",
    locationmode="country names",
    color="PopulationValue",
    hover_name="Country",
    title=f"Population mondiale en {selected_year}",
    color_continuous_scale="Viridis"
)
st.plotly_chart(fig_map, use_container_width=True)

st.markdown("---")

# --- Comparaison multi-pays sur période ---
if selected_countries:
    df_compare = df_long_filtered[df_long_filtered["Country"].isin(selected_countries)]
    st.subheader("⚔️ Comparaison entre pays")
    fig_compare = px.line(df_compare, x="Year", y="PopulationValue", color="Country", markers=True,
                          title="Évolution de la population par pays")
    st.plotly_chart(fig_compare, use_container_width=True)





