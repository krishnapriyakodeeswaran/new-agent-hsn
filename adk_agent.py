from flask import Flask, request, jsonify
from hsn_validation import validate_hsn_format, validate_hsn_existence, validate_hsn_hierarchy
from hsn_suggestion import suggest_hsn
import pandas as pd

app = Flask(__name__)

# Load dataset
hsn_data = pd.read_excel("HSN_SAC.xlsx", sheet_name="HSN_MSTR")

@app.route('/validate_hsn', methods=['POST'])
@app.route('/validate_hsn', methods=['POST'])
def validate_hsn():
    data = request.json
    print("Received Data:", data)  # Debugging step

    if not data or "HSNCode" not in data:
        return jsonify({"error": "HSNCode missing"}), 400
    
    hsn_code = data["HSNCode"]
    validation_result = {
        "HSNCode": hsn_code,
        "valid_format": validate_hsn_format(hsn_code),
        "exists": validate_hsn_existence(hsn_code, hsn_data),
        "hierarchy_valid": validate_hsn_hierarchy(hsn_code, hsn_data)
    }
    return jsonify(validation_result)


@app.route('/suggest_hsn', methods=['POST'])
def suggest_hsn_api():
    """Endpoint to suggest HSN codes based on user input."""
    data = request.json
    description = data.get("description")

    suggestions = suggest_hsn(description, hsn_data)

    return jsonify({"query": description, "suggestions": suggestions})

if __name__ == '__main__':
    app.run(debug=True)
print("Dataset Columns:", hsn_data.columns)
