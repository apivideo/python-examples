from flask import Flask, render_template, request, redirect, url_for, abort
import os, requests

app = Flask(__name__)

app.config['UPLOAD_EXTENSIONS'] = ['.mov', '.mp4', '.m4v', '.jpm', '.jp2', '.3gp', '.3g2', '.mkv', '.mpg', '.ogv', '.webm', '.wmv' ]

@app.errorhandler(413)
def too_large(e):
    return "File is too large", 413

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    my_files = request.files
    api_key=request.form['API Key']

    # Set up variables for endpoints (we will create the third URL programmatically later)
    auth_url = "https://ws.api.video/auth/api-key"
    create_url = "https://ws.api.video/videos"    

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = {
        "apiKey": api_key
    }
    # Send the first authentication request to get a token. The token can be used for one hour with the rest of the API endpoints.
    response = requests.request("POST", auth_url, json=payload, headers=headers)
    response = response.json()
    token = response.get("access_token")
    auth_string = "Bearer " + token

    # Set up headers for authentication
    headers_bearer = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": auth_string
    }

    for item in my_files:
        uploaded_file = my_files.get(item)

        if uploaded_file.filename != '':
            file_ext = os.path.splitext(uploaded_file.filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)

    # Create the video container payload, you can add more parameters if you like, check the docs at [https://docs.api.video](https://docs.api.video)
        payload2 = {
            "title": uploaded_file.filename
        }

    # Send the request to create the container, and retrieve the videoId from the response.
        response = requests.request("POST", create_url, json=payload2, headers=headers_bearer)
        response = response.json()
        videoId = response["videoId"]

    # Create endpoint to upload your video to - you have to add the videoId into the URL
        upload_url = create_url + "/" + videoId + "/source"

    # Create upload video headers 
        headers_upload = {
            "Accept": "application/vnd.api.video+json",
            "Authorization": auth_string
        }

    # Upload the file by specifying a path to it and opening it in binary, then attaching the open file to your request 

        file = {"file": uploaded_file.read()}
        response = requests.request("POST", upload_url, files=file, headers=headers_upload)


    return redirect(url_for('index'))





        
