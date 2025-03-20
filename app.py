from flask import Flask, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model
with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

@app.route("/get", methods=["GET"])
def get_status():
    return jsonify({"message": "Model is running"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        features = np.array([data["PM2.5"], data["PM10"], data["NO2"], data["CO"], data["SO2"], data["O3"]]).reshape(1, -1)
        prediction = model.predict(features)
        return jsonify({"AQI": float(prediction[0])})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)