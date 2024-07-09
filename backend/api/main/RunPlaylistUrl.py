from googleapiclient.discovery import build
from .ExtractPlayListIdFromUrl import ExtractUrl
from .GetVideosByPlayListID import GetVideoIds
from .ListCommentsPerVideo import ListCommentsPerVideo
from .CommentProcessor import CommentPreprocessing
import os

def deletefile(file):
    file_path = os.path.abspath(file)
    os.remove(file_path)
 
def process_analysis_request(url, urltype):
        youtube = build('youtube', 'v3', developerKey="AIzaSyD0o6qSpe8H7kJYwhGKIhhIGWQbG4B6nwQ")
        if(urltype == "playlist"):
            playListId = ExtractUrl.extract_playlist_id(url)
            videoIds = GetVideoIds.get_list_of_video_ids(playListId,youtube)
            for videoId in videoIds:
                ListCommentsPerVideo.extract_all_comments(videoId,youtube)
        else:
            videoId = ExtractUrl.extract_video_id(url)
            ListCommentsPerVideo.extract_all_comments(videoId,youtube)
        
        positive_score, negative_score = CommentPreprocessing.process_data("Comments.csv")
        print(positive_score + negative_score)
        
        deletefile("Comments.csv")
        
        return positive_score, negative_score


        # https://www.youtube.com/watch?v=GA9_QJAhr8Q
    
result = process_analysis_request("https://www.youtube.com/watch?v=B9uCX2s7y7A", "video")
print(result)
     

