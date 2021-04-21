# When you stop live streaming, if you selected record, a copy of your live stream is stored for playback. 
# If you wanted to retrieve all your videos associated with a particular live stream ID, you could use the videos endpoint with a query
# that filters for just these videos, then return those in a list. This sample doesn't handle pagination. 
# For an example of how to implement pagination, see list_all_videos_pagination.py.

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

# Retrieve the videos that were created using a particular live stream ID

url = "https://ws.api.video/videos"

querystring = {"currentPage":"1","pageSize":"100"}

headers = {
    "Accept": "application/json",
    "Authorization": token
    }
querystring = {"liveStreamId":"live stream ID here","currentPage":"1","pageSize":"25"}
response = requests.request("GET", url, headers=headers, params=querystring)

response = response.json()
print(response)
