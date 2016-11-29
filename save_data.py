import audio_characteristics, read_data
import cPickle as pickle

word_filenames = read_data.get_word_filenames(['01','02','03','04'])
pickle.dump(word_filenames, open("word_filenames_test.p", "wb"))

audio_waves = read_data.get_audio_waves( word_filenames )
pickle.dump(audio_waves, open("audio_waves_test.p", "wb"))

words_fourier_transform = audio_characteristics.fourier_transform(audio_waves)
pickle.dump(words_fourier_transform, open("words_fourier_transform_test.p", "wb"))

