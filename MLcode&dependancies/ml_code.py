from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences
import json

def predictor(sentence):
    sentence = [sentence]
    with open('tokenizer.json') as f:
        data = json.load(f)
        tokenizer = tokenizer_from_json(data)
    sequence = tokenizer.texts_to_sequences(sentence)
    padded = pad_sequences(sequence, padding='post', maxlen=100, truncating='post')
    model = load_model('fake_news_predictor.h5')
    prediction = model.predict_classes(padded)
    return prediction[0][0]

output = predictor('Trump impeachment trial to begin week of Feb. 8, Senate Democratic leader says')
