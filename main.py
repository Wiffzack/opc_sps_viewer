import os,sys
from shutil import which
from tkinter import *
from tkinter.ttk import *

root = Tk()

class Window(Frame):

    def openNewWindow(self):
     
        # Toplevel object which will 
        # be treated as a new window
        newWindow = Toplevel(root)

        # sets the title of the
        # Toplevel widget
        newWindow.title("Settings")

        # sets the geometry of toplevel
        newWindow.geometry("200x800")

        # A Label widget to show in toplevel
        Label(newWindow, 
                text ="This is a new window").pack()


    def check_openssl():
        return which("openssl")

    def create_cert(self):
        os.system("openssl genrsa -out key.pem 2048 ")
        os.system("openssl req -x509 -days 365 -new -out certificate.pem -key key.pem -config ssl.conf")

    def __init__(self, master=None):
        Frame.__init__(self, master)   
        print ("Main frame started")  
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
        certButton = Button(self, text="Create Certificate", command=self.create_cert)
        if(self.check_openssl == None):
            certButton["state"] = "disabled"
        certButton.place(x=5, y=5)

        settings = Button(self, text="New window", command=self.openNewWindow)
        settings.place(x=5, y=50)        

    def clickExitButton(self):
        exit()
        
app = Window(root)
root.wm_title("Tkinter button")
root.geometry("800x600")
root.mainloop()