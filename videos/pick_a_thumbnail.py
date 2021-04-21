# Add a thumbnail using a timecode. api.video will set it as your thumbnail for you. 
# You must know the videoId for your video to use this sample. 

import requests 

# Authenticate and get access token
url = "https://ws.api.video/auth/api-key"

payload = {"apiKey": "your api key here"}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)
response = response.json()
token = response.get("access_token")

# Add the videoId for the video you want to add a thumbnail to into the URL 
# where it says VIDEOIDHERE. 

url = "https://ws.api.video/videos/VIDEOIDHERE/thumbnail"

headers = {
    "Accept": "application/vnd.api.video+json",
    "Content-Type": "application/json",
    "Authorization": token
}

# Choose the time in the video you want the image to come from. 

payload = {
    "timecode": "00:00:30:000"
}

response = requests.request("PATCH", url, headers=headers, json=payload)

print(response.text)

# NOTES: If you added a thumbnail by uploading a picture, this will override 
# your picture. 
