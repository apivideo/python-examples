# Retrieve a list of all live streams 

import requests

# Retrieve an access token
url = "https://ws.api.video/auth/api-key"

payload = {"apiKey": "your API key here"}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)
response = response.json()
token = response.get("access_token")

# Prepare and send request for a list of all live streams
url = "https://ws.api.video/live-streams"

querystring = {"currentPage":"1","pageSize":"25"}

headers = {
    "Accept": "application/vnd.api.video+json",
    "Content-Type": "application/json",
    "Authorization": token
}

response = requests.request("GET", url, headers=headers, params=querystring)
response = response.json()
print(response)
