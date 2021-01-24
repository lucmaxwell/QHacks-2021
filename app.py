from flask import Flask, request, render_template, url_for
from ml_code import predictor

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', test="")

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    if text != "Simply Copy and Paste Your Headline Here an Press Submit~":
        predictionNum = int(predictor(text))
        result = ''
        if predictionNum == 1:
            result = 'This source is reliable'
        else:
            result = 'This source is unreliable'
        processed_text = text.upper()
        return render_template('index.html', test=result)
    else:
        return render_template('index.html', test="")

if __name__ == "__main__":
    app.run(debug = True)
