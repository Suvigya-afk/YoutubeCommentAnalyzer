
class ExtractUrl:
    
    def extract_playlist_id(url):
        playlistID = ""
        index = url.index("list") + 5
        for i in range(index,len(url)):
            if(url[i] == '&'):
             break
            else:
                playlistID += url[i]
        return playlistID
    
    def extract_video_id(url):
        videoID = ""
        index = url.index("?v") + 3
        for i in range(index,len(url)):
            if(url[i] == '&'):
             break
            else:
                videoID += url[i]
        return videoID
    
# result = ExtractUrl.extract_video_id("https://www.youtube.com/watch?v=GA9_QJAhr8Q")
# print(result)
