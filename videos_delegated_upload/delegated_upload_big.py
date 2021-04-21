# How to upload a large video that is over 128 MB to api.video. (Though this script will also work for videos under 128 MB if you want to test it out.)

import requests
import os

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

# Send the first authentication request to get a token. The token can be used for one hour with the rest of the API endpoints.
response = requests.request("POST", auth_url, json=payload, headers=headers)
response = response.json()
token = response.get("access_token")

# Set up headers and payload to generate your delegated upload token and request a token.
# The time-to-live (ttl) for the token is customizable. 0 means the token lives forever. Otherwise, you can specify in seconds. 

auth_string = "Bearer " + token

delegate_headers = {
    "Accept": "application/vnd.api.video+json",
    "Content-Type": "application/json",
    "Authorization": auth_string
}

delegate_payload = {
    "ttl": 0
}

# Send your request, and retrieve your delegated token from the response.
response = requests.request("POST", token_url, json=delegate_payload, headers=delegate_headers)

response = response.json()
token = response.get("token")

# Create an uploader for chunks of your file.
CHUNK_SIZE = 1000000

# This is our chunk reader. This is what gets the next chunk of data ready to send.
def read_in_chunks(file_object, CHUNK_SIZE):
    while True:
        datas = file_object.read(CHUNK_SIZE)
        if not datas:
            break
        yield datas

# Upload your file by breaking it into chunks and sending each piece 
def upload(file, url, token):
    content_name = str(file)
    content_path = os.path.abspath(file)
    content_size = os.stat(content_path).st_size

    print(content_name, content_path, content_size)

    f = open(content_path, "rb")

    index = 0
    offset = 0
    headers = {}
    videoId = ""

    for chunk in read_in_chunks(f, CHUNK_SIZE):
        offset = index + len(chunk)
        headers['Content-Range'] = 'bytes %s-%s/%s' % (index, offset -1, content_size)
        
        try:
            if(index == 0):
                d_query = {"token": token}
                file = {"file": chunk}
                r = requests.post(url, files=file, params=d_query, headers=headers)
                json_response = r.json()
                videoId = json_response.get("videoId")
            else: 
                d_query = {"token": token}
                body = {"videoId": videoId}
                
# Quick note here - for "file": you can put a different key name. This key name will be used to title your video 
# in api.video. You can change the title later as well as any other preferences for the video. 

                file = {"the file name you want here": chunk}
                r = requests.post(url, files=file, data=body, params=d_query, headers=headers)
                
            print(r.json())
            print("r: %s, Content-Range: %s" % (r, headers['Content-Range']))
        except Exception as e:
            print(e)
            
        index = offset
        
# Add a path to the file you want to upload, and away we go! 
upload('file_example_MP4.mp4', delegated_upload_url, token)
