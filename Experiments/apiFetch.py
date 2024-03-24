import requests
from SecretsToo import auth

url = "https://api.themoviedb.org/3/authentication"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {auth}"
}

response = requests.get(url, headers=headers, verify=False)

print(response.text)