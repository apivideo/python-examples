# Authenticate with your API key and get a token for use with api.video endpoints. 
# Your token lasts for one hour 

url = "https://ws.api.video/auth/api-key"

payload = {"apiKey": "your api key here"}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)
response = response.json()
token = response.get("access_token")
