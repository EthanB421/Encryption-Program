import tkinter as tk

HEIGHT = 700
WIDTH = 500

#Toggle button for the cesar cipher
vigenereStatus = True
cesarStatus = True
playfairStatus = True

def vigenere():
    global vigenereStatus
    if vigenereStatus:
        vigenereStatus = False
        vigenereButton.config(image = vOn)
        print("vigenere is  online")
    else:
        vigenereStatus = True
        vigenereButton.config(image = vOff)
        print("vigenere is offline")

def playfair():
    global playfairStatus
    if playfairStatus:
        playfairStatus = False
        playfairButton.config(image = pOn)
        print("playfair is  online")
    else:
        playfairStatus = True
        playfairButton.config(image = pOff)
        print("playfair is offline")

def cesars():
    global cesarStatus
    if cesarStatus:
        cesarStatus = False
        cesarButton.config(image = cOn)
        print("I am online")
    else:
        cesarStatus = True
        cesarButton.config(image = cOff)
        print("I am offline")


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
encrypt = tk.Button(frame, text="Encrypt", bg='#8ac4e6', font=15, command=lambda: cesars(entry.get()))
encrypt.place(relx=0.67, rely=0.15, relwidth=0.15, relheight=0.08)
#Decrypt button
decrypt = tk.Button(frame, text="Decrypt", bg='#8ac4e6', font=15, command=lambda: cesars(entry.get()))
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