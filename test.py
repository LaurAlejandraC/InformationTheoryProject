from pickle import load
import read_data
import audio_characteristics
import classifier
import time

prediction_model = load(open("prediction_model.p", "rb"))

test_filenames = read_data.get_word_filenames('02')
test_audio_waves = read_data.get_audio_waves(test_filenames)
test_words_fourier_transform = audio_characteristics.fourier_transform(test_audio_waves)

test_data, test_words = classifier.prepare_data(test_words_fourier_transform)
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