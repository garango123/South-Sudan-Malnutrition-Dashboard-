import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="South Sudan Acute Malnutrition Crisis Dashboard (2026)",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM STYLING
# =========================================================
st.markdown("""
<style>
/* Main background */
.stApp {
    background-color: #0f172a;
    color: white;
}

/* Headers */
h1, h2, h3, h4 {
    color: #f8fafc !important;
}

/* Metric cards */
[data-testid="metric-container"] {
    background: linear-gradient(135deg, #1e293b, #334155);
    border: 1px solid #475569;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
}

/* Tables */
[data-testid="stDataFrame"] {
    background-color: white;
    border-radius: 10px;
}

/* Expander */
.streamlit-expanderHeader {
    background-color: #1e293b;
    color: white !important;
    border-radius: 8px;
}

/* Buttons */
.stButton>button {
    background-color: #2563eb;
    color: white;
    border-radius: 8px;
    border: none;
    padding: 0.5rem 1rem;
}

.stButton>button:hover {
    background-color: #1d4ed8;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# TITLE
# =========================================================
st.title("🇸🇸 South Sudan Acute Malnutrition Crisis Dashboard (2026)")

st.markdown("""
### National Nutrition Situation Overview

This dashboard provides a comprehensive overview of the **2026 acute malnutrition crisis**
across all **10 states** and **3 Administrative Areas** of South Sudan.

#### Dashboard Includes:
- Acute malnutrition severity analysis
- IPC classification monitoring
- County-level GAM and SAM indicators
- Crisis drivers and vulnerabilities
- Humanitarian response tracking
- Interactive visual analytics

""")

st.warning(
    "⚠️ Placeholder data is currently used. Replace with verified datasets "
    "from IPC, UNICEF, WHO, WFP, FSNMS, and CLiMIS."
)

# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.title("📌 Dashboard Navigation")

menu = st.sidebar.radio(
    "Select Dashboard Section",
    [
        "National Overview",
        "Regional Severity",
        "IPC Phase 5 Areas",
        "County Analysis",
        "Crisis Drivers",
        "Humanitarian Response"
    ]
)

# =========================================================
# DATA
# =========================================================

states_list = [
    "Jonglei",
    "Upper Nile",
    "Unity",
    "Warrap",
    "Western Bahr el Ghazal",
    "Northern Bahr el Ghazal",
    "Lakes",
    "Eastern Equatoria",
    "Central Equatoria",
    "Western Equatoria"
]

admin_areas = [
    "Abyei Administrative Area",
    "Greater Pibor Administrative Area",
    "Ruweng Administrative Area"
]

severity_df = pd.DataFrame({
    "Region": states_list + admin_areas,
    "Type": ["State"] * len(states_list) + ["Administrative Area"] * len(admin_areas),
    "Severity Score": [75, 82, 79, 68, 60, 62, 58, 54, 50, 52, 85, 78, 73]
})

ipc_df = pd.DataFrame({
    "Region": [
        "Jonglei",
        "Jonglei",
        "Jonglei",
        "Upper Nile",
        "Upper Nile",
        "Unity",
        "Unity",
        "Abyei Administrative Area"
    ],
    "County": [
        "Akobo",
        "Uror",
        "Fangak",
        "Ulang",
        "Nasir",
        "Rubkona",
        "Abiemnhom",
        "Abyei Area"
    ]
})

county_data = pd.DataFrame({
    "State/Area": [
        "Jonglei",
        "Jonglei",
        "Upper Nile",
        "Unity",
        "Unity",
        "Warrap"
    ],
    "County": [
        "Akobo",
        "Fangak",
        "Ulang",
        "Rubkona",
        "Leer",
        "Tonj North"
    ],
    "GAM (%)": [21.5, 19.8, 17.2, 18.8, 16.3, 14.2],
    "SAM (%)": [5.1, 4.8, 4.2, 4.6, 4.0, 3.2],
    "Food Insecurity (%)": [78, 82, 70, 75, 72, 65]
})

drivers_df = pd.DataFrame({
    "Driver": [
        "Conflict",
        "Displacement",
        "Flooding",
        "Economic Crisis",
        "Disease Outbreaks",
        "Access Restrictions"
    ],
    "Impact Weight (%)": [30, 25, 15, 10, 12, 8]
})

nutrition_df = pd.DataFrame({
    "Group": [
        "Children Under 5",
        "Pregnant & Breastfeeding Women"
    ],
    "Population (Millions)": [2.2, 1.2]
})

# =========================================================
# NATIONAL OVERVIEW
# =========================================================
if menu == "National Overview":

    st.header("🌍 National Nutrition Crisis Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Children Under 5 Requiring Treatment",
        "2.2 Million"
    )

    col2.metric(
        "Pregnant & Breastfeeding Women",
        "1.2 Million"
    )

    col3.metric(
        "Population Facing IPC 3+",
        "7.8 Million"
    )

    st.markdown("---")

    fig = go.Figure()

    fig.add_trace(go.Indicator(
        mode="gauge+number",
        value=78,
        title={'text': "National Nutrition Severity Index"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "red"},
            'steps': [
                {'range': [0, 40], 'color': "green"},
                {'range': [40, 70], 'color': "orange"},
                {'range': [70, 100], 'color': "darkred"}
            ]
        }
    ))

    fig.update_layout(
        paper_bgcolor="#0f172a",
        font={"color": "white"}
    )

    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# REGIONAL SEVERITY
# =========================================================
elif menu == "Regional Severity":

    st.header("📊 Regional Malnutrition Severity")

    fig_regions = px.bar(
        severity_df,
        x="Region",
        y="Severity Score",
        color="Type",
        text="Severity Score",
        template="plotly_dark",
        title="Malnutrition Severity Across South Sudan"
    )

    fig_regions.update_layout(
        xaxis_tickangle=-30
    )

    st.plotly_chart(fig_regions, use_container_width=True)

    st.subheader("Regional Data Table")
    st.dataframe(severity_df, use_container_width=True)

# =========================================================
# IPC PHASE 5
# =========================================================
elif menu == "IPC Phase 5 Areas":

    st.header("🔥 IPC Phase 5 Locations")

    st.error(
        "The following locations are categorized as "
        "Catastrophe / Extremely Critical."
    )

    st.dataframe(ipc_df, use_container_width=True)

    fig_ipc = px.histogram(
        ipc_df,
        x="Region",
        color="Region",
        template="plotly_dark",
        title="Distribution of IPC Phase 5 Counties"
    )

    st.plotly_chart(fig_ipc, use_container_width=True)

# =========================================================
# COUNTY ANALYSIS
# =========================================================
elif menu == "County Analysis":

    st.header("🔍 Interactive County Analysis")

    selected_state = st.selectbox(
        "Select State or Administrative Area",
        sorted(county_data["State/Area"].unique())
    )

    filtered = county_data[
        county_data["State/Area"] == selected_state
    ]

    st.subheader(f"County Statistics — {selected_state}")

    st.dataframe(filtered, use_container_width=True)

    # GAM Bar Chart
    fig_county = px.bar(
        filtered,
        x="County",
        y="GAM (%)",
        color="County",
        text="GAM (%)",
        template="plotly_dark",
        title=f"GAM Rates in {selected_state}"
    )

    st.plotly_chart(fig_county, use_container_width=True)

    # Histogram
    fig_hist = px.histogram(
        filtered,
        x="GAM (%)",
        nbins=10,
        template="plotly_dark",
        title=f"GAM Distribution in {selected_state}"
    )

    st.plotly_chart(fig_hist, use_container_width=True)

    # Scatter Plot
    fig_scatter = px.scatter(
        filtered,
        x="Food Insecurity (%)",
        y="GAM (%)",
        size="SAM (%)",
        color="County",
        hover_name="County",
        template="plotly_dark",
        title="Food Insecurity vs GAM"
    )

    st.plotly_chart(fig_scatter, use_container_width=True)

# =========================================================
# CRISIS DRIVERS
# =========================================================
elif menu == "Crisis Drivers":

    st.header("⚠️ Drivers of Acute Malnutrition")

    fig_drivers = px.pie(
        drivers_df,
        names="Driver",
        values="Impact Weight (%)",
        hole=0.4,
        template="plotly_dark",
        title="Key Drivers of the Nutrition Crisis"
    )

    st.plotly_chart(fig_drivers, use_container_width=True)

    st.subheader("Nutrition Burden")

    fig_burden = px.bar(
        nutrition_df,
        x="Group",
        y="Population (Millions)",
        color="Group",
        text="Population (Millions)",
        template="plotly_dark",
        title="Affected Population Groups"
    )

    st.plotly_chart(fig_burden, use_container_width=True)

# =========================================================
# HUMANITARIAN RESPONSE
# =========================================================
elif menu == "Humanitarian Response":

    st.header("🚑 Humanitarian Response Activities")

    st.success("""
    Humanitarian partners and the Ministry of Health are scaling up:

    ✅ Stabilization Centers  
    ✅ Therapeutic Feeding Programs  
    ✅ Community MUAC Screening  
    ✅ Mobile Nutrition Clinics  
    ✅ Cholera Response Activities  
    ✅ WASH-Nutrition Integrated Response  
    """)

    response_df = pd.DataFrame({
        "Intervention": [
            "Therapeutic Feeding",
            "Mobile Clinics",
            "MUAC Screening",
            "WASH Support",
            "Disease Response"
        ],
        "Coverage (%)": [72, 55, 80, 60, 68]
    })

    fig_response = px.bar(
        response_df,
        x="Intervention",
        y="Coverage (%)",
        color="Intervention",
        text="Coverage (%)",
        template="plotly_dark",
        title="Humanitarian Response Coverage"
    )

    st.plotly_chart(fig_response, use_container_width=True)

# =========================================================
# STATE EXPANDERS
# =========================================================
st.markdown("---")
st.header("📌 State-by-State Narrative Analysis")

for state in states_list + admin_areas:
    with st.expander(f"{state} Analysis"):
        st.write(f"""
        **{state}** continues to experience varying levels of acute malnutrition,
        driven by food insecurity, displacement, disease outbreaks, flooding,
        and limited access to health services.

        Replace this section with verified IPC or Nutrition Cluster analysis.
        """)

# =========================================================
# FOOTER
# =========================================================
st.markdown("---")

st.caption("""
Data Sources:
IPC AMN 2026 | UNICEF South Sudan | WHO Africa | WFP FSMS |
CLiMIS South Sudan | Nutrition Cluster Reports
""")
