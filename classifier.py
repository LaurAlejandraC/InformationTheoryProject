from pickle import load
from sklearn.ensemble import RandomForestClassifier
import cPickle as pickle
import numpy as np

MAX_LENGTH = 164052


def fill_with_zeros( data ):
    result = []
    for val in data:
        temp = np.zeros(MAX_LENGTH - len(val))
        result.append(np.concatenate((val, temp.T)))
    return result


def prepare_data(words_fourier_transform):
    data = []
    words = []

    for word in words_fourier_transform:
        for fourier_transform in words_fourier_transform[word]:
            data.append(fourier_transform)
            words.append(word)

    data = fill_with_zeros( data )
    return data, words


word_filenames = load(open("word_filenames.p", "rb"))
audio_waves = load(open("audio_waves.p", "rb"))
words_fourier_transform = load(open("words_fourier_transform.p", "rb"))
data, words = prepare_data(words_fourier_transform)

prediction_model = RandomForestClassifier(n_estimators=10000, n_jobs=16, verbose=3)
prediction_model = prediction_model.fit(data, words)


pickle.dump(prediction_model, open("prediction_model.p", "wb"))