from tkinter import *


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("tkinter GUI App")
        master.geometry('400x200')

        self.label = Label(master, text="Hello! tkinter GUI App", pady=40)
        self.label.pack()

        self.close_button = Button(master, text="Quit", command=master.quit)
        self.close_button.pack()


win = Tk()
my_gui = MyFirstGUI(win)
win.mainloop()
