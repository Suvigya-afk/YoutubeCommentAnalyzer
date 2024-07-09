from googleapiclient.discovery import build

class ListCommentsPerVideo:
    
    def extract_all_comments(videoId, youtube):
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=videoId,
            textFormat="plainText",
            maxResults=100
            )
        
        response = request.execute()
        
        file = open('Comments.csv','a',encoding='utf-8')
        for item in response['items']:
            username = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
            publishedAt = item['snippet']['topLevelComment']['snippet']['publishedAt']
            comment = remove_new_line_from_comment(item['snippet']['topLevelComment']['snippet']['textOriginal'].replace(",",""))
            file.write("\n" + ">>>" + username + "," + publishedAt +  "," + comment)
            
    

def remove_new_line_from_comment(comment):
    final_line = ""
    lines = comment.split("\n")
    for line in lines:
        final_line +=line
    return final_line

        
        
        
        
        
        
        
        
     
    
   
        
            
    

