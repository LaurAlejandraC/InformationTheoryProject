from Tkinter import *
from PIL import Image, ImageTk
from numpy import *
import sounddevice as sd
import os
from scipy.io.wavfile import read, write
from tkFileDialog import askopenfilename
import read_data, classifier, audio_characteristics
from scipy.fftpack import rfft


class App:
    def __init__(self, master):
        self.fs = 48000

        self.words = {'01':'Safer', '02':'Wahed', '03':'Ethnan', '04':'Thlatha', '05':'Arbah', '06':'Khamsah', '07':'Setah', '08':'Sabah', '09':'Thamanah', '10':'Tesah', '11':'Al-tansheet', '12':'Al-tahweel', '13':'Al-raseed', '14':'Al-tasdeed', '15':'Naam', '16':'Laa', '17':'Al-tamueel', '18':'Al-baynat', '19':'Al-hesab', '20':'Enha'}

        print "Initial load"
        self.prediction_model = classifier.load_model()
        print "End load"

        master.title("Word Recognizer")
        # master.iconbitmap("mic.ico")
        master.geometry('{}x{}'.format(500, 250))

        top = Frame(master)
        top.pack(side=TOP)

        center = Frame(master)
        center.pack(side=TOP)

        bottom = Frame(master)
        bottom.pack(side=TOP)

        #self.img_record = ImageTk.PhotoImage(file="red-mic.png")
        #self.img_stop = ImageTk.PhotoImage(file="stop.png")
        #self.img_play = ImageTk.PhotoImage(file="play.png")
        #self.img_file = ImageTk.PhotoImage(file="file.png")

        self.btn_recording = Button(master, text=" Grabar        ", compound="left",
                                    command=self.recording)
        self.btn_recording.pack(in_=top, side=LEFT, pady=20, padx=10)

        self.btn_stop = Button(master, text=" Detener      ", state="disabled", compound="left",
                               command=self.stopping)
        self.btn_stop.pack(in_=top, side=LEFT, pady=20, padx=10)

        self.btn_choose_file = Button(master, text=" Seleccionar ", state="normal", compound="left",
                               command=self.choose_file)
        self.btn_choose_file.pack(in_=center, side=LEFT, pady=20, padx=10)

        self.btn_play = Button(master, text=" Reproducir ", state="normal", compound="left",
                               command=self.playing)
        self.btn_play.pack(in_=center, side=LEFT, pady=20, padx=10)

        self.lbl = Label(text="La palabra es: ")
        self.lbl.pack(in_=bottom)

        self.lbl_output = Label(text="")
        self.lbl_output.pack()



    def recording(self):
        self.btn_recording['state'] = 'disabled'
        self.btn_stop['state'] = 'normal'
        self.lbl_output['text'] = ""

        duration = 3  # seconds
        self.my_recording = sd.rec(duration * self.fs, samplerate=self.fs, channels=2)
        self.recognize()

    def stopping(self):
        self.btn_recording['state'] = 'normal'
        self.btn_stop['state'] = 'disabled'

    def playing(self):
        self.btn_recording['state'] = 'normal'
        self.btn_stop['state'] = 'disabled'
        sd.play(self.my_recording, self.fs)

    def choose_file(self):
        filename = askopenfilename()
        self.my_recording = read_data.get_wav_data(filename)
        self.playing()
        self.recognize()

    def recognize(self):
        data = rfft(self.my_recording)
        data = abs(data)
        data = data.flatten()
        data = classifier.fill_with_zeros([data])
        output = self.prediction_model.predict(data)
        self.lbl_output['text'] = self.words[output[0]]
        print self.words[output[0]]


master = Tk()
app = App(master)
master.mainloop()
