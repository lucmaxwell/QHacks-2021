from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences
import json
import keras
import numpy as np

def predictor(sentence):
    sentence = [sentence]
    with open('tokenizer_2.json') as f:
        data = json.load(f)
        tokenizer = tokenizer_from_json(data)
    sequence = tokenizer.texts_to_sequences(sentence)
    padded = pad_sequences(sequence, padding='post', maxlen=100, truncating='post')
    model = load_model('fake_news_predictor_2.h5')
    prediction = model.predict_classes(padded)
    return prediction[0][0]