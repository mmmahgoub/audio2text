from flask import Flask, render_template, request
import speech_recognition as sr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recognize', methods=['POST'])
def recognize():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak something...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return {'text': text}
    except sr.UnknownValueError:
        return {'error': 'Could not understand audio'}
    except sr.RequestError as e:
        return {'error': f'Could not request results from Google Speech Recognition service; {e}'}

if __name__ == '__main__':
    app.run(debug=True)
