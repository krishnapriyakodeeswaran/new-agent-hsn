import requests

BASE_URL = "http://127.0.0.1:5000"

# Test HSN Validation
def test_validation():
    test_hsn_codes = ["01011010", "999999"]
    for code in test_hsn_codes:
        response = requests.post(f"{BASE_URL}/validate_hsn", json={"HSNCode": code})
        
        # Check if the response is valid before parsing JSON
        if response.status_code == 200:
            print(response.json())  
        else:
            print(f"Error {response.status_code}: {response.text}")  

# Test HSN Suggestion
def test_suggestions():
    test_descriptions = ["Cotton", "Mobile Phones", "Unknown Item"]
    for desc in test_descriptions:
        response = requests.post(f"{BASE_URL}/suggest_hsn", json={"description": desc})
        
        # Check if the response is valid before parsing JSON
        if response.status_code == 200:
            print(response.json())  
        else:
            print(f"Error {response.status_code}: {response.text}")  

if __name__ == "__main__":
    test_validation()
    test_suggestions()
import requests

