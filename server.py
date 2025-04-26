'''
Deploy a Flask application that will allow a user to provide
a text string which will then be analyzed to determine which emotion amongst a set of 5
is the most likely emotion being conveyed by the given text.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def text_analyze():
    '''
    Retrieve the provided text string from the user, then pass the text
    to be analyzed by the emotion detector. Finally, return a response displaying
    the confidence scores across all emotions and the dominant emotion.
    '''
    text = request.args.get("textToAnalyze")
    response = emotion_detector(text)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return f"""For the given statement, the system response is
            'anger': {response['anger']}, 'disgust': {response['disgust']},
            'fear': {response['fear']}, 'joy': {response['joy']}, and 'sadness': {response['sadness']}.
            The dominant emotion is {response['dominant_emotion']}"""

@app.route("/")
def render_index_page():
    '''
    Render the index page to the user, this is where the text string to be
    analyzed is provided and a response is displayed back to the user.
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
