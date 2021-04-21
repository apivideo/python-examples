# How to upload a large video that is over 128 MB to api.video. (Though this script will also work for videos under 128 MB if you want to test it out.)

import requests
import os 

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

# Set up headers for authentication - the rest of the endpoints use Bearer authentication.

auth_string = "Bearer " + token

headers2 = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": auth_string
}

# Create the video container payload, you can add more parameters if you like, check out the docs at https://docs.api.video
payload2 = {
    "title": "Demo Vid from my Computer",
    "description": "Video upload test."
}

# Send the request to create the container, and retrieve the videoId from the response.
response = requests.request("POST", create_url, json=payload2, headers=headers2)
response = response.json()
videoId = response["videoId"]

# Create endpoint to upload video to - you have to add the videoId into the URL
upload_url = create_url + "/" + videoId + "/source"

# Set up the chunk size. This is how much you want to read from the file every time you grab a new chunk of your file to read.
# If you're doing a big upload, the recommendation is 50 - 80 MB (50000000-80000000 bytes). It's listed at 1MB (1000000 bytes) because 
# then you can try this sample code with a small file just to see how it will work.

CHUNK_SIZE = 1000000


# This is our chunk reader. This is what gets the next chunk of data ready to send.
def read_in_chunks(file_object, CHUNK_SIZE):
    while True:
        data = file_object.read(CHUNK_SIZE)
        if not data:
            break
        yield data

# Upload your file by breaking it into chunks and sending each piece 
def upload(file, url):
    content_name = str(file)
    content_path = os.path.abspath(file)
    content_size = os.stat(content_path).st_size

    print(content_name, content_path, content_size)

    f = open(content_path, "rb")

    index = 0
    offset = 0
    headers = {}

    for chunk in read_in_chunks(f, CHUNK_SIZE):
        offset = index + len(chunk)
        headers['Content-Range'] = 'bytes %s-%s/%s' % (index, offset -1, content_size)
        headers['Authorization'] = auth_string
        index = offset
        try:

            file = {"file": chunk}
            r = requests.post(url, files=file, headers=headers)
            print(r.json())
            print("r: %s, Content-Range: %s" % (r, headers['Content-Range']))
        except Exception as e:
            print(e)

# Add a path to the file you want to upload, and away we go! 
upload('your-giant-file-here.mp4', upload_url)
