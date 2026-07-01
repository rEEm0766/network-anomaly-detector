from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
with open("models/anomaly_model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        packet_size = float(request.form["packet_size"])
        duration = float(request.form["duration"])
        protocol = int(request.form["protocol"])

        data = np.array([[packet_size, duration, protocol]])

        result = model.predict(data)

        if result[0] == -1:
            prediction = "⚠️ Anomaly Detected!"
        else:
            prediction = "✅ Normal Traffic"

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)