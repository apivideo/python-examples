import requests
# Get the status of a video (whether the video is uploaded and available) with this request. 
# You can use this to poll periodically to see if the status has changed. If you'd prefer to use 
# webhooks see the webhooks section of the api.video documentation. 

# Set up authentication URL and variables 
auth_url = "https://ws.api.video/auth/api-key"
api_key = "your api key here"
video_id = "your video ID here"

# Set up headers and payload for first authentication request
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

payload = {
    "apiKey": api_key
}

# Send the first authentication request to get a token. The token can be used for one hour with the rest of the API endpoints.
response = requests.request("POST", auth_url, json=payload, headers=headers)
response = response.json()
token = response.get("access_token")

# Set up headers for authentication - the rest of the endpoints use Bearer authentication.

auth_string = "Bearer " + token

headers2 = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": auth_string
}

# Build the URL you'll send to in order to check the status of your video. 
status_url = "https://ws.api.video/videos/" + video_id + "/status"

# Send the request to get the status of your video
response = requests.request("GET", status_url, headers=headers2)
response = response.json()
print(response)
