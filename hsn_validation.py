import pandas as pd
from data_loader import load_hsn_sac_data  # ✅ Correct function name


# Load dataset
df_hsn, df_sac = load_hsn_sac_data("HSN_SAC.xlsx")  # ✅ Load both sheets
 # ✅ Only loading HSN data

def is_valid_format(hsn_code):
    """Checks if the HSN code is numeric and has an acceptable length."""
    return hsn_code.isdigit() and len(hsn_code) in [2, 4, 6, 8]

def exists_in_master(hsn_code, df):
    """Verifies if the HSN code exists in the dataset."""
    return hsn_code in df["HSNCode"].astype(str).values

def check_hierarchy(hsn_code, df):
    """Validates if parent codes exist, but allows exceptions."""
    parent_levels = [2, 4, 6]
    missing_parents = []
    
    for length in parent_levels:
        parent_code = hsn_code[:length]
        if parent_code not in df["HSNCode"].astype(str).values:
            missing_parents.append(parent_code)
    
    return {"valid": len(missing_parents) == 0, "missing_parents": missing_parents}

def validate_hsn(hsn_code):
    """Validates an HSN code using the dataset."""
    if not is_valid_format(hsn_code):
        return {"valid": False, "reason": "Invalid format"}

    if not exists_in_master(hsn_code, df_hsn):
        return {"valid": False, "reason": "HSN code not found"}

    hierarchy_check = check_hierarchy(hsn_code, df_hsn)
    if not hierarchy_check["valid"]:
        return {"valid": False, "reason": f"Parent levels missing: {hierarchy_check['missing_parents']}"}

    description = df_hsn[df_hsn["HSNCode"] == hsn_code]["Description"].values[0]
    return {"valid": True, "hsn_code": hsn_code, "description": description}

# Example usage

