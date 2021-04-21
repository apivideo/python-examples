import requests

# Get api.video refresh token (the code is almost exactly the same as for authentication
# but here you are retrieving the refresh token. If you want to use refresh tokens in your code,
# when you authenticate the first time with your api key, make sure to retrieve both tokens 
# and keep the refresh token somewhere safe. When you need it, you can use it to get another 
# access token

url = "https://ws.api.video/auth/api-key"

payload = {"apiKey": "your api key here"}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)
response = response.json()
token = response.get("refresh_token")
print(token)

# Code sample for when your access token expires and you want to use your 
# refresh token to get a new access token. 

url = "https://ws.api.video/auth/refresh"

payload = {"refreshToken": token}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)
response = response.json()
print(response)
