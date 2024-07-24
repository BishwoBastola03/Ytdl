from pytube import YouTube
from flask import Flask,render_template,jsonify,request
import requests

app = Flask(__name__)
@app.route('/home',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/download", methods=['POST'])
def download():
    if request.method == "POST":
        result= request.form
        video_url= request.form['URL_Link']
        def video_dowload(url):
            video=YouTube(url)
            stream=video.streams.get_highest_resolution()
            stream.download() 
        video_dowload(video_url)  
        return render_template("result.html",result = result)  

if __name__=="__main__":
    app.run(debug=True,port=3000)