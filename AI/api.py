from flask import Flask, request, jsonify
from model import recommend_properties
import pandas as pd

# Load the dataset
data = pd.read_csv("property_data.csv")

app = Flask(__name__)

# Route for recommendations
@app.route("/recommend", methods=["POST"])
def recommend():
    request_data = request.json
    property_id = request_data.get("property_id", None)
    if property_id is None:
        return jsonify({"error": "Property ID not provided"}), 400

    try:
        recommendations = recommend_properties(property_id)
        return recommendations.to_json(orient="records"), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
