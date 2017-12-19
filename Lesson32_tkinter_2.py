from tkinter import *
# now for creating the window
class Window(Frame):

    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        # initializing the window
        self.master.title ('GUI') #adding title
        self.pack(fill=BOTH, expand=1) # expand option
        # adding a quit botton
        quitButton = Button(self, text='Quit')
        quitButton.place(x=0, y=0)


root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()