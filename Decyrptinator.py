import os
from os import path
import tkinter
import tkinter.messagebox
from tkinter import messagebox as ms
from tkinter import *
import datetime
import tkinter.tix


# Code, um eine Datei in einer anderen Datei zu verstecken


def getkey(filename, keyname, newfile):
    original = open(filename, "rb").read()
    encrypted = open(newfile, "rb").read()
    dat1_length = len(original)
    dat2_length = len(encrypted)
    if dat1_length > dat2_length:
        encrypted += os.urandom(dat1_length - dat2_length)
    else:
        original += os.urandom(dat2_length - dat1_length)
    with open(filename, "wb") as out:
        out.write(original)
    with open(newfile, "wb") as out:
        out.write(encrypted)
    key = bytes(a ^ b for (a, b) in zip(original, encrypted))
    with open(keyname + ".key", "wb") as key_out:
        key_out.write(key)


# Code, um eine Datei zu verschlüsseln


def encrypt(filename, keyname, newfile):
    to_encrypt = open(filename, "rb").read()
    size = len(to_encrypt)
    key = os.urandom(size)
    with open(keyname + ".key", "wb") as key_out:
        key_out.write(key)
    encrypted = bytes(a ^ b for (a, b) in zip(to_encrypt, key))
    with open(newfile, "wb") as encrypted_out:
        encrypted_out.write(encrypted)


# Code, um eine Datei zu entschlüsseln


def decrypt(filename, keyname, newfile):
    encrypted = open(filename, "rb").read()
    key = open(keyname, "rb").read()
    decrypted = bytes(a ^ b for (a, b) in zip(encrypted, key))
    with open(newfile, "wb") as decrypted_out:
        decrypted_out.write(decrypted)


# Erstelle Fenster


window = tkinter.Tk()
window.title("Decryptinator")
app_width = 800
app_height = 400
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)
window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
window.resizable(False, False)
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)


def check_but2_command(but2, path1, path2, path3):
    if but2 == 1:
        if path.isfile(path1):
            if path.isfile(path2 + ".key"):
                response = ms.askokcancel("Warnung",
                                          "Dieser Schlüssel existiert schon! Soll dieser überschrieben werden?")
                if response == 1:
                    if path.isfile(path3):
                        getkey(path1, path2, path3)
                        ms.showinfo("Erfolgreich", "Datei wurde erfolgreich versteckt!")
                    else:
                        ms.showerror("Error", "Versteckdatei existiert nicht!")
            else:
                if path.isfile(path3):
                    getkey(path1, path2, path3)
                    ms.showinfo("Erfolgreich", "Datei wurde erfolgreich versteckt!")
                else:
                    ms.showerror("Error", "Versteckdatei existiert nicht!")
        else:
            ms.showerror("Error", "Zu versteckende Datei existiert nicht!")

    elif but2 == 2:
        if path.isfile(path1):
            if path.isfile(path2):
                if path.isfile(path3):
                    response = ms.askokcancel("Warnung",
                                              "Diese Datei existiert schon! Soll diese überschrieben werden?")
                    if response == 1:
                        decrypt(path1, path2, path3)
                        ms.showinfo("Erfolgreich", "Datei wurde erfolgreich herausgelesen!")

                elif path3 == "":
                    ms.showerror("Error", "die neue Datei hat keinen Namen!")

                else:
                    decrypt(path1, path2, path3)
                    ms.showinfo("Erfolgreich", "Datei wurde erfolgreich herausgelesen!")
            else:
                ms.showerror("Error", "Der Schlüssel existiert nicht!")
        else:
            ms.showerror("Error", "Die zu herauslesende Datei existiert nicht!")

    elif but2 == 3:
        if path.isfile(path1):
            if path.isfile(path2 + ".key"):
                response = ms.askokcancel("Warnung",
                                          "Dieser Schlüssel existiert schon! Soll dieser überschrieben werden?")
                if response == 1:
                    if path.isfile(path3):
                        response = ms.askokcancel("Warnung",
                                                  "Diese Datei existiert schon! Soll diese überschrieben werden?")
                        if response == 1:
                            encrypt(path1, path2, path3)
                            ms.showinfo("Erfolgreich", "Datei wurde erfolgreich verschlüsselt!")
                    else:
                        encrypt(path1, path2, path3)
                        ms.showinfo("Erfolgreich", "Datei wurde erfolgreich verschlüsselt!")
            else:
                if path.isfile(path3):
                    response = ms.askokcancel("Warnung",
                                              "Diese Datei existiert schon! Soll diese überschrieben werden?")
                    if response == 1:
                        encrypt(path1, path2, path3)
                        ms.showinfo("Erfolgreich", "Datei wurde erfolgreich verschlüsselt!")
                else:
                    encrypt(path1, path2, path3)
                    ms.showinfo("Erfolgreich", "Datei wurde erfolgreich verschlüsselt!")
        else:
            ms.showerror("Error", "Die zu verschlüsselnde Datei existiert nicht!")

    elif but2 == 4:
        if path.isfile(path1):
            if path.isfile(path2):
                if path.isfile(path3):
                    response = ms.askokcancel("Warnung",
                                              "Diese Datei existiert schon! Soll diese überschrieben werden?")
                    if response == 1:
                        decrypt(path1, path2, path3)
                        ms.showinfo("Erfolgreich", "Datei wurde erfolgreich entschlüsselt!")

                elif path3 == "":
                    ms.showerror("Error", "die neue Datei hat keinen Namen!")

                else:
                    decrypt(path1, path2, path3)
                    ms.showinfo("Erfolgreich", "Datei wurde erfolgreich entschlüsselt!")
            else:
                ms.showerror("Error", "Der Schlüssel existiert nicht!")
        else:
            ms.showerror("Error", "Die zu entschlüsselnde Datei existiert nicht!")


