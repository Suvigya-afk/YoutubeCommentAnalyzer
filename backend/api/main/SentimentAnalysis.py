from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

stop_words = stopwords.words("english")

def tokenize_comment(tokeize_comment):
    return word_tokenize(tokeize_comment,"english")

def remove_stop_words(comment):
    final_string = ""
    for word in tokenize_comment(comment):
        if word not in stop_words:
            final_string = final_string + " " + word
    return final_string
    
def sentiment_analyze(sentiment_text):
    try: 
        final_comment_to_process = remove_stop_words(sentiment_text)
        score = SentimentIntensityAnalyzer().polarity_scores(final_comment_to_process)
    except:
        print("Found Issue while processing below comment \n" + sentiment_text)
    return score