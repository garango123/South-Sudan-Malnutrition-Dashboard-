============================================================

South Sudan Malnutrition Trends Dashboard (Streamlit)

Ten States + Three Administrative Areas

============================================================

Features:

- Adults malnutrition indicators

- Adolescents malnutrition indicators

- Children malnutrition indicators

- State + admin area comparison

- Trend analysis (time-series simulation / import-ready)

- CSV import (UNICEF / WFP / WHO compatible)

- Power BI export

- SQLite optional backend

============================================================

import streamlit as st import pandas as pd import numpy as np import os import sqlite3

st.set_page_config(page_title="South Sudan Malnutrition Dashboard", layout="wide")

DATA_PATH = "data" os.makedirs(DATA_PATH, exist_ok=True)

============================================================

REGIONS (10 states + 3 admin areas)

============================================================

regions = [ "Warrap", "Northern Bahr el Ghazal", "Western Bahr el Ghazal", "Lakes", "Western Equatoria", "Central Equatoria", "Eastern Equatoria", "Jonglei", "Upper Nile", "Unity", "Pibor Administrative Area", "Ruweng Administrative Area", "Abyei Administrative Area" ]

============================================================

SIMULATED BASELINE DATA (replace with UNICEF/WFP/WHO CSV)

============================================================

@st.cache_data def load_data(): np.random.seed(42)

df = pd.DataFrame({
    "region": regions,

    # Malnutrition prevalence (%)
    "children_stunting": np.random.uniform(20, 65, len(regions)),
    "children_wasting": np.random.uniform(5, 25, len(regions)),
    "children_underweight": np.random.uniform(15, 50, len(regions)),

    "adolescent_malnutrition": np.random.uniform(10, 40, len(regions)),
    "adult_malnutrition": np.random.uniform(8, 35, len(regions)),

    # Health system proxy indicators
    "food_insecurity_index": np.random.uniform(30, 90, len(regions)),
    "health_access_index": np.random.uniform(20, 85, len(regions)),

    # Population risk weighting
    "population_risk_score": np.random.uniform(1, 10, len(regions))
})

return df

============================================================

LOAD DATA

============================================================

df = load_data()

============================================================

SIDEBAR NAVIGATION

============================================================

menu = st.sidebar.selectbox( "Navigation", [ "Overview", "Children Nutrition", "Adolescent Nutrition", "Adult Nutrition", "Regional Comparison", "Risk Index Map (Table)", "Data Import (CSV)", "SQL Database", "Export Data" ] )

============================================================

OVERVIEW

============================================================

if menu == "Overview": st.title("South Sudan Malnutrition Trends Dashboard") st.caption("Adults • Adolescents • Children Nutrition Analysis")

col1, col2, col3 = st.columns(3)

col1.metric("Avg Child Stunting %", f"{df['children_stunting'].mean():.1f}")
col2.metric("Avg Adolescent Malnutrition %", f"{df['adolescent_malnutrition'].mean():.1f}")
col3.metric("Avg Adult Malnutrition %", f"{df['adult_malnutrition'].mean():.1f}")

st.bar_chart(df.set_index("region")["children_stunting"])

============================================================

CHILDREN

============================================================

elif menu == "Children Nutrition": st.header("Children Malnutrition Indicators")

st.subheader("Stunting (%)")
st.bar_chart(df.set_index("region")["children_stunting"])

st.subheader("Wasting (%)")
st.bar_chart(df.set_index("region")["children_wasting"])

st.subheader("Underweight (%)")
st.bar_chart(df.set_index("region")["children_underweight"])

============================================================

ADOLESCENTS

============================================================

elif menu == "Adolescent Nutrition": st.header("Adolescent Nutrition Analysis")

st.line_chart(df.set_index("region")["adolescent_malnutrition"])
st.dataframe(df[["region", "adolescent_malnutrition"]])

============================================================

ADULTS

============================================================

elif menu == "Adult Nutrition": st.header("Adult Malnutrition Trends")

st.line_chart(df.set_index("region")["adult_malnutrition"])

st.dataframe(df[["region", "adult_malnutrition", "health_access_index"]])

============================================================

REGIONAL COMPARISON

============================================================

elif menu == "Regional Comparison": st.header("Cross-Regional Nutrition Comparison")

st.bar_chart(df.set_index("region"))

============================================================

RISK INDEX

============================================================

elif menu == "Risk Index Map (Table)": st.header("Malnutrition Risk Index by Region")

st.dataframe(df.sort_values("population_risk_score", ascending=False))

============================================================

CSV IMPORT

============================================================

elif menu == "Data Import (CSV)": st.header("Import UNICEF / WFP / WHO Dataset")

uploaded = st.file_uploader("Upload CSV", type=["csv"])

if uploaded:
    imported_df = pd.read_csv(uploaded)
    st.success("Data Loaded Successfully")
    st.dataframe(imported_df)

============================================================

SQL DATABASE

============================================================

elif menu == "SQL Database": st.header("SQLite Integration")

db_path = os.path.join(DATA_PATH, "malnutrition.db")
conn = sqlite3.connect(db_path)

df.to_sql("nutrition_data", conn, if_exists="replace", index=False)

query = st.text_area("SQL Query", "SELECT * FROM nutrition_data LIMIT 10")

if st.button("Run Query"):
    result = pd.read_sql_query(query, conn)
    st.dataframe(result)

============================================================

EXPORT

============================================================

elif menu == "Export Data": st.header("Export for Power BI / Excel")

csv_path = os.path.join(DATA_PATH, "south_sudan_malnutrition.csv")
df.to_csv(csv_path, index=False)

st.download_button(
    "Download CSV",
    df.to_csv(index=False),
    file_name="south_sudan_malnutrition.csv",
    mime="text/csv"
)

============================================================

FOOTER

============================================================

st.markdown("---") st.caption("South Sudan Malnutrition Analytics Dashboard - UNICEF/WFP Ready Architecture")
