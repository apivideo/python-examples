import requests

# Retrieve access token
url = "https://ws.api.video/auth/api-key"

payload = {"apiKey": "your API key here"}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)
response = response.json()
token = response.get("access_token")

# Add the live stream ID for the live stream you want to add a thumbnail to
live = "livestreamID"

# Open the image you want to set as the thumbnail 
files = { 
    'file': ("image1.jpg", open("image1.jpg", "rb"))
}

# Prepare and send the request that sets the thumbnail
url = "https://ws.api.video/live-streams/" + live + "/thumbnail"

headers = {
    "Accept": "application/json",
    "Authorization": token
}

response = requests.request("POST", url, files=files, headers=headers)

print(response.text)
