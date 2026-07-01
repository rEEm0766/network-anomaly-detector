import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import pickle
import os

# Random sample network data
np.random.seed(42)

data = pd.DataFrame({
    "packet_size": np.random.randint(40, 1500, 1000),
    "duration": np.random.uniform(0.1, 10, 1000),
    "protocol": np.random.randint(0, 3, 1000)
})

# Train Isolation Forest model
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(data)

# Create models folder if it doesn't exist
os.makedirs("models", exist_ok=True)

# Save the trained model
with open("models/anomaly_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved successfully!")