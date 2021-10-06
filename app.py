from flask import Flask
import datetime
from youtube_transcript_api import YouTubeTranscriptApi

# define a variable to hold you app
app = Flask(__name__)


# define your resource endpoints
@app.get('/')
def index_page():
    return "Hello World"


# start the server on localhost:8000
if __name__ == '__main__':
    app.run(debug=True, port=8000)
