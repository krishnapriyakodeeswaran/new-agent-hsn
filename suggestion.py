import pandas as pd
from fuzzywuzzy import process

def suggest_hsn(query, df):
    """Suggests HSN codes based on user query using fuzzy matching."""
    choices = df["Description"].tolist()
    matches = process.extract(query, choices, limit=5)  # Top 5 closest matches

    suggested_codes = []
    for match in matches:
        description = match[0]
        hsn_code = df[df["Description"] == description]["HSNCode"].values[0]
        suggested_codes.append({"HSNCode": hsn_code, "Description": description})

    return suggested_codes


