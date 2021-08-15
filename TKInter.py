import tkinter
mainwindow = tkinter.Tk()
mainwindow.title("Hello world")
mainwindow.geometry("640x480+8+100")
lable = tkinter.Label(mainwindow, text="Hello World")
lable.pack(side="top")
# ".pack is a geometry manager
# more pack option "side,fill,expand"
# fill must be Y,X,BOTH
# expand = TRUE or FALSE
leftframe = tkinter.Frame(mainwindow)
leftframe.pack(side='left', anchor='n', expand=False)
# Anchors are used to define where text is positioned relative to a reference point.
# they are n,s,e,w,CENTRE
canvas = tkinter.Canvas(leftframe, relief='raised', borderwidth=5)
# The Canvas is a rectangular area intended for drawing pictures or other complex layouts.
# for canvas https://www.tutorialspoint.com/python/tk_canvas.htm#:~:text=Advertisements,or%20frames%20on%20a%20Canvas.
# relief must be flat, groove, raised, ridge, solid, sunken
canvas.pack(side='left')
# side must be top,bottom,left,right
rightframe = tkinter.Frame(mainwindow)
rightframe.pack(side='right', anchor='n', expand=False)
button1 = tkinter.Button(mainwindow, text='Start')
button2 = tkinter.Button(mainwindow, text='Stop')
button1.pack(side='top')
button2.pack(side='top')
mainwindow.mainloop()
