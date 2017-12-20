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
        # adding a quit botton with event handling using command
        quitButton = Button(self, text='Quit', command=self.client_exit)
        quitButton.place(x=0, y=0)
    #adding the function for quitting the window
    def client_exit(self):
        exit()

root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()