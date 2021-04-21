import requests

# Retrieve an access token using your API credentials
url = "https://ws.api.video/auth/api-key"

payload = {"apiKey": "api key here"}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)
response = response.json()
token = response.get("access_token")

# Endpoint for live streaming
url = "https://ws.api.video/live-streams"

# Payload for live streaming, whether you will record the live stream for playback and the live stream name
payload = {
    "record": False,
    "name": "Bob"
}

# Headers for live streaming
headers = {
    "Accept": "application/vnd.api.video+json",
    "Content-Type": "application/json",
    "Authorization": token
}

response = requests.request("POST", url, json=payload, headers=headers)
