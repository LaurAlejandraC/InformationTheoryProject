from pickle import load


audio_waves = load(open("audio_waves.p", "rb"))
words_fourier_transform = load(open("words_fourier_transform.p", "rb"))