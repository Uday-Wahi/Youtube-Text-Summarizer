from youtube_transcript_api import YouTubeTranscriptApi
from transformers import T5ForConditionalGeneration, T5Tokenizer
from flask import Flask, request


model = T5ForConditionalGeneration.from_pretrained("t5-small")
tokenizer = T5Tokenizer.from_pretrained("t5-small")
app = Flask(__name__)


def getTranscript(id: str) -> list:
    return YouTubeTranscriptApi.get_transcript(id)


def extractText(dictionary: list) -> str:
    text = ""
    for d in dictionary:
        text = text + d['text'] + " "
    return text


def cleanText(text: str) -> str:
    cleanedText = " ".join(text.split())
    return cleanedText


def summarizeText(longText: str) -> str:
    inputs = tokenizer.encode("summarize: " + longText, return_tensors="pt")
    outputs = model.generate(
        inputs,
        num_beams=4,
        no_repeat_ngram_size=2,
        min_length=200,
        max_length=300,
        early_stopping=True
    )
    decoded = tokenizer.decode(outputs[0])
    return decoded


# Index page
@app.route("/")
def index():
    return "<h2>Goto /api/summarize?videoID=<youtube_video_id></h2>"


# api call to summarize
@app.route("/api/summarize")
def summarize() -> str:
    return summarizeText(cleanText(extractText(getTranscript(request.args.get("videoID")))))


if __name__ == "__main__":
    app.run(debug=True, port=8000, host='0.0.0.0')
