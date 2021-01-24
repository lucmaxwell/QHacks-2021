from flask import Flask, request, render_template, url_for
#from ml_code import predictor

app = Flask(__name__)
'''
predictionNum = int(predictor('Trump is president'))

result = ''
if predictionNum == 1:
    result = 'reliable'
else:
    result = 'unreliable'
'''

@app.route('/')
def index():
    return render_template('index.html', test="replace with result from ML file") 

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

if __name__ == "__main__":
    app.run(debug = True)
