import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import io
import json

dataset2 = pd.read_csv('train.csv')

dataset2.dropna(inplace=True)

text = list(dataset2['text'])
labels = list(dataset2['label'])
headings = list(dataset2['title'])

'''
encoded_labels = []
for i in range(len(labels)):
    if labels[i] == 'REAL':
        encoded_labels.append(1)
    else:
        encoded_labels.append(0)
'''

training_headings = headings[:15000]
validation_headings = headings[15000:]

training_labels = np.array(labels[:15000])
validation_labels = np.array(labels[15000:])


tokenizer = Tokenizer(num_words=20000, oov_token='<OOV>')
tokenizer.fit_on_texts(training_headings)
tokenizer.word_index

training_sequences = tokenizer.texts_to_sequences(training_headings)
padded_training = pad_sequences(training_sequences, padding='post', maxlen=100, truncating='post')

validation_sequences = tokenizer.texts_to_sequences(validation_headings)
padded_validation = pad_sequences(validation_sequences, padding='post', maxlen=100, truncating='post')

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, GlobalAveragePooling1D, Conv1D, Dropout
from tensorflow.keras.backend import clear_session

model = Sequential()

model.add(Embedding(20000, 32, input_length=100))
model.add(Conv1D(64, 5, activation='relu'))
model.add(GlobalAveragePooling1D())
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(1, activation='sigmoid'))

model.summary()

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

history = model.fit(padded_training, training_labels, validation_data=(padded_validation, validation_labels), epochs=10, verbose=1)

'''
import matplotlib.pyplot as plt

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(len(acc))

plt.plot(epochs, acc, 'r', label='Training Accuracy')
plt.plot(epochs, val_acc, 'b', label='Validation Accuracy')
plt.title('Training and Validation Accuracy')

plt.figure()
plt.show()

plt.plot(epochs, loss, 'r', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and Validation loss')
plt.figure()
plt.show()
'''

tokenizer_json = tokenizer.to_json()
with io.open('tokenizer.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(tokenizer_json, ensure_ascii=False))

model.save('fake_news_predictor.h5')

clear_session()

