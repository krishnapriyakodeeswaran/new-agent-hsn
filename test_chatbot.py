import requests

url = "http://127.0.0.1:5000/chat"
data = {"message": "9987"}  # Example SAC Code
response = requests.post(url, json=data)

print("Chatbot Response:", response.json()["response"])  # Should return SAC description
