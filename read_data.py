import os
from scipy.io.wavfile import read, write

filenames = os.listdir("Corpus")


def get_word_filenames():
    word_filenames = {}
    for current_file in filenames:
        word = current_file.split(".")[2]
        if word not in word_filenames:
            word_filenames[word] = [current_file]
        else:
            word_filenames[word].append(current_file)
    return word_filenames


def get_wav_data(file):
    return read(file)[1]


def make_wav(data, outfile, samplerate):
    write(outfile, samplerate, data)


def get_audio_waves( word_filenames ):
    audio_waves = {}
    for word in word_filenames:
        audio_waves[word] = []
        for filename in word_filenames[word]:
            audio_waves[word].append( get_wav_data("Corpus/" + filename) )
    return audio_waves


result = get_audio_waves( get_word_filenames() )
print result['01'][:10]