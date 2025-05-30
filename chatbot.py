from flask import Flask, request, jsonify
import pandas as pd
from data_loader import load_hsn_sac_data
from hsn_validation import validate_hsn
from sac_validation import validate_sac
from suggestion import suggest_hsn

app = Flask(__name__)

# Load both datasets
df_hsn, df_sac = load_hsn_sac_data("HSN_SAC.xlsx")

@app.route("/chat", methods=["POST"])
def chat():
    """Determines if input is HSN or SAC code and returns validation or suggestions."""
    user_input = request.json.get("message", "").strip()

    if not user_input:
        return jsonify({"response": "Invalid input"}), 400

    if user_input.isdigit():  # Checking if it's HSN or SAC code
        result_hsn = validate_hsn(user_input)
        result_sac = validate_sac(user_input)

        response = (
            result_hsn["description"] if result_hsn["valid"] else 
            (result_sac["description"] if result_sac["valid"] else "Invalid code")
        )
    else:  # Assuming it's a product description for HSN suggestions
        suggestions_hsn = suggest_hsn(user_input, df_hsn)

        response = (
            suggestions_hsn[0]["Description"] if suggestions_hsn else "No match found"
        )

    return jsonify({"response": response})

if __name__ == "__main__":
    while True:
        user_code = input("\nEnter HSN or SAC code (or type 'exit' to quit): ").strip()

        if user_code.lower() == "exit":
            print("Exiting chatbot... 👋")
            break  # ✅ Allows user to exit

        result_hsn = validate_hsn(user_code)
        result_sac = validate_sac(user_code)

        if result_hsn["valid"]:
            print(f"Chatbot Response: {result_hsn}")
        elif result_sac["valid"]:
            print(f"Chatbot Response: {result_sac}")
        else:
            print("Invalid code")
