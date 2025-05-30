import pandas as pd
from data_loader import load_hsn_data
from hsn_validation import validate_hsn
from suggestion import suggest_hsn

def process_user_input(user_input, df):
    """Determines if input is an HSN code or product description, then responds."""
    if user_input.isdigit():  # Check if input is numeric (HSN Code Validation)
        result = validate_hsn(user_input, df)
        return result
    else:  # Otherwise, assume it's a product description (Suggestion Logic)
        suggestions = suggest_hsn(user_input, df)
        return {"suggestions": suggestions}

# Example usage
if __name__ == "__main__":
    df = load_hsn_data()
    
    user_input = input("Enter HSN code or product description: ")
    response = process_user_input(user_input, df)
    
    print("\nAgent Response:")
    print(response)
