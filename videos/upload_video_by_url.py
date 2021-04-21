# Upload a video from a public URL 

import requests

# Set up variables for endpoints
auth_url = "https://ws.api.video/auth/api-key"
create_url = "https://ws.api.video/videos"

# Set up headers and payload for first authentication request
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

payload = {
    "apiKey": "sandbox or production key here"
}

# Send the first authentication request to get a token. The token can be used for one hour with the rest of the API endpoints.
response = requests.request("POST", auth_url, json=payload, headers=headers)
response = response.json()
token = response.get("access_token")


# Set up headers for bearer authentication
auth_string = "Bearer " + token

headers2 = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": auth_string
}

# Prepare the payload and upload the video
payload = {
    "title": "My Demo Video",
    "source": "https://www.learningcontainer.com/mp4-sample-video-files-download/#Sample_AVI_File"
}
response = requests.request("POST", create_url, json=payload, headers=headers2)

# Check out the response
print(response.json())
