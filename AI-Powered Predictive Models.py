from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Sample dataset
data = {
    "vehicle_count": [10, 20, 30, 40, 50],
    "average_speed": [60, 50, 40, 30, 20],
    "congestion": [0, 0, 1, 1, 1]  # 0: No congestion, 1: Congestion
}

df = pd.DataFrame(data)
X = df[["vehicle_count", "average_speed"]]
y = df["congestion"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model training
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predicting congestion for new data
new_data = [[25, 45]]  # Example input
prediction = model.predict(new_data)
print("Congestion Prediction:", "Congested" if prediction[0] else "Not Congested")
