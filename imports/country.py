import requests
import json

## Return country details for the given country.
def country_details(country: str):
    response = requests.get('https://restcountries.eu/rest/v2/name/'+country)
    if response.ok:
        return json.loads(response.content)
    else:
        return response.raise_for_status