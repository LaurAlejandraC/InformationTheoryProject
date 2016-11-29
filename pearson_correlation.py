import numpy as np
from pickle import load
from scipy.stats import pearsonr
import time
import math

MAX_LENGTH = 164052


def prepare_data(words_fourier_transform):
    data = []
    words = []

    for word in words_fourier_transform:
        for fourier_transform in words_fourier_transform[word]:
            data.append(fourier_transform)
            words.append(word)

    data = fill_with_zeros( data )
    return data, words


def fill_with_zeros( data ):
    result = []
    for array in data:
        temp = np.zeros(MAX_LENGTH - len(array))
        result.append(np.concatenate((array, temp)))
    return result


def get_data_average(words_fourier_transform):
    average = {}
    for word in words_fourier_transform:
        current_data = fill_with_zeros(words_fourier_transform[word])
        current_data = np.average(current_data)
        average[word] = current_data
    return average

def classify( to_classify, averages ):
    p_value = 0
    result = '00'
    for word in averages:
        current_p = pearsonr(to_classify, averages[word])
        print current_p
        #if not math.isnan(current_p[0]):
        #    current_p = abs(current_p[0])
        #    if current_p > p_value:
        #        result = word
        #        p_value = current_p
    return result

print "Training"
##### Training data
word_filenames = load(open("word_filenames.p", "rb"))
audio_waves = load(open("audio_waves.p", "rb"))
words_fourier_transform = load(open("words_fourier_transform.p", "rb"))
average = get_data_average(words_fourier_transform)

print "Testing"
##### Testing data
word_filenames_test = load(open("word_filenames_test.p", "rb"))
audio_waves_test = load(open("audio_waves_test.p", "rb"))
words_fourier_transform_test = load(open("words_fourier_transform_test.p", "rb"))

test_data, test_words = prepare_data(words_fourier_transform_test)

output = []
start = time.time()
for data in test_data:
    output.append(classify(data, average))
end = time.time()
end -= start
print "Time " + str(end)

# print "Validating"
# approved = 0.0
# for i in xrange(len(output)):
#     #print output[i] + test_words[i]
#     if output[i] == test_words[i]:
#         approved += 1.0
#
# approved /= len(output)
# approved *= 100.0
# print "Accuracy percentage: " + str(approved)
