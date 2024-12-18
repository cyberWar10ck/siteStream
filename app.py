from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# پوشه‌ای که فیلم‌ها در آن قرار دارند
VIDEO_FOLDER = './static/video'

@app.route('/')
def index():
    # لیست کردن همه فایل‌های ویدیویی در پوشه
    videos = [f for f in os.listdir(VIDEO_FOLDER) if f.endswith(('.mp4', '.mkv', '.avi'))]
    return render_template('index.html', videos=videos)

#@app.route("/play/<video_name>")
#def play(video_name):
    #subtitle_name = video_name.replace(".mp4", ".vtt")  # فرض کنیم زیرنویس با همین نام وجود دارد
    #return send_from_directory(VIDEO_FOLDER, video_name=video_name, subtitle_name=subtitle_name)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=False)
