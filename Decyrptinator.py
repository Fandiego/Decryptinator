import os
import tkinter
import tkinter.messagebox
from tkinter import *

def button_command1():                      #Klasse funktioniert
    global filename1
    filename1 = entry1.get()
    global filename2
    filename2 = entry2.get()
    keygen(filename1, filename2, "")
    return None

def button_command2():                      #Klasse funktioniert
    global filename1
    filename1 = entry1.get()
    global filename2
    filename2 = entry2.get()
    filename3 = entry3.get()
    decrypt(filename1, filename2, filename3)
    return None

def button_command3():                      #Klasse funktioniert
    global filename1
    filename1 = entry1.get()
    encrypt(filename1)
    return None

def button_command4():                      #Klasse funktioniert
    global filename1
    filename1 = entry1.get()
    global filename2
    filename2 = entry2.get()
    decrypt2(filename1, filename2)
    return None

def equalize(path_1, path_2):               #Klasse funktioniert
    dat1 = open(path_1, "rb").read()
    dat2 = open(path_2, "rb").read()
    l_dat1 = len(dat1)
    l_dat2 = len(dat2)
    if l_dat1 > l_dat2:
        dat2 += os.urandom(l_dat1 - l_dat2)
    else:
        dat1 += os.urandom(l_dat2 - l_dat1)
    with open(path_1, "wb") as out:
        out.write(dat1)
    with open (path_2, "wb") as out:
        out.write(dat2)

def keygen(orig_path, enc_path, key_path):  #Klasse funktioniert
    equalize(orig_path, enc_path)
    original = open(orig_path, "rb").read()
    encrypted = open(enc_path, "rb").read()
    key = bytes(a ^ b for (a, b) in zip(original, encrypted))
    with open(key_path + "enc.key", "wb") as key_out:
        key_out.write(key)

def decrypt(enc_path, key_path, dec_path):  #Klasse funktioniert
    encrypted = open(enc_path, "rb").read()
    key = open(key_path, "rb").read()
    decrypted = bytes(a ^ b for (a, b) in zip(encrypted, key))
    with open(dec_path, "wb") as decrypted_out:
        decrypted_out.write(decrypted)

def encrypt(filename):                      #Klasse funktioniert
    to_encrypt = open(filename, "rb").read()
    size = len(to_encrypt)
    key = os.urandom(size)
    with open(filename + ".key" , "wb") as key_out:
        key_out.write(key)
    encrypted = bytes(a ^ b for (a, b) in zip(to_encrypt, key))
    with open(filename, "wb") as encrypted_out:
        encrypted_out.write(encrypted)

def decrypt2(filename, key):                #Klasse funktioniert
    file = open(filename, "rb").read()
    key = open(key, "rb").read()
    decrypted = bytes(a ^ b for (a, b) in zip(file, key))
    with open("entschlüsselt_" + filename, "wb") as decrypted_out:
        decrypted_out.write(decrypted)

def but1():                                 #Klasse funktioniert
    root.destroy()
    global but1root
    but1root = tkinter.Tk()
    but1root.title("Datei als neue Datei verschlüsseln/entschlüsseln")
    but1root.geometry("1200x500")
    but1root.configure(bg="black")
    button1 = tkinter.Button(but1root, text="verschlüsseln",command=but1encrypt, height=2, width=100, bg="grey").place(x="20", y="20")
    button2 = tkinter.Button(but1root, text="entschlüsseln",command=but1decrypt, height=2, width=100, bg="grey").place(x="20", y="60")
    but1root.mainloop()

def but1encrypt():                          #Klasse funktioniert
    but1root.destroy()
    but1encrypt = tkinter.Tk()
    but1encrypt.title("Datei verschlüsseln")
    but1encrypt.geometry("1200x500")
    but1encrypt.configure(bg="black")
    Label(but1encrypt, text="Name der Ursprung Datei: ", bg="black", fg="grey").grid(row=0, column=0)
    Label(but1encrypt, text="Name der Verschlüsstelten Datei: ",  bg="black", fg="grey").grid(row=1, column=0)
    global entry1
    entry1 = Entry(but1encrypt, width = 20, bg="grey")
    entry1.grid(row=0, column=1)
    global entry2
    entry2 = Entry(but1encrypt, width = 20, bg="grey")
    entry2.grid(row=1, column=1)
    Button(but1encrypt, text="verschlüsseln", command=button_command1, height=2, width=17, bg="grey").grid(row=2, column=1)
    but1encrypt.mainloop()

