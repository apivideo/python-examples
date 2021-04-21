# How to do a delegated upload of a video that is under 128 MB to api.video. 
# Delegated uploads are authenticated with a delegated token, which you can customize expiration for.

import requests

# Set up variables for endpoints 
auth_url = "https://ws.api.video/auth/api-key"
token_url = "https://ws.api.video/upload-tokens"
delegated_upload_url = "https://ws.api.video/upload"

# Set up headers and payload for first authentication request
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

payload = {
    "apiKey": "your api key here"
}

# Send the first authentication request to get a token. The token can be used for one hour with other api.video endpoints.
response = requests.request("POST", auth_url, json=payload, headers=headers)
response = response.json()
token = response.get("access_token")

# Set up headers and payload to generate your delegated upload token and request a token.
# This token will not expire unless you specify an expiry time, or you delete it. 
auth_string = "Bearer " + token

delegate_headers = {
    "Accept": "application/vnd.api.video+json",
    "Content-Type": "application/json",
    "Authorization": auth_string
}

delegate_payload = {
    "ttl": 0
}

response = requests.request("POST", token_url, json=delegate_payload, headers=delegate_headers)

# Retrieve the token and upload your video using the token. 
response = response.json()
token = response.get("token")

# Upload by URL
d_upload_headers = {
    "Accept": "application/vnd.api.video+json"
}

d_query = {"token": token}

# Whatever the title of the file is, this will be the title of your file on upload, minus the format ending
# because it will be converted to HLS. 

d_payload = {
    "file": open("small_vid.mp4", "rb")
}

response = requests.request("POST", delegated_upload_url, files=d_payload, params=d_query, headers=d_upload_headers)

# You can check out the results of your upload. Notice that defaults are provided for your file. 
# You can change the data that comes back by updating the metadata for your video. 
print(response.json())
