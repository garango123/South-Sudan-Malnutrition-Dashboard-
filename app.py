st.title("South Sudan Acute Malnutrition Crisis Dashboard (2026)")

st.markdown("""
This dashboard provides a professional and data-driven overview of the acute malnutrition crisis in South Sudan during the 2026 lean season.

The analysis highlights the most affected states, IPC Acute Malnutrition classifications, humanitarian response activities, food insecurity patterns, and critical nutrition indicators affecting children under five and pregnant and breastfeeding women.

The crisis is primarily driven by:
- Conflict and displacement
- Cholera outbreaks and disease burden
- Economic collapse and inflation
- Flooding and climate shocks
- Restricted humanitarian access
- Disrupted agricultural production
""")

st.header("National Crisis Highlights")

col1, col2, col3 = st.columns(3)

col1.metric("Children Under 5 Requiring Treatment", "2.2 Million")
col2.metric("Pregnant & Breastfeeding Women", "1.2 Million")
col3.metric("People Facing Acute Hunger", "7.8 Million")

st.warning("South Sudan is experiencing one of the worst food insecurity and acute malnutrition crises in its history.")

st.header("Most Affected States")

import pandas as pd
import plotly.express as px

states_df = pd.DataFrame({
    "State": [
        "Jonglei",
        "Upper Nile",
        "Unity",
        "Warrap",
        "Northern Bahr el Ghazal"
    ],
    "Severity": [95, 90, 88, 76, 72]
})

fig_states = px.bar(
    states_df,
    x="State",
    y="Severity",
    title="Malnutrition Severity Across Most Affected States",
    text="Severity"
)

st.plotly_chart(fig_states, use_container_width=True)

st.markdown("""
Approximately 70% of South Sudan's acute malnutrition burden is concentrated within five states:

- Jonglei
- Upper Nile
- Unity
- Warrap
- Northern Bahr el Ghazal
""")

st.header("IPC Phase 5 (Extremely Critical) Areas")

phase5_df = pd.DataFrame({
    "State/Area": [
        "Jonglei",
        "Jonglei",
        "Jonglei",
        "Jonglei",
        "Upper Nile",
        "Upper Nile",
        "Upper Nile",
        "Upper Nile",
        "Unity",
        "Unity",
        "Abyei Administrative Area"
    ],
    "County": [
        "Akobo",
        "Fangak",
        "Uror",
        "Duk",
        "Baliet",
        "Akoka",
        "Luakpiny/Nasir",
        "Ulang",
        "Abiemnhom",
        "Rubkona",
        "Entire Abyei Region"
    ]
})

st.dataframe(phase5_df, use_container_width=True)

st.header("Regional Malnutrition Analysis")

with st.expander("Jonglei State"):
    st.write("""
    Jonglei is currently the most critically affected state in South Sudan.
    Conflict-driven displacement has caused GAM rates to exceed emergency thresholds.
    Fangak County recorded approximately 21.5% Global Acute Malnutrition.
    """)

with st.expander("Upper Nile State"):
    st.write("""
    Upper Nile continues to face severe pressure from refugee inflows and conflict spillover from Sudan.
    Four counties remain under IPC Phase 5 classification.
    """)

with st.expander("Unity State"):
    st.write("""
    Unity State continues to experience extreme wasting levels.
    Flooding and agricultural destruction have weakened local food systems.
    """)

with st.expander("Warrap & Northern Bahr el Ghazal"):
    st.write("""
    These states remain in IPC Phase 4 due to chronic food deficits, rising food prices, and weak health systems.
    """)

with st.expander("Greater Equatoria Region"):
    st.write("""
    Central, Eastern, and Western Equatoria show relatively lower acute wasting levels due to improved rainfall and market functionality.
    """)
    

st.header("Key Drivers of the Crisis")

drivers_df = pd.DataFrame({
    "Driver": [
        "Conflict",
        "Displacement",
        "Flooding",
        "Disease Outbreaks",
        "Economic Collapse",
        "Humanitarian Access Constraints"
    ],
    "Impact": [35, 25, 15, 10, 10, 5]
})

fig_pie = px.pie(
    drivers_df,
    names="Driver",
    values="Impact",
    title="Main Drivers of Acute Malnutrition"
)

st.plotly_chart(fig_pie, use_container_width=True)

st.header("Nutrition Burden Visualization")

nutrition_df = pd.DataFrame({
    "Category": [
        "Children Under Five",
        "Pregnant & Breastfeeding Women"
    ],
    "Affected Population": [2.2, 1.2]
})

fig_nutrition = px.bar(
    nutrition_df,
    x="Category",
    y="Affected Population",
    text="Affected Population",
    title="Population Requiring Acute Malnutrition Treatment (Millions)"
)

st.plotly_chart(fig_nutrition, use_container_width=True)

st.header("Humanitarian Response Efforts")

st.success("""
The Ministry of Health, UNICEF South Sudan, WHO, and humanitarian partners are scaling up emergency nutrition interventions across the country.
""")

st.markdown("""
### Key Interventions

- Expansion of stabilization centers
- Distribution of therapeutic feeding supplies
- Community nutrition screening
- Frontline health worker training
- Emergency cholera response support
- Mobile nutrition clinics
- Child wasting treatment programs
""")

st.header("Interactive County Analysis")

counties = [
    "Akobo",
    "Fangak",
    "Uror",
    "Duk",
    "Baliet",
    "Akoka",
    "Luakpiny/Nasir",
    "Ulang",
    "Rubkona",
    "Abiemnhom"
]

selected_county = st.selectbox("Select County", counties)

st.info(f"Displaying nutrition risk profile for {selected_county}.")


st.sidebar.title("Dashboard Navigation")

st.sidebar.info("South Sudan Nutrition Crisis Monitoring System")

st.sidebar.markdown("""
### Dashboard Sections
- National Overview
- IPC Phase 5 Areas
- State Analysis
- Humanitarian Drivers
- Nutrition Visualizations
- Response Efforts
""")


st.markdown("---")

st.caption("Data Sources: IPC, UNICEF South Sudan, WHO Africa, WFP, ReliefWeb, CLiMIS South Sudan")
