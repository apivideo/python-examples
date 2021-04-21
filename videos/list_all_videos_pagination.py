# Retrieve a list of all pages of videos in your account. 
# You must handle pagination if you have more than one page of entries to return. 

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

# Works with retrieving live streams endpoint as well. Takes a URL and an access token
# and returns all your videos. You can adjust the page size to return up to 100 entries per page.
# Entries are returned in a list. 

def paginated_response(url, token):
    headers = {
    "Accept": "application/json",
    "Authorization": token
    }
    json_response = requests.request("GET", url, headers=headers, params={})
    json_response = json_response.json()
    total_pages = 1
    if json_response is not None:
        if 'pagination' in json_response:
            total_pages = json_response['pagination']['pagesTotal']
    video_info = list(json_response['data'])
    if total_pages > 1:
        for i in range(2, total_pages +1):
            querystring = {"currentPage":str(i), "pageSize":"25"}
            r = requests.request("GET", url, headers=headers, params=querystring)
            r = r.json()
            video_info = video_info + r['data']
    return video_info

print(paginated_response(url, token))