def show_frame(oldframe, newframe):
    oldframe.grid_forget()
    newframe.grid(row=0, column=0, sticky='nsew')


class BasicFrame(Frame):
    def __init__(self, the_window, framename):
        self.maincolor = "#F0F8FF"
        self.secondcolor = "black"
        self.thirdcolor = "#757c88"
        super().__init__(the_window)
        self["relief"] = RAISED
        self["bd"] = 0
        self["bg"] = self.maincolor
        self.but1 = None
        self.but2 = None
        self.headerlabel = Label(self, text=framename, bg=self.secondcolor, fg=self.thirdcolor, font=("Times", 20))
        self.headerlabel.place(x=0, y=0, width=800, height=50)
        self.footerlabel = Label(self, text="Copyright © " + str(datetime.datetime.now().year) + " Diego Fantino",
                                 bg=self.maincolor, fg="black", font=("Times", 10), anchor="w")
        self.footerlabel.place(x=5, y=370, width=795, height=30)

    def set_button_frames(self, but1, but2):
        self.but1 = but1
        self.but2 = but2


class FirstFrame(BasicFrame):
    def __init__(self, the_window, framename, text1, text2):
        BasicFrame.__init__(self, the_window, framename)

        self.button1 = Button(self, text=text1, command=lambda: show_frame(self, self.but1), bg=self.thirdcolor)
        self.button1.place(x=160, y=110, width=520, height=60)
        self.button2 = tkinter.Button(self, text=text2, command=lambda: show_frame(self, self.but2), bg=self.thirdcolor)
        self.button2.place(x=160, y=180, width=520, height=60)


class MiddleFrame(FirstFrame):
    def __init__(self, the_window, framename, text1, text2):
        FirstFrame.__init__(self, the_window, framename, text1, text2)
        self.button3 = Button(self, text="zurück", command=lambda: show_frame(self, framemain), bg=self.thirdcolor)
        self.button3.place(x=160, y=250, width=520, height=60)


class LastFrame(BasicFrame):
    def __init__(self, the_window, framename, text1, text2, text3, text4):
        BasicFrame.__init__(self, the_window, framename)
        self.label1 = tkinter.Label(self, text=text1, bg=self.maincolor, anchor='e')
        self.label1.place(x=160, y=110, width=200, height=30)
        self.label2 = tkinter.Label(self, text=text2, bg=self.maincolor, anchor='e')
        self.label2.place(x=160, y=160, width=200, height=30)
        self.label3 = tkinter.Label(self, text=text3, bg=self.maincolor, anchor='e')
        self.label3.place(x=160, y=210, width=200, height=30)
        self.entry1 = Entry(self, bg="white")
        self.entry1.place(x=440, y=110, width=200, height=30)
        self.entry2 = Entry(self, bg="white")
        self.entry2.place(x=440, y=160, width=200, height=30)
        self.entry3 = Entry(self, bg="white")
        self.entry3.place(x=440, y=210, width=200, height=30)
        self.button1 = Button(self, text="zurück", command=lambda: show_frame(self, self.but1), bg=self.thirdcolor)
        self.button1.place(x=240, y=280, width=120, height=40)
        self.button2 = Button(self, text=text4,
                              command=lambda: check_but2_command(self.but2, self.entry1.get(), self.entry2.get(),
                                                                 self.entry3.get()), bg=self.thirdcolor)
        self.button2.place(x=440, y=280, width=120, height=40)


# Erstelle Frames

framemain = FirstFrame(window, "Decryptinator", "Datein in anderer Datei verstecken/herauslesen",
                       "Datei verschlüsseln/entschlüsseln")
framemiddle1 = MiddleFrame(window, "Datei in anderer Datei verstecken/herauslesen", "Datei in anderer Datei verstecken",
                           "Datei in anderer Datei herauslesen")
framemiddle2 = MiddleFrame(window, "Datei verschlüsseln/entschlüsseln", "Datei verschlüsseln", "Datei entschlüsseln")
framelast1 = LastFrame(window, "Datei in anderer Datei verstecken", "Name der zu versteckenden Datei: ",
                       "Name des Schlüssels: ", "Name der  Versteckdatei: ", "verstecken")
framelast2 = LastFrame(window, "Datei aus anderer Datei herauslesen", "Name der Ursprungsdatei: ",
                       "Name des Schlüssels: ", "Name der neuen Datei: ", "herauslesen")
framelast3 = LastFrame(window, "Datei verschlüsseln", "Name der Ursprungsdatei: ", "Name des Schlüssels: ",
                       "Name der neuen Datei: ", "verschlüsseln")
framelast4 = LastFrame(window, "Datei entschlüsseln", "Name der Urprungsdatei: ", "Name des Schlüssels: ",
                       "Name der neuen Datei: ", "entschlüsseln")
framemain.set_button_frames(framemiddle1, framemiddle2)
framemiddle1.set_button_frames(framelast1, framelast2)
framemiddle2.set_button_frames(framelast3, framelast4)
framelast1.set_button_frames(framemiddle1, 1)
framelast2.set_button_frames(framemiddle1, 2)
framelast3.set_button_frames(framemiddle2, 3)
framelast4.set_button_frames(framemiddle2, 4)
framemain.grid(row=0, column=0, sticky='nsew')
window.mainloop()
