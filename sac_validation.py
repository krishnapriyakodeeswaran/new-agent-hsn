import pandas as pd
from data_loader import load_hsn_sac_data  # ✅ Ensure correct import

# Load dataset
df_hsn, df_sac = load_hsn_sac_data("HSN_SAC.xlsx")  # ✅ Loads both sheets

def is_valid_sac(sac_code):
    """Checks if the SAC code is numeric and has an acceptable length."""
    return sac_code.isdigit() and len(sac_code) in [2, 4, 6]  # ✅ Allows 2-digit, 4-digit, and 6-digit SAC codes

def exists_in_sac_master(sac_code, df):
    """Verifies if the SAC code exists in the dataset."""
    return sac_code in df["SAC_CD"].astype(str).values  # ✅ Uses correct column name

def validate_sac(sac_code):
    """Validates an SAC code using the dataset."""
    if not is_valid_sac(sac_code):
        return {"valid": False, "reason": "Invalid format"}

    matching_rows = df_sac[df_sac["SAC_CD"].astype(str) == sac_code]  # ✅ Ensures correct lookup

    if matching_rows.empty:
        return {"valid": False, "reason": "SAC code not found"}

    description = matching_rows["SAC_Description"].values[0]  # ✅ Use correct column name
    return {"valid": True, "sac_code": sac_code, "description": description}

# Example usage
if __name__ == "__main__":
    try:
        sac_code = input("Enter SAC code to validate: ").strip()  # ✅ Handles user input safely
        result = validate_sac(sac_code)
        print(result)  # ✅ Prints validation result
    except EOFError:
        print("\nEOFError: No input received. Please enter a valid SAC code.")  # ✅ Handles missing input
