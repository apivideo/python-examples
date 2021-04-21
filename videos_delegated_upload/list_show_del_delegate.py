# This code sample shows you how to work with delegated tokens without an SDK.
# There's a sample for how to list all tokens, retrieve details about a token, and delete a token. 

import requests

# Set up variables for endpoints (we will create the third URL programmatically later)
auth_url = "https://ws.api.video/auth/api-key"
token_url = "https://ws.api.video/upload-tokens"

# Set up headers and payload for first authentication request
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

payload = {
    "apiKey": "your API key here"
}

# AUTHENTICATION - GET ACCESS TOKEN
# Send the first authentication request to get a token. The token can be used for one hour with the rest of the API endpoints.
response = requests.request("POST", auth_url, json=payload, headers=headers)
response = response.json()
token = response.get("access_token")

# DELEGATED UPLOADS - LIST ACTIVE TOKENS
url = "https://ws.api.video/upload-tokens"

headers = {
    "Accept": "application/vnd.api.video+json",
    "Content-Type": "application/json",
    "Authorization": "Bearer " + token
}

querystring = {"currentPage": "3", "pageSize": "25"}
headers = {"Accept": "application/vnd.api.video+json", "Authorization": "Bearer " + token}

show_response = requests.request("GET", token_url, headers=headers, params=querystring)
print(show_response.json())

# DELEGATED UPLOADS - RETRIEVE DETAILS ABOUT A TOKEN

url = "https://ws.api.video/upload-tokens/" + "the token you want to look up"

headers = {
    "Accept": "application/vnd.api.video+json",
    "Authorization": "Bearer " + token
}

response = requests.request("GET", url, headers=headers)

print(response.text)

# DELEGATED UPLOADS - DELETE ALL TOKENS  

url = "https://ws.api.video/upload-tokens/" + "the token you want to delete"

headers = {
    "Accept": "application/vnd.api.video+json",
    "Authorization": "Bearer " + token
}

response = requests.request("DELETE", url, headers=headers)

print(response.text)
