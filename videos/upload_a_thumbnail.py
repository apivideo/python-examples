# Upload a thumbnail for a video.
# Your video must already be uploaded to api.video for this to work. 

import requests 

# Get api.video token 

url = "https://ws.api.video/auth/api-key"

payload = {"apiKey": "your API key here"}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)
response = response.json()
token = response.get("access_token")

# Add the video ID you want to send a thumbnail to 

vid = "video ID here"

url = "https://ws.api.video/videos/" + vid + "/thumbnail"

headers = {
    "Accept": "application/vnd.api.video+json",
    "Authorization": token
}

# Add your file to use as a thumbnail 

file = {"file": open("THUMBNAIL.jpg", "rb")}

response = requests.request("POST", url, files=file, headers=headers)
print(response.json())
