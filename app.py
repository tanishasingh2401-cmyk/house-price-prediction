import joblib
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

model = joblib.load("/kaggle/working/house_price_model.joblib")
feature_columns = model.feature_names_in_.tolist()

@app.route("/")
def home():
    return jsonify({
        "message": "House Price Prediction API is running!"
    })

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        if not isinstance(data, dict):
            return jsonify({"error": "Send house details as JSON"}), 400

        input_data = pd.DataFrame([data])
        input_data = pd.get_dummies(
            input_data, drop_first=True, dtype=int
        )
        input_data = input_data.reindex(
            columns=feature_columns, fill_value=0
        )

        prediction = model.predict(input_data)[0]

        return jsonify({
            "predicted_price": round(float(prediction), 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
