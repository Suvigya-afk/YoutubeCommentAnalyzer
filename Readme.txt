Project: YouTube Sentiment Analysis Tool

Overview:
In response to YouTube's removal of visible dislike counts on videos, which can obscure viewers' ability to gauge a video's reception, I developed a web tool to provide insights into the popularity of YouTube videos and playlists through sentiment analysis of viewer comments.

Solution:
I created a web application using Django and React that analyzes the sentiment of comments on YouTube videos and playlists. The process works as follows:

Data Collection:
Users can input the URL of a video or playlist. Utilizing the Google API client, the tool retrieves comments associated with the specified content.
Data Processing:
The collected comments are stored in a CSS file for further analysis. A separate process extracts each comment and performs sentiment analysis, calculating positive and negative sentiment scores.
Visualization:
The sentiment scores are displayed on-screen using a pie chart, allowing users to easily interpret the overall sentiment of the comments.
Impact:
This tool helps viewers gain valuable insights into the general sentiment surrounding a video or playlist, offering a clearer understanding of its reception beyond traditional like/dislike metrics. By presenting positive and negative sentiment scores in a visually engaging pie chart format, users can make more informed decisions about which content to engage with, thereby enhancing their viewing experience. Furthermore, it provides content creators with actionable feedback on audience reactions, which can inform future video production and engagement strategies.

Tools/Techs Used:
Backend: Django, JWT Authentication, NLTK, Sentiment Analysis
Frontend: ReactJS, Axios, Charts

Current Challenges:
Since the api call to the google client only fetches a limited number of comments at time, a more persistent approach of storing 
comments with a DB would help.
Future Objectives:
Enable feature for shorts as well.

Install below:
Have to install nltk, use the settings.py file.
Run the requirements.txt file for backend.
Install vite for frontend.

Run below to start the project:
To run backend, go to the main backend dir and run command "python3 manage.py runserver".
To run the frontend, open terminal in src, and run command "npm run dev".
