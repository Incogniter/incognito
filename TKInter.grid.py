import tkinter
mainwindow = tkinter.Tk()
mainwindow.title("Hello world")
mainwindow.geometry("640x480+8+100")

lable = tkinter.Label(mainwindow, text="Hello World")
lable.grid(row=0, column=1)

leftframe = tkinter.Frame(mainwindow)
leftframe.grid(row=1, column=1)
canvas = tkinter.Canvas(leftframe, relief='raised', borderwidth=5)
canvas.grid(row=1, column=0)

rightframe = tkinter.Frame(mainwindow)
rightframe.grid(row=1, column=2, sticky='n')
button1 = tkinter.Button(rightframe, text='Start')
button2 = tkinter.Button(rightframe, text='Stop')
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)

# configure the columns
mainwindow.columnconfigure(0, weight=1)
mainwindow.columnconfigure(1, weight=1)
mainwindow.grid_columnconfigure(2, weight=1)

leftframe.config(relief='sunken', borderwidth=1)
rightframe.config(relief='sunken', borderwidth=1)
leftframe.grid(sticky='ns')
rightframe.grid(sticky='new')
#
rightframe.columnconfigure(0, weight=1)
button1.grid(sticky='we')
button2.grid(sticky='we')

mainwindow.mainloop()
