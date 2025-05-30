A Flask-powered chatbot that validates HSN & SAC codes, suggests HSN codes based on product descriptions, and ensures structured GST classification.

🔹 Project Overview
This chatbot:

i)Validates HSN (Harmonized System of Nomenclature) codes and SAC (Services Accounting Code) codes.

ii)Suggests relevant HSN codes based on product descriptions using fuzzy matching (fuzzywuzzy).

iii)Uses Flask API for user interactions and data retrieval.

iv)Loads structured HSN & SAC datasets from an Excel sheet for accurate classification.

 Technology Stack
Python (Core Logic)

Flask (API Framework)

Pandas (Data Handling)

FuzzyWuzzy (HSN Suggestions)

Excel Integration (openpyxl for reading data)

 Folder Structure
📂 new-agent-hsn/
 ├── chatbot.py          # Main chatbot interface (Flask API & Terminal Input)
 ├── data_loader.py      # Loads HSN & SAC data from Excel
 ├── hsn_validation.py   # Validates HSN codes
 ├── sac_validation.py   # Validates SAC codes
 ├── suggestion.py       # Suggests HSN codes for product descriptions
 ├── HSN_SAC.xlsx        # Contains the HSN & SAC datasets
 ├── README.md           # Project documentation
🔹 Installation & Setup
1️) Clone the Repository
bash
git clone https://github.com/your-repository-name.git
cd new-agent-hsn

2️) Install Dependencies
bash
pip install flask pandas fuzzywuzzy openpyxl

3️) Run the Chatbot
bash
python chatbot.py

🔹 Usage
1️) Validating HSN/SAC Codes
bash
Enter HSN or SAC code (or type 'exit' to quit): 010130
✔️ Response:

json
{"valid": True, "hsn_code": "010130", "description": "LIVE HORSES"}
2️) Getting HSN Suggestions Using Fuzzy Matching
bash
Enter product description: Leather Bags
✔️ Response:

json
[{"HSNCode": "4202", "Description": "Leather Travel Bags, Handbags, Wallets"}]
🔹 Key Learnings from the Project
Modular programming with Flask APIs.

Excel integration for structured datasets.

Validations & fuzzy matching for enhanced user experience.

