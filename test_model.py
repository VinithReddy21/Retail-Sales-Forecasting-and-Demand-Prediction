import joblib
import sklearn

print("Scikit-learn:", sklearn.__version__)

model = joblib.load("models/sales_forecast_model.pkl")

print(type(model))
print("Loaded successfully")