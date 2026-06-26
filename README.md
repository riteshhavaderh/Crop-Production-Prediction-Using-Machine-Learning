# 🌾 Crop Production Prediction Using Machine Learning and Historical Rainfall Analysis

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-XGBoost-green)
![Streamlit](https://img.shields.io/badge/Deployment-Streamlit-red)
![Status](https://img.shields.io/badge/Status-Deployed-success)

---

## 🔗 Live Application

### 🌐 Streamlit Web Application

https://agricultural-crop-yield-prediction-webapp.streamlit.app/

---

# 📌 Project Overview

Agriculture plays a vital role in India's economy. Accurate crop production prediction helps farmers, agricultural organizations, and policymakers make informed decisions regarding crop planning, resource allocation, and food security.

This project develops a Machine Learning based Crop Production Prediction System using historical agricultural production data combined with historical rainfall data across India.

The model predicts crop production using:

- State
- District
- Season
- Crop
- Area
- Historical rainfall patterns

The final model is deployed using Streamlit.

---

# 🎯 Objectives

- Analyze crop production trends across India.
- Study the impact of rainfall on agricultural production.
- Identify major crop-producing states and crops.
- Develop a machine learning model for crop prediction.
- Deploy the model using Streamlit.

---

# 📊 Dataset Features

| Feature | Description |
|---------|-------------|
| State | State Name |
| District_Name | District Name |
| Year | Production Year |
| Season | Crop Season |
| Crop | Crop Name |
| Area | Area Under Cultivation |
| Production | Crop Production |
| JAN-DEC | Monthly Rainfall |
| ANNUAL | Annual Rainfall |
| JF | Jan-Feb Rainfall |
| MAM | Mar-Apr-May Rainfall |
| JJAS | Jun-Jul-Aug-Sep Rainfall |
| OND | Oct-Nov-Dec Rainfall |

---

# 📈 Exploratory Data Analysis

## Production by State

![Production by State](images/state_production.png)

### Findings

- Bihar recorded the highest crop production.
- Tamil Nadu ranked second.
- Kerala, Punjab, and Chhattisgarh showed moderate production.
- Jharkhand and Arunachal Pradesh had relatively lower production.

---

## Production by Season

![Production by Season](images/season_production.png)

### Findings

- Whole Year crops contributed the highest production.
- Kharif season ranked second.
- Rabi season ranked third.
- Summer and Autumn contributed less.

---

## Top Crops by Production

![Top Crops](images/top_crops.png)

### Findings

| Rank | Crop |
|------|------|
| 1 | Rice |
| 2 | Maize |
| 3 | Wheat |
| 4 | Sugarcane |
| 5 | Potato |

Rice dominates agricultural production due to extensive cultivation and favorable climatic conditions.

---

## Average Monthly Rainfall

![Monthly Rainfall](images/monthly_rainfall.png)

### Findings

- July receives the maximum rainfall.
- August receives the second highest rainfall.
- June and September also contribute significantly.
- Winter months receive minimal rainfall.

---

## Average Seasonal Rainfall

![Seasonal Rainfall](images/seasonal_rainfall.png)

### Findings

Seasonal rainfall contribution:

1. JJAS (Highest)
2. OND
3. MAM
4. JF

The monsoon season contributes the majority of India's annual rainfall.

---

## Year-wise Annual Rainfall

![Yearly Rainfall](images/yearly_rainfall.png)

### Findings

- Rainfall varies significantly across years.
- Peak rainfall occurred around 2007.
- Lowest rainfall occurred around 2002 and 2009.

---

## Correlation Heatmap

![Correlation Heatmap](images/correlation_heatmap.png)

### Findings

- Strong correlations exist among rainfall variables.
- Seasonal rainfall strongly influences annual rainfall.
- Area has a positive relationship with production.
- Monsoon rainfall significantly impacts crop production.

---

# 🤖 Machine Learning Models

The following models were evaluated:

- Linear Regression
- Ridge Regression
- Lasso Regression
- Random Forest Regressor
- XGBoost Regressor

---

# 🏆 Final Model: XGBoost Regressor

### Model Parameters

```python
XGBRegressor(
    n_estimators=300,
    learning_rate=0.1,
    max_depth=8,
    random_state=42
)
```

---

# 📊 Model Performance

| Metric | Score |
|--------|--------|
| Train R² | 0.9398 |
| Test R² | 0.9122 |
| MAE | 751.13 |

### Interpretation

✅ Excellent predictive performance

✅ No significant overfitting

✅ Strong generalization capability

---

## Feature Importance

![Feature Importance](images/feature_importance.png)

### Most Important Features

| Rank | Feature |
|------|---------|
| 1 | Area |
| 2 | Season |
| 3 | Crop |
| 4 | State |
| 5 | Rainfall Features |

Area under cultivation emerged as the most important predictor of crop production.

---

# 🌐 Streamlit Application

The application predicts crop production using:

- State
- District
- Season
- Crop
- Year
- Area

Historical rainfall is automatically retrieved and used for prediction.

### Web Application Screenshot

![Web App](images/webapp.png)

---

# 🛠️ Technologies Used

### Programming
- Python

### Data Analysis
- Pandas
- NumPy

### Visualization
- Matplotlib
- Seaborn

### Machine Learning
- Scikit-Learn
- XGBoost

### Deployment
- Streamlit

### Serialization
- Joblib

---

# 📁 Project Structure

```
Crop Production Prediction/
│
├── Data/
│   └── Crop_Production_Data.csv
│
├── Models/
│   ├── crop_production_model.pkl
│   └── label_encoders.pkl
│
├── images/
│
├── app.py
├── prediction.py
├── crop_production.ipynb
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🚀 Run Locally

```bash
git clone https://github.com/riteshhavaderh/Crop-Production-Prediction-Using-Machine-Learning.git

pip install -r requirements.txt

streamlit run app.py
```

---

# 🔮 Future Enhancements

- Weather API integration
- Crop recommendation system
- Fertilizer recommendation
- Soil analysis integration
- FastAPI backend deployment
- Deep learning models

---

# 👨‍💻 Author

**Ritesh Havade**

Master's in Statistics | Data Analyst | Data Scientist | Machine Learning Enthusiast

---

⭐ If you found this project useful, consider giving it a star.