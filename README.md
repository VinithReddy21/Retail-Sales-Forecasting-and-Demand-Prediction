Retail Sales Forecasting and Demand Prediction System
Overview

A machine learning-based retail analytics system developed to forecast future sales and product demand using historical retail transaction data.

The project combines data science, machine learning, business intelligence, and interactive deployment to support inventory optimization and strategic business decision-making.

Features
Retail sales forecasting
Demand prediction
Data preprocessing pipeline
Exploratory Data Analysis (EDA)
Feature engineering
Multiple model comparison
Hyperparameter tuning
Feature importance analysis
Interactive Streamlit dashboard
Business insights generation
Dataset
Source

Corporación Favorita Grocery Sales Forecasting Dataset

Dataset Statistics
Metric	Value
Records	3,000,888
Features	6
Size	~125 MB
Time Period	2013–2017
Stores	54
Product Families	33
Technology Stack
Programming
Python
Data Analysis
Pandas
NumPy
Visualization
Matplotlib
Seaborn
Machine Learning
Scikit-learn
Deployment
Streamlit
Machine Learning Workflow
Data Collection
Data Cleaning
Feature Engineering
Exploratory Data Analysis
Model Training
Hyperparameter Optimization
Model Evaluation
Deployment
Models Evaluated
Model	R² Score
Linear Regression	0.168
Decision Tree	0.763
Gradient Boosting	0.651
Random Forest	0.847

Best Model: Random Forest Regressor

Final Performance
Metric	Value
MAE	101.43
RMSE	448.81
R² Score	0.847
Project Structure
Retail-Sales-Forecasting-and-Demand-Prediction/
│
├── dataset/
│   └── train.csv
│
├── notebooks/
│   └── Retail_Sales_Forecasting.ipynb
│
├── models/
│   ├── sales_forecast_model.pkl
│   ├── label_encoder.pkl
│   └── sample_predictions.csv
│
├── screenshots/
│   ├── architecture_diagram.png
│   ├── prediction_vs_actual.png
│   ├── feature_importance.png
│   ├── comparison.png
│   └── dashboard.png
│
├── app.py
├── requirements.txt
└── README.md
Future Enhancements
XGBoost implementation
LightGBM implementation
Deep Learning forecasting
Real-time forecasting API
Cloud deployment using Azure
Automated business reporting






Four machine learning models were evaluated for sales forecasting.

Linear Regression achieved an R² score of 0.168, indicating poor performance due to the non-linear nature of retail sales data.

Decision Tree improved performance with an R² score of 0.763 by capturing decision-based patterns.

Gradient Boosting achieved an R² score of 0.651.

Random Forest achieved the highest R² score of 0.847 and was selected as the final model due to its superior predictive performance and robustness.


Business Insights
Sales Trend Analysis
Sales exhibited a consistent upward trend from 2013 to 2017.
Seasonal demand fluctuations were observed across multiple product categories.
Promotional campaigns significantly influenced sales performance.
Key Drivers of Sales

Based on feature importance analysis:

Feature importance

Relative contribution of features in the Random Forest model.

Business Recommendations
Increase inventory allocation for high-performing product families.
Optimize promotional campaigns during peak demand periods.
Use demand forecasting to reduce inventory holding costs.
Improve stock planning and replenishment strategies.


## Dataset

The original dataset is not included in this repository due to GitHub file size limits.
link to the dataset , download train.csv
https://www.kaggle.com/competitions/store-sales-time-series-forecasting/data?utm_source=chatgpt.com&select=train.csv
Place the dataset at:
dataset/train.csv

## Model

The trained model file is not included.
Run the notebook to retrain and generate:
models/sales_forecast_model.pkl
