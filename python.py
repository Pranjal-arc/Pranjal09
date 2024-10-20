from predictive_model import SalesPredictor

# Initialize the predictor
predictor = SalesPredictor()

# Sample input data
data = {
    "Date": "2023-10-01",
    "Store_ID": 1,
    "Promotion": "Yes",
    "Weather": "Sunny",
    "Holiday": "No"
}

# Get prediction
prediction = predictor.predict(data)
print(f"Predicted Sales: {prediction}")
