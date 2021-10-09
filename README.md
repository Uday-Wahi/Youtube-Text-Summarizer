
# Youtube-Text-Summarizer

#### Built using Flask
This API helps to summarize the youtube videos based on their caption.\
It does so using Google trained NLP [T5](https://huggingface.co/transformers/model_doc/t5.html) model passed through [HuggingFace](https://huggingface.co/) transformer and [PyTorch](https://pytorch.org/) for GPU utilization.
## API Reference

#### Get subtitle summary

```http
  GET /api/summarize?videoID={video_id}
```

| Parameter | Type     | Description          |
| :---------| :--------| :--------------------|
| `video_id`| `string` | **Youtube** video id |

Takes the video ID and returns the summarized subtitle.

## Run Locally

#### Clone the project

```bash
  git clone https://github.com/Uday-Wahi/Youtube-Text-Summarizer.git
```

#### Go to the project directory

```bash
  cd Youtube-Text-Summarizer
```

#### Create a virtual environment

```bash
  python3 -m venv <folder name>
```

#### Activate the virtual environment

- On Unix / MacOS
```bash
  source venv/bin/activate
```

- On Windows
```ps
  source venv/bin/activate.bat
```

#### Install dependencies

- On Unix / MacOS
```bash
  pip install -r requirements.txt
```

- On Windows
```ps
  pip3 install -r requirements.txt
```

#### Start the server

```bash
  python app.py
```
## Authors

- [@Uday Wahi](https://www.github.com/Uday-Wahi)

  
## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/uday-wahi/)
## 🚀 About Me
I'm a full stack web developer...\
Android front-end developer..\
Learning cybersecurity.
## Tech Stack

**Server:** [Flask](https://palletsprojects.com/p/flask/)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[T5-model](https://huggingface.co/transformers/model_doc/t5.html)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HuggingFace transformer](https://huggingface.co/)
  