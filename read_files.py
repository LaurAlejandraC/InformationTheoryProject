import os

filenames = os.listdir("Corpus")
words_filenames = {}


def get_words_filenames():
    global words_filenames
    for current_file in filenames:
        word = current_file.split(".")[2]
        if word not in words_filenames:
            words_filenames[word] = [current_file]
        else:
            words_filenames[word].append(current_file)

get_words_filenames()

