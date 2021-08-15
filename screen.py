import tkinter
import os

mainwindow = tkinter.Tk()

mainwindow.title("Hello world")
mainwindow.geometry("640x480+8+100")

label = tkinter.Label(mainwindow, text='My Codes')
label.grid(row=0, column=0, columnspan=3)

mainwindow.columnconfigure(0, weight=1)
mainwindow.columnconfigure(1, weight=1)
mainwindow.columnconfigure(2, weight=3)
mainwindow.columnconfigure(3, weight=3)
mainwindow.columnconfigure(4, weight=3)

mainwindow.rowconfigure(0, weight=1)
mainwindow.rowconfigure(1, weight=1)
mainwindow.rowconfigure(2, weight=3)
mainwindow.rowconfigure(3, weight=3)
mainwindow.rowconfigure(4, weight=3)

fileList = tkinter.Listbox(mainwindow)
fileList.grid(row=1, column=0, rowspan=2, sticky='news')
fileList.configure(borderwidth=2, relief='raised')
for zone in os.listdir('D:\python\Projects'):
    fileList.insert(tkinter.END, zone)





mainwindow.mainloop()
