



import requests

url = "http://127.0.0.1:8000/process/"

try:
    response = requests.post(url)
    response.raise_for_status()  # Raise an exception for bad status codes
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")