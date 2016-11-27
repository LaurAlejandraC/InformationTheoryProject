import audio_characteristics, read_data
import cPickle as pickle

audio_waves = read_data.get_audio_waves()
pickle.dump(audio_waves, open("audio_waves.p", "wb"))

words_fourier_transform = audio_characteristics.fourier_transform(audio_waves)
pickle.dump(words_fourier_transform, open("words_fourier_transform.p", "wb"))

