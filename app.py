import streamlit as st
import pandas as pd

from prediction import predict_crop_production

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Crop Production Prediction",
    page_icon="🌾",
    layout="wide"
)

# =====================================
# LOAD DATA
# =====================================

@st.cache_data
def load_data():
    return pd.read_csv("Data/Crop_Production_Data.csv")

df = load_data()

# =====================================
# TITLE
# =====================================

st.title("🌾 Crop Production Prediction System")

st.markdown(
    """
    Predict crop production using historical rainfall
    and agricultural data.
    """
)

# =====================================
# INPUTS
# =====================================

state = st.selectbox(
    "Select State",
    sorted(df['State'].unique())
)

districts = sorted(
    df[df['State'] == state]['District_Name'].unique()
)

district = st.selectbox(
    "Select District",
    districts
)

season = st.selectbox(
    "Select Season",
    sorted(df['Season'].unique())
)

# Optional: Filter crops based on state
crops = sorted(
    df[df['State'] == state]['Crop'].unique()
)

crop = st.selectbox(
    "Select Crop",
    crops
)

year = st.number_input(
    "Enter Year",
    min_value=2025,
    max_value=2050,
    value=2028
)

area = st.number_input(
    "Enter Area (Hectares)",
    min_value=1.0,
    value=1000.0,
    step=100.0
)

# =====================================
# PREDICTION
# =====================================

if st.button("Predict Production"):

    try:

        prediction = predict_crop_production(
            state=state,
            district=district,
            year=year,
            season=season,
            crop=crop,
            area=area
        )

        st.success("Prediction Generated Successfully ✅")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Predicted Production",
                f"{prediction:,.2f}"
            )

        with col2:
            st.metric(
                "Production Per Hectare",
                f"{prediction/area:.2f}"
            )

    except Exception as e:
        st.error(f"Error: {e}")