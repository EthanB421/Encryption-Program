import tkinter as tk

HEIGHT = 700
WIDTH = 500

alphabet = "abcdefghijklmnopqrstuvwxyz "
letterIndex = dict(zip(alphabet, range(len(alphabet))))
indexLetter = dict(zip(range(len(alphabet)), alphabet))
#Cipher status allows the user to decide which cipher they want to use
cipherStatus = 0
encryptStatus = True
#Toggle button for the cesar cipher
vigenereStatus = True
cesarStatus = True
playfairStatus = True

def decryptStaging():
    global encryptStatus
    encryptStatus = False
    finalMessage()

def cesarEncrypt(plaintext, shift=3):
    cipher = ''

    for letter in plaintext:
        index = ((letterIndex[letter] + shift) % len(alphabet))
        cipherLetter = indexLetter[index]
        cipher += cipherLetter  
    result['text'] = cipher     
 
def cesarDecrypt(ciphertext, shift=-3):
    global encryptStatus
    encryptStatus = 3
    uncipher = ''
    for letter in ciphertext:
        index = ((letterIndex[letter] + shift) % len(alphabet))
        cipherLetter = indexLetter[index]
        uncipher += cipherLetter  
    result['text'] = uncipher     

def vigenere():
    global vigenereStatus
    if vigenereStatus:
        vigenereStatus = False
        vigenereButton.config(image = vOn)
        print("vigenere is  online")
        global cipherStatus
        cipherStatus = 1
    else:
        cipherStatus = 0
        vigenereStatus = True
        vigenereButton.config(image = vOff)
        print("vigenere is offline")

def playfair():
    global playfairStatus
    if playfairStatus:
        global cipherStatus
        cipherStatus = 2
        playfairStatus = False
        playfairButton.config(image = pOn)
        print("playfair is  online")
    else:
        cipherStatus = 0
        playfairStatus = True
        playfairButton.config(image = pOff)
        print("playfair is offline")

def cesars():
    global cesarStatus
    if cesarStatus:
        global cipherStatus
        cipherStatus = 3
        cesarStatus = False
        cesarButton.config(image = cOn)
    else:
        cipherStatus = 0
        cesarStatus = True
        cesarButton.config(image = cOff)

def finalMessage():
    if(cipherStatus == 1) and (encryptStatus == False):
        result['text'] = "i am inside vigenere"
    elif (cipherStatus == 2) and (encryptStatus == False):
        result['text'] = "i am inside playfair"
    elif (cipherStatus == 3) and (encryptStatus == False):
        cesarDecrypt(entry.get())
    elif (cipherStatus == 1)and (encryptStatus):
        print(cipherStatus)
    elif (cipherStatus == 2) and (encryptStatus):
        print(cipherStatus)
    elif (cipherStatus == 3) and (encryptStatus):
        cesarEncrypt(entry.get())

#Front-end GUI
root =tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="#8ae6c1")
frame.place(relwidth=1, relheight=1)

#Cesar's cipher toggle button
cesarButton = tk.Button(frame, text = "Cesar's Cipher",bg='#8ac4e6', font=15, command=lambda: cesars())
cesarButton.place(relx= 0.09, rely = 0.05, relwidth = 0.25, relheight=0.05)
#Playfair cipher toggle button
playfairButton = tk.Button(frame, text = "Playfair Cipher",bg='#8ac4e6', font=15, command=lambda: playfair())
playfairButton.place(relx= 0.37, rely = 0.05, relwidth = 0.25, relheight=0.05)
#Vigenere cipher toggle button
vigenereButton = tk.Button(frame, text = "Vigenère Cipher",bg='#8ac4e6', font=15, command=lambda: vigenere())
vigenereButton.place(relx= 0.65, rely = 0.05, relwidth = 0.25, relheight=0.05)
#Encrypt button
encrypt = tk.Button(frame, text="Encrypt", bg='#8ac4e6', font=15, command=lambda: finalMessage())
encrypt.place(relx=0.67, rely=0.15, relwidth=0.15, relheight=0.08)
#Decrypt button
decrypt = tk.Button(frame, text="Decrypt", bg='#8ac4e6', font=15, command= lambda: decryptStaging())
decrypt.place(relx=0.82, rely=0.15, relwidth=0.15, relheight=0.08)
#Key entry
key = tk.Entry(frame, bg="#8ac4e6")
key.place(relx=0.22, rely=0.35, relwidth=0.45, relheight=0.08)
#Entry
entry = tk.Entry(frame, bg="#8ac4e6")
entry.place(relx=0.22, rely=0.15, relwidth=0.45, relheight=0.08)
#Key LABEL
labelKey = tk.Label(frame, text = "Key", font = 24, bg="#8ae6c1")
labelKey.place(relx=0.1, rely=0.3, relwidth=.3)
#Final output label
result = tk.Label(frame, bg="#8ac4e6",fg="white", font=('Times New Roman', 28))
result.place(relx=0, rely=0.5, relwidth=1, relheight=0.3)

#Vigenere button toggled image
vOn = tk.PhotoImage(file = "vToggled.png")
vOff = tk.PhotoImage(file = "vUntoggled.png")
#Cesar button toggled image
cOn = tk.PhotoImage(file = "cToggled.png")
cOff = tk.PhotoImage(file = "cUntoggled")
#Playfair button toggled image
pOn = tk.PhotoImage(file = "pToggled.png")
pOff = tk.PhotoImage(file = "pUntoggled.png")

root.mainloop()