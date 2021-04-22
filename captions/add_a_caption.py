# If you have a caption file prepared and the videoId for the video
# you want to add it to, you can use this code sample to do an upload.
# This code will upload any files you have in the same directory as this 
# code snippet that end '.vtt'

import requests
import glob, os
import re

# Get an access token using your API key 
url = "https://ws.api.video/auth/api-key"

payload = {"apiKey": "api key here"}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)
response = response.json()
token = response.get("access_token")

# Add Caption Files

headers = {
    "Accept": "application/json",
    "Authorization": token
}

videoId = "vi6FZib80ZrC8q73AekJqNDH"

# Look through the files in your directory for caption files. (Files that end .vtt.)
for file in os.listdir("./"):
    if file.endswith(".vtt"):
       result = re.search('_(.*)\.', file)
       result = result.group()
       result = result.strip('_')
       result = result.strip('.')
       caption = { 
            'file': (file, open(file, "rb"))
       }
       url = "https://ws.api.video/videos/" + videoId + "/captions/" + result
       response = requests.request("POST", url, files=caption, headers=headers)
       print(response.json())
