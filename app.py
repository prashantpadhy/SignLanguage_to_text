from cmath import pi
from pickle import TRUE
from flask import Flask, render_template, Response
from helper import DetectSignLang

app = Flask(__name__)

detectSignLang=DetectSignLang()

@app.route('/')
def index():
    return render_template('sign to text.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/manual')
def manual():
    return render_template('manual.html')

def gen(camera):
    while True:
        if(camera.turnOff==True):
            break
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    
@app.route('/video_feed')
def video_feed():
    global detectSignLang
    detectSignLang=DetectSignLang()
    return Response(gen(detectSignLang),mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/video_off')
def video_off():
    detectSignLang.turnOff=True
    detectSignLang.close()
    return "Nothing"


if __name__ == '__main__':
    app.run(debug=True)