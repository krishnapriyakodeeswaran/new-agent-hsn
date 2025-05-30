from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load dataset
hsn_data = pd.read_excel("HSN_SAC.xlsx", sheet_name="HSN_MSTR")
hsn_data.columns = hsn_data.columns.str.strip()

# Validation Functions
def validate_hsn_format(hsn_code):
    return hsn_code.isdigit() and len(hsn_code) in [2, 4, 6, 8]

def validate_hsn_existence(hsn_code):
    return hsn_code in hsn_data["HSNCode"].astype(str).values

def validate_hsn_hierarchy(hsn_code):
    """Check if parent levels exist for the given HSN code."""
    levels = [hsn_code[:i] for i in [2, 4, 6, 8] if i <= len(hsn_code)]
    missing_levels = [level for level in levels if level not in hsn_data["HSNCode"].astype(str).values]

    # Debugging output
    print(f"Checking hierarchy for {hsn_code}: Missing parent levels -> {missing_levels}")

    return not missing_levels  # Returns True if all parent levels exist, otherwise False


def suggest_hsn(description):
    description = description.lower()
    suggestions = hsn_data[hsn_data["Description"].str.contains(description, case=False, na=False)]
    return suggestions[["HSNCode", "Description"]].to_dict(orient="records")

# API Endpoints
@app.route("/validate", methods=["GET"])
def validate():
    hsn_code = request.args.get("hsn_code")
    
    if not validate_hsn_format(hsn_code):
        return jsonify({"status": "Invalid format", "message": "HSN Code must be numeric and 2, 4, 6, or 8 digits."})
    
    if not validate_hsn_existence(hsn_code):
        return jsonify({"status": "Invalid code", "message": "HSN Code not found in dataset."})
    
    if not validate_hsn_hierarchy(hsn_code):
        return jsonify({"status": "Warning", "message": "Parent levels missing, validation incomplete."})
    
    return jsonify({"status": "Valid HSN Code", "hsn_code": hsn_code})

@app.route("/suggest", methods=["GET"])
def suggest():
    description = request.args.get("description")
    results = suggest_hsn(description)
    
    if not results:
        return jsonify({"status": "No matches", "message": "No relevant HSN codes found for the given description."})
    
    return jsonify({"status": "Success", "results": results})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
