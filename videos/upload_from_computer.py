# How to upload a video from your computer that is under 128 MB using the api.video API

import requests

# Set up variables for endpoints (we will create the third URL programmatically later)
auth_url = "https://ws.api.video/auth/api-key"
create_url = "https://ws.api.video/videos"

# Set up headers and payload for first authentication request
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

payload = {
    "apiKey": "your API key here"
}

# Send the first authentication request to get a token. The token can be used for one hour with the rest of the API endpoints.
response = requests.request("POST", auth_url, json=payload, headers=headers)
response = response.json()
token = response.get("access_token")

auth_string = "Bearer " + token


# Set up headers for authentication
headers_bearer = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": auth_string
}

# Create the video container payload, you can add more parameters if you like, check the docs at [https://docs.api.video](https://docs.api.video)
payload2 = {
    "title": "Demo Vid from my Computer",
    "description": "Video upload of Big Buck Bunny to demo how to do an upload from a folder on your computer."
}

# Send the request to create the container, and retrieve the videoId from the response.
response = requests.request("POST", create_url, json=payload2, headers=headers_bearer)
response = response.json()
videoId = response["videoId"]

# Create endpoint to upload your video to - you have to add the videoId into the URL
upload_url = upload_url + "/" + videoId + "/source"

# Create upload video headers 
headers_upload = {
    "Accept": "application/vnd.api.video+json",
    "Authorization": auth_string
}

# Upload the file by specifying a path to it and opening it in binary, then attaching the open file to your request 
file = {"file": open("your-video.flv", "rb")}
response = requests.request("POST", upload_url, files=file, headers=headers_upload)

# Check out the response to see if everything went well!
json_response = response.json()
print(json_response)
