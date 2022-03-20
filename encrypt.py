import tkinter as tk

HEIGHT = 700
WIDTH = 500

#Toggle button for the cesar cipher
cesarStatus = True
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
cesarButton.place(relx= 0.03, rely = 0.05, relwidth = 0.25, relheight=0.05)
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

#Cesar button toggled image
cOn = tk.PhotoImage(file = "cToggled.png")
cOff = tk.PhotoImage(file = "cUntoggled")

root.mainloop()