from tkinter import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master


        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Item")
        #fileMenu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="File", menu=fileMenu)

        editMenu = Menu(menu)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")
        menu.add_cascade(label="Edit", menu=editMenu)
        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # create button, link it to clickExitButton()
        exitButton = Button(self, text="Exit", command=self.clickExitButton)

        # place button at (0,0)
        exitButton.place(x=5, y=5)

    def clickExitButton(self):
        exit()
        
root = Tk()
app = Window(root)
root.wm_title("Tkinter button")
root.geometry("320x200")
root.mainloop()