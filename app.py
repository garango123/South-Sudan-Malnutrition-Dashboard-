import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================
st.set_page_config(
    page_title="South Sudan Acute Malnutrition Dashboard",
    page_icon="🇸🇸",
    layout="wide"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================
st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

h1, h2, h3 {
    color: #0b3d91;
}

[data-testid="metric-container"] {
    background-color: white;
    border-radius: 15px;
    padding: 20px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    border-left: 5px solid #0b3d91;
}

section[data-testid="stSidebar"] {
    background-color: #0b3d91;
}

section[data-testid="stSidebar"] * {
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# TITLE
# ==========================================================
st.title("🇸🇸 South Sudan Acute Malnutrition Crisis Dashboard (2026)")

st.markdown("""
This dashboard provides a national overview of the acute malnutrition situation
across South Sudan's 10 states and 3 Administrative Areas.

### Dashboard Features
- Nutrition severity analysis
- IPC classification monitoring
- County-level GAM & SAM analysis
- Interactive charts and tables
- Humanitarian response overview
""")


# ==========================================================
# NATIONAL METRICS
# ==========================================================
st.header("🌍 National Nutrition Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Children U5 Needing Treatment",
        "2.2M",
        "+12%"
    )

with col2:
    st.metric(
        "PLW Affected",
        "1.2M",
        "+8%"
    )

with col3:
    st.metric(
        "Population IPC 3+",
        "7.8M",
        "+15%"
    )

with col4:
    st.metric(
        "Critical Counties",
        "32",
        "+5"
    )

# ==========================================================
# REGIONAL DATA
# ==========================================================
states = [
    "Jonglei",
    "Upper Nile",
    "Unity",
    "Warrap",
    "Lakes",
    "Northern Bahr el Ghazal",
    "Western Bahr el Ghazal",
    "Eastern Equatoria",
    "Central Equatoria",
    "Western Equatoria",
    "Abyei Administrative Area",
    "Greater Pibor Administrative Area",
    "Ruweng Administrative Area"
]

severity = [82, 79, 76, 70, 61, 64, 59, 52, 48, 50, 85, 78, 74]

regions_df = pd.DataFrame({
    "Region": states,
    "Severity Score": severity
})

# ==========================================================
# BAR CHART
# ==========================================================
st.header("📊 Regional Malnutrition Severity")

fig_bar = px.bar(
    regions_df,
    x="Region",
    y="Severity Score",
    color="Severity Score",
    text="Severity Score",
    template="plotly_white",
    title="Regional Severity Scores"
)

fig_bar.update_layout(
    xaxis_tickangle=-30,
    height=500
)

st.plotly_chart(fig_bar, use_container_width=True)

# ==========================================================
# PIE CHART
# ==========================================================
st.header("⚠️ Drivers of Acute Malnutrition")

drivers_df = pd.DataFrame({
    "Driver": [
        "Conflict",
        "Flooding",
        "Displacement",
        "Disease",
        "Economic Crisis",
        "Access Constraints"
    ],
    "Percentage": [30, 20, 18, 12, 10, 10]
})

fig_pie = px.pie(
    drivers_df,
    names="Driver",
    values="Percentage",
    hole=0.4,
    title="Main Drivers of Nutrition Crisis"
)

st.plotly_chart(fig_pie, use_container_width=True)

# ==========================================================
# COUNTY DATA
# ==========================================================
county_df = pd.DataFrame({
    "State": [
        "Jonglei",
        "Jonglei",
        "Upper Nile",
        "Unity",
        "Unity",
        "Warrap",
        "Lakes"
    ],
    "County": [
        "Akobo",
        "Fangak",
        "Nasir",
        "Leer",
        "Rubkona",
        "Tonj North",
        "Rumbek East"
    ],
    "GAM (%)": [21.5, 20.2, 18.6, 17.8, 19.1, 14.5, 13.8],
    "SAM (%)": [5.2, 4.9, 4.5, 4.1, 4.8, 3.0, 2.8],
    "Food Insecurity (%)": [82, 80, 76, 72, 75, 65, 60]
})

# ==========================================================
# DATA TABLE
# ==========================================================
st.header("📋 County Nutrition Statistics")

st.dataframe(
    county_df,
    use_container_width=True
)

# ==========================================================
# SELECT BOX
# ==========================================================
selected_state = st.selectbox(
    "Select State",
    county_df["State"].unique()
)

filtered_df = county_df[
    county_df["State"] == selected_state
]

# ==========================================================
# COUNTY BAR CHART
# ==========================================================
st.subheader(f"GAM Rates — {selected_state}")

fig_gam = px.bar(
    filtered_df,
    x="County",
    y="GAM (%)",
    text="GAM (%)",
    color="County",
    template="plotly_white"
)

st.plotly_chart(fig_gam, use_container_width=True)

# ==========================================================
# HISTOGRAM
# ==========================================================
st.subheader("📈 GAM Distribution Histogram")

fig_hist = px.histogram(
    county_df,
    x="GAM (%)",
    nbins=10,
    color="State",
    template="plotly_white"
)

st.plotly_chart(fig_hist, use_container_width=True)

# ==========================================================
# SCATTER PLOT
# ==========================================================
st.subheader(" GAM vs Food Insecurity")

fig_scatter = px.scatter(
    county_df,
    x="Food Insecurity (%)",
    y="GAM (%)",
    size="SAM (%)",
    color="State",
    hover_name="County",
    template="plotly_white"
)

st.plotly_chart(fig_scatter, use_container_width=True)

# ==========================================================
# LINE CHART
# ==========================================================
st.header("📉 Monthly Nutrition Trend")

trend_df = pd.DataFrame({
    "Month": [
        "Jan", "Feb", "Mar", "Apr",
        "May", "Jun", "Jul", "Aug",
        "Sep", "Oct", "Nov", "Dec"
    ],
    "Cases": [
        120, 150, 170, 200,
        220, 260, 280, 300,
        320, 340, 360, 390
    ]
})

fig_line = px.line(
    trend_df,
    x="Month",
    y="Cases",
    markers=True,
    title="Monthly Acute Malnutrition Trend",
    template="plotly_white"
)

st.plotly_chart(fig_line, use_container_width=True)

# ==========================================================
# IPC PHASE 5 TABLE
# ==========================================================
st.header(" IPC Phase 5 Areas")

ipc_df = pd.DataFrame({
    "Region": [
        "Jonglei",
        "Jonglei",
        "Upper Nile",
        "Unity",
        "Abyei Area"
    ],
    "County": [
        "Akobo",
        "Fangak",
        "Nasir",
        "Leer",
        "Abyei"
    ],
    "Classification": [
        "Catastrophe",
        "Extremely Critical",
        "Catastrophe",
        "Critical",
        "Critical"
    ]
})

st.dataframe(ipc_df, use_container_width=True)

# ==========================================================
# HUMANITARIAN RESPONSE
# ==========================================================
st.header(" Humanitarian Response")

response_df = pd.DataFrame({
    "Program": [
        "Therapeutic Feeding",
        "Mobile Clinics",
        "MUAC Screening",
        "WASH Support",
        "Vaccination"
    ],
    "Coverage (%)": [78, 60, 85, 55, 70]
})

fig_response = px.bar(
    response_df,
    x="Program",
    y="Coverage (%)",
    text="Coverage (%)",
    color="Program",
    template="plotly_white",
    title="Response Coverage"
)

st.plotly_chart(fig_response, use_container_width=True)

# ==========================================================
# GAUGE CHART
# ==========================================================
st.header(" National Severity Gauge")

fig_gauge = go.Figure(go.Indicator(
    mode="gauge+number",
    value=78,
    title={'text': "National Severity Index"},
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

fig_gauge.update_layout(height=400)

st.plotly_chart(fig_gauge, use_container_width=True)

# ==========================================================
# STATE ANALYSIS
# ==========================================================
st.header(" State-by-State Analysis")

for state in states:
    with st.expander(f"{state} Analysis"):
        st.write(f"""
        {state} continues to experience acute malnutrition challenges due to:
        - Food insecurity
        - Conflict and displacement
        - Disease outbreaks
        - Flooding
        - Limited health service access

        
        """)

# ==========================================================
# FOOTER
# ==========================================================
st.markdown("---")

st.caption("""
Data Sources:
IPC Acute Malnutrition Analysis 2026 | UNICEF South Sudan |
WHO Africa | WFP FSMS | CLiMIS | Nutrition Cluster
""")
