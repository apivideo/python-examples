# This code sample will retrieve all videos from the videos endpoint. 
# If you have more than 100 videos, this code sample will not retrieve all your videos 
# as it doesn't handle pagination. See the list_all_videos_pagination.py example for that.

import requests

# Get api.video token 

url = "https://ws.api.video/auth/api-key"

payload = {"apiKey": "your api key here"}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)
response = response.json()
token = response.get("access_token")

# Retrieve the videos

url = "https://ws.api.video/videos"

querystring = {"currentPage":"1","pageSize":"100"}

headers = {
    "Accept": "application/json",
    "Authorization": token
    }

response = requests.request("GET", url, headers=headers, params=querystring)

response = response.json()
print(response)