def but1decrypt():                          #Klasse funktioniert
    but1root.destroy()
    but1decrypt = tkinter.Tk()
    but1decrypt.title("Datei entschlüsseln")
    but1decrypt.geometry("1200x500")
    but1decrypt.configure(bg="black")
    Label(but1decrypt, text="Name der zu entschlüsselnden Datei: ", bg="black", fg="grey").grid(row=0, column=0)
    Label(but1decrypt, text="Name des Schlüssels: ",  bg="black", fg="grey").grid(row=1, column=0)
    Label(but1decrypt, text="Name der neuen Datei: ",  bg="black", fg="grey").grid(row=2, column=0)
    global entry1
    entry1 = Entry(but1decrypt, width = 20, bg="grey")
    entry1.grid(row=0, column=1)
    global entry2
    entry2 = Entry(but1decrypt, width = 20, bg="grey")
    entry2.grid(row=1, column=1)
    global entry3
    entry3 = Entry(but1decrypt, width = 20, bg="grey")
    entry3.grid(row=2, column=1)
    Button(but1decrypt, text="entschlüsseln", command=button_command2, height=2, width=17, bg="grey").grid(row=3, column=1)
    but1decrypt.mainloop()

def but2():                                 #Klasse funktioniert
    root.destroy()
    global but2root
    but2root = tkinter.Tk()
    but2root.title("Datei verschlüsseln/entschlüsseln")
    but2root.geometry("1200x500")
    but2root.configure(bg="black")
    button1 = tkinter.Button(but2root, text="verschlüsseln",command=but2encrypt, height=2, width=100, bg="grey").place(x="20", y="20")
    button2 = tkinter.Button(but2root, text="entschlüsseln",command=but2decrypt, height=2, width=100, bg="grey").place(x="20", y="60")
    but2root.mainloop()

def but2encrypt():                          #Klasse funktioniert
    but2root.destroy()
    but2encrypt = tkinter.Tk()
    but2encrypt.title("Datei verschlüsseln")
    but2encrypt.geometry("1200x500")
    but2encrypt.configure(bg="black")
    Label(but2encrypt, text="Name der zu Verschlüsselnden Datei: ",  bg="black", fg="grey").grid(row=0, column=0)
    global entry1
    entry1 = Entry(but2encrypt, width = 20, bg="grey")
    entry1.grid(row=0, column=1)
    Button(but2encrypt, text="verschlüsseln", command=button_command3, height=2, width=17, bg="grey").grid(row=1, column=1)
    but2encrypt.mainloop()

def but2decrypt():                          #Klasse funktioniert
    but2root.destroy()
    but2edecrypt = tkinter.Tk()
    but2edecrypt.title("Datei entschlüsseln")
    but2edecrypt.geometry("1200x500")
    but2edecrypt.configure(bg="black")
    Label(but2edecrypt, text="Name der zu entschlüsselnden Datei: ", bg="black", fg="grey").grid(row=0, column=0)
    Label(but2edecrypt, text="Name des Schlüssels: ",  bg="black", fg="grey").grid(row=1, column=0)
    global entry1
    entry1 = Entry(but2edecrypt, width = 20, bg="grey")
    entry1.grid(row=0, column=1)
    global entry2
    entry2 = Entry(but2edecrypt, width = 20, bg="grey")
    entry2.grid(row=1, column=1)
    Button(but2edecrypt, text="entschlüsseln", command=button_command4, height=2, width=17, bg="grey").grid(row=2, column=1)
    but2edecrypt.mainloop()

# Main                                      #Klasse funktioniert
root = tkinter.Tk()
root.title("Decryptinator")
root.geometry("1200x500")
root.configure(bg="black")
firstbutton = tkinter.Button(root, text="Datei als neue Datei verschlüsseln/entschlüsseln",command=but1, height=2, width=100, bg="grey").place(x="20", y="20")
secondbutton = tkinter.Button(root, text="Datei verschlüsseln/entschlüsseln",command=but2, height=2, width=100, bg="grey").place(x="20", y="60")
root.mainloop()








