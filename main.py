import os,sys
from shutil import which
from tkinter import *
from tkinter.ttk import *

root = Tk()

# First add grafana and prometheus 
# later maybe mongodb postgres etc ...
def okay(text):
    print ("sdsf")
    print (text)

class NewWindow(Toplevel):
    
    def __init__(self, master = None):
        
        super().__init__(master = master)
        self.title("New Window")
        self.geometry("200x200")
        label = Label(self, text ="This is a new Window")
        label.pack()
        e = Entry(self)
        e.pack()
        e.place(x=5, y=50) 
        e.focus_set()
        b = Button(self,text='finish',command=lambda: okay((e.get())))
        b.place(x=5, y=100) 
        b.bind('<Return>', okay)

class Window(Frame):

    def print_text(self,e):
        print ("called")
        print (e.get())

    def replace_ip(self,node_ip="192.168.0.1"):
        replacements = {'placeholder_ip':node_ip}

        with open('ssl.conf') as infile, open('ssl.conf', 'w') as outfile:
            for line in infile:
                for src, target in replacements.items():
                    line = line.replace(src, target)
                outfile.write(line)
            
    def return_pressed(event):
        print('Return key pressed.')

    def createOPCServer(self):
        # Toplevel object which will 
        # be treated as a new window
        newWindow = Toplevel(root)
        # sets the title of the
        # Toplevel widget
        newWindow.title("Settings")
        # sets the geometry of toplevel
        newWindow.geometry("200x600")
        e = Entry(newWindow)
        e.pack()
        e.place(x=5, y=50) 
        e.focus_set()
        b = Button(newWindow,text='finish',command=print(e.get()))
        b.bind('<Return>', self.return_pressed)
        #b.pack(side='bottom')
        b.place(x=5, y=100) 
        # A Label widget to show in toplevel

    
        Label(newWindow, 
                text ="OPC Server Settings").pack()

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
        fileMenu.add_command(label="Add OPC Server",  command=self.createOPCServer)
        fileMenu.add_command(label="Add OPC Client",  command=self.createOPCServer)
        menu.add_cascade(label="File", menu=fileMenu)

        editMenu = Menu(menu)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")
        menu.add_cascade(label="Edit", menu=editMenu)
        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        opserver = Button(self, text="Add OPC Server", command=self.createOPCServer)
        opserver.place(x=5, y=25) 

        opcclient = Button(self, text="Add OPC Client", command=self.createOPCServer)
        opcclient.place(x=5, y=50)  

        btn = Button(root, text ="Click to open a new window")
        btn.bind("<Button>", lambda e: NewWindow(root))    
        btn.place(x=5, y=75)  
        btn.pack(pady = 10)

        # create button, link it to clickExitButton()
        """         certButton = Button(self, text="Create Certificate", command=self.create_cert)
        if(self.check_openssl == None):
        certButton["state"] = "disabled"
        certButton.place(x=5, y=5)

        settings = Button(self, text="New window", command=self.openNewWindow)
        settings.place(x=5, y=50)   """      

    def clickExitButton(self):
        exit()
        
app = Window(root)
root.wm_title("Tkinter button")
root.geometry("800x600")
root.mainloop()