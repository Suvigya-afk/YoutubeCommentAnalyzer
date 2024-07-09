import csv
import string
from .SentimentAnalysis import sentiment_analyze

class CommentPreprocessing:
        
        def process_data(file):
                
                positive = 1
                negative = 1
                
                with open(file, 'r', encoding='utf-8',errors='ignore') as comments:
                        comments_data = csv.reader(comments , delimiter= ',')
                        next(comments_data)
                        for row in comments_data:
                                try:
                                        if row != [] and row[0].startswith(">>>"):
                                                score = sentiment_analyze(row[2].lower().translate(str.maketrans('','',string.punctuation)))
                                                if extract_emotion(score) == "positive":
                                                        positive+=1
                                                else:
                                                        negative+=1
                                        else:
                                                continue
                                except:
                                        if(row != "\n"):
                                                print("Found some issue for comment posted by " + row[0] + " posted at " + row[1] + "." )
                                        else:
                                                print("Empty line found.")  
                                                
                print("Negative Score: ")
                print(negative)
                print("Positive Score: ")
                print(positive)
                
                percentageLikes = round((positive / (positive + negative))*100,2)
                percentagedislikes = round((negative / (positive + negative))*100,2)
                
                if positive > negative:
                        print("This playlist has a overall positive vibe with :" + str(percentageLikes) +"%' having positive thoughts about it.")
                else:
                        print("This playlist has a overall negative vibe with :" + str(percentagedislikes) +"%' having negative thoughts about it.") 
                
                return positive, negative
                
        
def extract_emotion(score):
        neg_score = score['neg']
        pos_score = score['pos']
        
        if neg_score > pos_score:
                return "negative"
        else:
                return "positive"
