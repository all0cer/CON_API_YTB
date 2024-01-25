from googleapiclient.discovery import build

youtube_api_key = "YOUR_API_KEY_HERE" #For keys visit: https://console.cloud.google.com

youtube = build('youtube', 'v3', developerKey=youtube_api_key)

Playlist_ID = "YOUR_PLAYLISTID_HERE" #Search in URI after parameter "list="
Playlist_name = "Explain attack"

videos = []
nextPage = None

while True:
    request = youtube.playlistItems().list(
    part="snippet",  # changes: contentDetails, id, snippet, status, statistics...
    playlistId= Playlist_ID,
    maxResults= 3,
    pageToken=nextPage
).execute()
    videos += request['items'] # get any content in the request (json)
    
    nextPage = request.get('nextPageToken')

    if nextPage is None:
        break
    
videos_titles = list(map(lambda x: x['snippet']['title'], videos))
print(videos_titles)