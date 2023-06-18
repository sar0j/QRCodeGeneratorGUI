from tkinter import*
from tkinter import messagebox
import pyqrcode

tk = Tk()
tk.title("QR Generator")
tk.config(bg = "#3E3E3E")

def generate_QR():
    if len(user_input.get()) != 0:
        global qr, img
        qr = pyqrcode.create(user_input.get())
        img = BitmapImage(data = qr.xbm(scale = 10))
    else:
        messagebox.showwarning('warning', "Fields are required!")
    try:
        display_code()
    except:
        pass

def display_code():
    img_lbl.config(image = img)
    output.config(text = "QR CODE : "+user_input.get())

lbl = Label(tk, text = "Enter TEXT or URL", bg = "#FFFFFF", padx = 30, pady = 20, font = ("Courier", 30))
lbl.pack()

user_input = StringVar()
entry = Entry(tk, textvariable = user_input, width = 50, font = ("ariel", 15))
entry.pack(padx = 50, pady = 30)

button = Button(tk, text = "Generate QR", width = 20, command = generate_QR, font = ("ariel", 15))
button.pack(padx = 10, pady = 10)

img_lbl = Label(tk, bg = "#FFFFFF")
img_lbl.pack()

output = Label(tk, text = "", bg = "#DDDDDD")
output.pack()

tk.mainloop()
