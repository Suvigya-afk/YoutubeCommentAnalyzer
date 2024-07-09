from googleapiclient.discovery import build

class GetVideoIds:
    
    # passing the Playlist ID and the YouTube client.
    def get_list_of_video_ids(playListId, youtube):
        videoIds = []
        
        request = youtube.playlistItems().list(
        part="snippet,contentDetails",
        playlistId=playListId,
        maxResults=100
        )
        response = request.execute()
        
        for item in response['items']:
            videoID = item['contentDetails']['videoId']
            videoIds.append(videoID)
        
        return videoIds