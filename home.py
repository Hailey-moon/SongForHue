from flask import Flask, render_template, request
from main import openai_mood

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
# def hello():
    # return render_template('index.html')
def getMood():
    response = "white"
    if request.method == 'POST':
        mood = request.form.get("mood")

        myPrompt = "The CSS code for a color of " + mood + ":\n\nbackground-color:"
        response = openai_mood(myPrompt)
        print(response)

        # take response and make it into background color

    return render_template("index.html", mood=response)

    

if __name__ == '__main__':
    app.run()