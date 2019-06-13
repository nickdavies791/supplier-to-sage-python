import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('IBAN_API_KEY', '')

## Return IBAN detail for given bank information.
def bank_details(country: str, sort: str, account: str):
    response = requests.get('https://api.iban.com/clients/api/calc-api.php?api_key='+api_key+'&format=json&country='+country+'&bankcode='+sort+'&account='+account)
    if response.ok:
        return json.loads(response.content)
    else:
        return response.raise_for_status