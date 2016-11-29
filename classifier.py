from pickle import load
from sklearn.ensemble import RandomForestClassifier
import read_data, audio_characteristics
import numpy as np
import time

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


test_filenames = read_data.get_word_filenames('08')
test_audio_waves = read_data.get_audio_waves(test_filenames)
test_words_fourier_transform = audio_characteristics.fourier_transform(test_audio_waves)

test_data, test_words = prepare_data(test_words_fourier_transform)
print "Start prediction"
start = time.time()
test_data = test_data[:15]
output = prediction_model.predict(test_data, n_jobs=16)
end = time.time()
print "End prediction"
print end-start

print output

approved = 0.0
for i in xrange(len(output)):
    if test_words[i] == output[i]:
        approved += 1.0

print "Accuracy: " + str(approved)
approved /= len(output)
approved *= 100.0
print "Accuracy percentage: " + str(approved)