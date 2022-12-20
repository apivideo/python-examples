[![badge](https://img.shields.io/twitter/follow/api_video?style=social)](https://twitter.com/intent/follow?screen_name=api_video)

[![badge](https://img.shields.io/github/stars/apivideo/python-examples?style=social)](https://github.com/apivideo/python-examples)

[![badge](https://img.shields.io/discourse/topics?server=https%3A%2F%2Fcommunity.api.video)](https://community.api.video)

![](https://github.com/apivideo/.github/blob/main/assets/apivideo_banner.png)

[api.video](https://api.video) is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.

# python-examples (without an SDK)
These are code samples for working with api.video in Python without an SDK. Grab a sample that matches your use case and you can use it as-needed. These samples use the requests library, which you may need to install if you haven't already. 

# Available Samples:

## Authentication 
* [Authentication](https://github.com/apivideo/python-examples/blob/main/authentication/authentication.py)
* [Refresh Token](https://github.com/apivideo/python-examples/blob/main/authentication/refresh_token.py)

## Captions Endpoint 
* [Add a Caption](https://github.com/apivideo/python-examples/blob/main/captions/add_a_caption.py)

## Live Endpoint
* [Add a Thumbnail to Your Live Stream](https://github.com/apivideo/python-examples/blob/main/live/add_thumbnail_to_ls.py)
* [Create a Live Stream Container](https://github.com/apivideo/python-examples/blob/main/live/create_ls_container.py)
* [Retrieve a Live Stream](https://github.com/apivideo/python-examples/blob/main/live/retrieve_ls.py)

## Videos Endpoint
* [List All Videos w Pagination](https://github.com/apivideo/python-examples/blob/main/videos/list_all_videos_pagination.py)
* [List All Videos up to 100](https://github.com/apivideo/python-examples/blob/main/videos/list_all_videos_up_to_100.py)
* [List Videos By liveStreamId](https://github.com/apivideo/python-examples/blob/main/videos/list_videos_by_livestreamid.py)
* [Pick a Thumbnail](https://github.com/apivideo/python-examples/blob/main/videos/pick_a_thumbnail.py)
* [Upload a Thumbnail](https://github.com/apivideo/python-examples/blob/main/videos/upload_a_thumbnail.py)
* [Upload a Video From Your Computer (works for files under 128MB)](https://github.com/apivideo/python-examples/blob/main/videos/upload_from_computer.py)
* [Upload a Large Video (works for files 128MB and up)](https://github.com/apivideo/python-examples/blob/main/videos/upload_large_video.py)
* [Upload a Video by URL](https://github.com/apivideo/python-examples/blob/main/upload_video_by_url.py)

## Videos - Delegated Upload
* [Delegated Uploads](https://github.com/apivideo/python-examples/blob/main/videos_delegated_upload/delegated_upload.py)
* [Delegated Uploads for Files That are 128MB and up](https://github.com/apivideo/python-examples/blob/main/videos_delegated_upload/delegated_upload_big.py)
* [List Delegate Tokens, Show a Single Token, Delete a Token](https://github.com/apivideo/python-examples/blob/main/videos_delegated_upload/list_show_del_delegate.py)

# Associated Tutorials 

## Authentication Endpoint Tutorials
* [When Your Token Expires, Hit Refresh and Protect Your API Key](https://api.video/blog/tutorials/when-your-token-expires-hit-refresh-and-protect-your-api-key) 

## Captions Endpoint Tutorials
* [Add Captions to Your Video with Maestra and api.video](https://api.video/blog/tutorials/add-captions-to-your-video-with-maestra-and-api-video) 

## Live Endpoint Tutorials
* [Live Stream to the Browser with FFMPEG CLI and Python](https://api.video/blog/tutorials/live-stream-to-the-browser-with-ffmpeg-cli-and-python)

## Videos Endpoint Tutorials 
* [Choose a Thumbnail with api.video's Pick a Thumbnail Endpoint](https://api.video/blog/tutorials/choose-a-thumbnail-with-api-video-s-pick-a-thumbnail-endpoint)
* [Create a Thumbnail For Your Video with Python and FFMPEG](https://api.video/blog/tutorials/automatically-add-a-thumbnail-to-your-video-with-python-and-ffmpeg)
* [How to Add a Thumbnail to Your Live Stream](https://api.video/blog/tutorials/how-to-add-a-thumbnail-to-your-live-stream)
* [Upload a Big Video File Using Python](https://api.video/blog/tutorials/upload-a-big-video-file-using-python)
* [Upload a Video From Your Computer with the api.video API (Python)](https://api.video/blog/tutorials/upload-a-video-from-your-computer-with-the-api-video-api-python)
* [Upload a Video with the api.video API Using a Public URL](https://api.video/blog/tutorials/upload-a-video-with-the-api-video-api-using-a-public-url-python)

## Videos - Delegated Uploads Tutorials 
* [Delegated Uploads for Videos Large and Small](https://api.video/blog/tutorials/delegated-uploads-for-videos-large-and-small-python)
* [Listing, Retrieving, and Deleting Delegated Tokens](https://api.video/blog/tutorials/listing-retrieving-and-deleting-delegated-tokens)

## Analytics Endpoint Tutorials 
* [Api.video Analytics: Add Markers Representing Viewer Density Per City to a Map with Observable](https://api.video/blog/tutorials/api-video-analytics-add-markers-representing-viewer-density-per-city-to-a-map-wit)
* [Api.video Analytics: Build a Choropleth Map (and Find Out What One Is)](https://api.video/blog/tutorials/use-observable-to-create-a-choropleth-map-of-your-viewers) 
* [Api.video Analytics: Create a Pie Chart Showing What Operating System is Most Popular to View](https://api.video/blog/tutorials/api-video-analytics-create-a-pie-chart-showing-operating-system)
* [Using Analytics to Analyze Where to Edit a Video](https://api.video/blog/tutorials/using-analytics-to-analyze-where-to-edit-a-video)
