from Tkinter import *
from email.mime import image
tk = Tk()
canvas = Canvas(tk, width = 400, height = 400)
canvas.pack()
my_image = PhotoImage(file = 'C:\Users\Usuario\Dropbox\Python sricpts & software\Show Image\ProfilePic.gif')
canvas.create_image(0,0, anchor = NW, image = my_image)