from Tkinter import *
from PIL import Image, ImageTk


class App:
    def __init__(self, master):
        master.title("Word Recognizer")
        master.iconbitmap('mic.ico')
        master.geometry('{}x{}'.format(400, 200))

        top = Frame(master)
        top.pack(side=TOP)

        self.imgRecord = ImageTk.PhotoImage(file="red-mic.png")
        self.imgStop = ImageTk.PhotoImage(file="stop.png")

        self.btnRecording = Button(master, text=" Grabar ", image=self.imgRecord, compound="left",
                                   command=self.recording)
        self.btnRecording.image = self.imgRecord
        self.btnRecording.pack(in_=top, side=LEFT, pady=20, padx=10)

        self.btnStop = Button(master, text=" Detener ", state="disabled", image=self.imgStop, compound="left",
                              command=self.stopping)
        self.btnStop.image = self.imgStop
        self.btnStop.pack(in_=top, side=LEFT, pady=20, padx=10)

        self.lbl = Label(text="La palabra es: ")
        self.lbl.pack()

        self.lblOutput = Label(text="")
        self.lblOutput.pack()

    def recording(self):
        self.btnRecording['state'] = 'disabled'
        self.btnStop['state'] = 'normal'
        self.lblOutput['text'] = ""

    def stopping(self):
        self.btnRecording['state'] = 'normal'
        self.btnStop['state'] = 'disabled'
        self.lblOutput['text'] = "Word"


master = Tk()
app = App(master)
master.mainloop()
