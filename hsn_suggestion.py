import pandas as pd

# Load dataset
hsn_data = pd.read_excel("HSN_SAC.xlsx", sheet_name="HSN_MSTR")

# Suggestion Logic
def suggest_hsn(description, hsn_data):
    """Suggest relevant HSN codes based on product description."""
    description = description.lower()
    suggestions = hsn_data[hsn_data["Description"].str.contains(description, case=False, na=False)]

    if suggestions.empty:
        return {"message": "No matching HSN codes found."}

    return suggestions[["HSNCode", "Description"]].to_dict(orient="records")
