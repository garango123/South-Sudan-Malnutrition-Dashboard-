import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="South Sudan Acute Malnutrition Crisis Dashboard (2026)",
    layout="wide"
)

# --------------------------------------------------
# TITLE & INTRODUCTION
# --------------------------------------------------
st.title("South Sudan Acute Malnutrition Crisis Dashboard (2026)")

st.markdown("""
This dashboard provides a comprehensive overview of the 2026 acute malnutrition crisis in South Sudan,
covering all **10 states** and **3 Administrative Areas**.

It includes:
- State and county malnutrition severity  
- IPC Acute Malnutrition classifications  
- Drivers of the nutrition crisis  
- Affected population groups  
- Humanitarian response activities  
- Interactive analytical tools  
""")

st.warning("Note: The numerical data shown here is placeholder data. Replace with official data from IPC, UNICEF, WHO, WFP, CLiMIS, and other verified sources.")

# --------------------------------------------------
# NATIONAL HIGHLIGHTS
# --------------------------------------------------
st.header("🌍 National Nutrition Crisis Overview (2026)")

col1, col2, col3 = st.columns(3)
col1.metric("Children Under 5 Requiring Treatment", "2.2 Million")
col2.metric("Pregnant & Breastfeeding Women (PLW)", "1.2 Million")
col3.metric("People Facing Crisis or Worse (IPC 3+)", "7.8 Million")

# --------------------------------------------------
# STATES & ADMINISTRATIVE AREAS
# --------------------------------------------------
st.header("📌 South Sudan States & Administrative Areas")

states_list = [
    "Jonglei", "Upper Nile", "Unity", "Warrap",
    "Western Bahr el Ghazal", "Northern Bahr el Ghazal", "Lakes",
    "Eastern Equatoria", "Central Equatoria", "Western Equatoria"
]

admin_areas = [
    "Abyei Administrative Area",
    "Greater Pibor Administrative Area",
    "Ruweng Administrative Area"
]

# -----------------------
# Placeholder severity data
# -----------------------
severity_df = pd.DataFrame({
    "Region": states_list + admin_areas,
    "Type": ["State"] * len(states_list) + ["Administrative Area"] * len(admin_areas),
    "Severity Score": [75, 82, 79, 68, 60, 62, 58, 54, 50, 52, 85, 78, 73]  # Placeholder
})

fig_regions = px.bar(
    severity_df,
    x="Region",
    y="Severity Score",
    color="Type",
    title="Malnutrition Severity: States & Administrative Areas",
    text="Severity Score"
)
st.plotly_chart(fig_regions, use_container_width=True)

# --------------------------------------------------
# IPC PHASE 5 EXTREME AREAS
# --------------------------------------------------
st.header("🔥 IPC Phase 5 (Catastrophe / Extremely Critical) Locations")

ipc_df = pd.DataFrame({
    "Region": ["Jonglei", "Jonglei", "Jonglei", "Upper Nile", "Upper Nile",
               "Unity", "Unity", "Abyei Administrative Area"],
    "County": ["Akobo", "Uror", "Fangak", "Ulang", "Nasir",
               "Rubkona", "Abiemnhom", "Abyei Area"]
})

st.dataframe(ipc_df, use_container_width=True)

# --------------------------------------------------
# REGIONAL STATE ANALYSIS EXPANDERS
# --------------------------------------------------
st.header("📊 State-by-State Nutrition Analysis")

for state in states_list + admin_areas:
    with st.expander(f"{state} Analysis"):
        st.write(f"""
        **{state}** continues to experience varying levels of acute malnutrition.
        Replace this section with detailed narrative analysis based on verified IPC or cluster reports.
        """)

# --------------------------------------------------
# DRIVERS OF THE CRISIS
# --------------------------------------------------
st.header("⚠ Key Drivers of the Malnutrition Crisis")

drivers_df = pd.DataFrame({
    "Driver": [
        "Conflict", "Displacement", "Flooding", "Economic Crisis",
        "Disease Outbreaks", "Access Restrictions"
    ],
    "Impact Weight (%)": [30, 25, 15, 10, 12, 8]
})

fig_drivers = px.pie(
    drivers_df,
    names="Driver",
    values="Impact Weight (%)",
    title="Drivers Contributing to Acute Malnutrition"
)

st.plotly_chart(fig_drivers, use_container_width=True)

# --------------------------------------------------
# NUTRITION BURDEN
# --------------------------------------------------
st.header("🧒👩 Nutrition Burden in Vulnerable Populations")

nutrition_df = pd.DataFrame({
    "Group": ["Children Under 5", "Pregnant & Breastfeeding Women"],
    "Population (Millions)": [2.2, 1.2]
})

fig_burden = px.bar(
    nutrition_df,
    x="Group",
    y="Population (Millions)",
    color="Group",
    text="Population (Millions)",
    title="Population Requiring Nutrition Treatment"
)

st.plotly_chart(fig_burden, use_container_width=True)

# --------------------------------------------------
# INTERACTIVE COUNTY ANALYSIS
# --------------------------------------------------
st.header("🔍 Interactive County Analysis")

# -----------------------
# Placeholder counties per region
# -----------------------
county_data = pd.DataFrame({
    "State/Area": ["Jonglei", "Jonglei", "Upper Nile", "Unity", "Unity", "Warrap"],
    "County": ["Akobo", "Fangak", "Ulang", "Rubkona", "Leer", "Tonj North"],
    "GAM (%)": [21.5, 19.8, 17.2, 18.8, 16.3, 14.2],  # placeholder
    "SAM (%)": [5.1, 4.8, 4.2, 4.6, 4.0, 3.2],
    "Food Insecurity (IPC 3+ %)": [78, 82, 70, 75, 72, 65]
})

selected_state = st.selectbox("Select State or Admin Area", sorted(set(county_data["State/Area"])))
filtered = county_data[county_data["State/Area"] == selected_state]

st.subheader(f"County Statistics for {selected_state}")
st.dataframe(filtered, use_container_width=True)

st.subheader("County Malnutrition Visualization")

fig_county = px.bar(
    filtered,
    x="County",
    y="GAM (%)",
    text="GAM (%)",
    title=f"Global Acute Malnutrition Rates in {selected_state}",
    color="County"
)
st.plotly_chart(fig_county, use_container_width=True)

# Histogram
fig_hist = px.histogram(
    filtered,
    x="GAM (%)",
    title=f"GAM Distribution Histogram for {selected_state}"
)
st.plotly_chart(fig_hist, use_container_width=True)

# Scatter (GAM vs Food Insecurity)
fig_scatter = px.scatter(
    filtered,
    x="Food Insecurity (IPC 3+ %) ",
    y="GAM (%)",
    size="GAM (%)",
    title=f"GAM vs Food Insecurity in {selected_state}"
)
st.plotly_chart(fig_scatter, use_container_width=True)

# --------------------------------------------------
# HUMANITARIAN RESPONSE
# --------------------------------------------------
st.header("🚑 Humanitarian Response Activities")

st.success("""
Humanitarian partners and the Ministry of Health are scaling up:
- Stabilization centers  
- Therapeutic feeding programs  
- Community MUAC screening  
- Mobile nutrition clinics  
- Cholera outbreak response  
- WASH-nutrition integrated response  
""")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("---")
st.caption("Data Sources (Insert Verified Values Manually): IPC AMN 2026, UNICEF South Sudan, WHO Africa, WFP FSMS, CLiMIS South Sudan.")
