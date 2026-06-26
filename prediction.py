# =========================================================
# LOAD REQUIRED LIBRARIES
# =========================================================

import pandas as pd
import joblib

# =========================================================
# LOAD SAVED FILES
# =========================================================

model = joblib.load('Models/crop_production_model.pkl')

encoder = joblib.load('Models/label_encoders.pkl')


# Load rainfall dataset
rainfall = pd.read_csv("Data/Crop_Production_Data.csv")
rainfall['State'].unique()

# =========================================================
# Get Recent Rainfall Average
# =========================================================
def get_recent_avg_rainfall(state):

    state_data = rainfall[
        rainfall['State'] == state
    ].sort_values('Year')

    if state_data.empty:
        raise ValueError(
            f"State '{state}' not found in rainfall dataset"
        )

    rainfall_cols = [
        'JAN','FEB','MAR','APR','MAY','JUN',
        'JUL','AUG','SEP','OCT','NOV','DEC',
        'ANNUAL','JF','MAM','JJAS','OND'
    ]

    return (
        state_data
        .tail(5)[rainfall_cols]
        .mean()
    )
    
# =========================================================
# Prediction Function
# =========================================================
def predict_crop_production(
        state,
        district,
        year,
        season,
        crop,
        area):

    rain = get_recent_avg_rainfall(state)

    input_df = pd.DataFrame([{

        'State': state,
        'District_Name': district,
        'Year': year,
        'Season': season,
        'Crop': crop,
        'Area': area,

        'JAN': rain['JAN'],
        'FEB': rain['FEB'],
        'MAR': rain['MAR'],
        'APR': rain['APR'],
        'MAY': rain['MAY'],
        'JUN': rain['JUN'],
        'JUL': rain['JUL'],
        'AUG': rain['AUG'],
        'SEP': rain['SEP'],
        'OCT': rain['OCT'],
        'NOV': rain['NOV'],
        'DEC': rain['DEC'],

        'ANNUAL': rain['ANNUAL'],
        'JF': rain['JF'],
        'MAM': rain['MAM'],
        'JJAS': rain['JJAS'],
        'OND': rain['OND']

    }])

    # Encoding
    cat_cols = [
        'State',
        'District_Name',
        'Season',
        'Crop'
    ]

    for col in cat_cols:
        input_df[col] = encoder[col].transform(
            input_df[col]
        )

    # Prediction
    prediction = model.predict(
        input_df
    )[0]

    return prediction


# =========================================================
# Example
# =========================================================

pred = predict_crop_production(
    state='Tamil Nadu',
    district='THIRUVALLUR',
    year=2028,
    season='Kharif',
    crop='Rice',
    area=5000
)

print("Predicted Production:", pred)