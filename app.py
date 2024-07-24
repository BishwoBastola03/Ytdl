
from flask import Flask, request, jsonify
from pytube import YouTube

app = Flask(__name__)

@app.route('/api/download', methods=['POST'])
def download_video():
    video_url = request.json['video_url']
    yt = YouTube(video_url)
    streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
    stream = streams.first()
    stream.download()
    return jsonify({'status': 'success', 'message': 'Video downloaded successfully'})

