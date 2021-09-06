import requests
from requests import HTTPError

for url in ["https://b14esh.com", "https://b14esh.com/xxxxxxxxxxxxxxxxxx"]:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f"Error: {http_err}")
    except Exception as err:
        print(f'Unknown error: {err}')
    else:
        print("Conected Successfully!")