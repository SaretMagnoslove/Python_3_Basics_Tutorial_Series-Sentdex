from tkinter import *
from PIL import Image, ImageTk #for handling images
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
        # defining menu bar
        menu = Menu(self.master)
        self.master.config(menu=menu)
        # adding a menu bar: File->Exit and File->Save
        file = Menu(menu)
        file.add_command(label='Save', command = self.client_exit)
        file.add_command(label='Exit', command = self.client_exit)
        menu.add_cascade(label='File', menu=file)
        # adding a menu bar Edit->Undo
        edit = Menu(menu)
        edit.add_command(label='Show Image', command=self.showImg)
        edit.add_command(label='Show Text', command=self.showTxt)
        menu.add_cascade(label='Edit', menu=edit)
    #adding the function for quitting the window
    def client_exit(self):
        exit()
    # defining a function for showing images
    def showImg(self):
        load = Image.open('pic.jpg')
        render = ImageTk.PhotoImage(load)
        # labeling the image
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
    # defining a function for showing text
    def showTxt(self):
        text = Label(self, text='The Witches and the Grinnygog')
        text.pack()
        
root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()