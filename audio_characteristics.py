from scipy.fftpack import rfft


def fourier_transform( audio_waves ):
    words_fourier_transform = {}
    for word in audio_waves:
        words_fourier_transform[word] = []
        for audio_wave in audio_waves[word]:
            data = rfft(audio_wave)
            data = abs(data)
            data = data.flatten()
            words_fourier_transform[word].append(data)
    return words_fourier_transform