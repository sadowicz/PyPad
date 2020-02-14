from TextArea import *
from Menu import *
from Toolbar import *

class PadApp:
    def __init__(self):

        mainWindow = tk.Tk(className=" PyPad")
        mainWindow.state('zoomed')  #start as a fullscreen window

        text = TextArea( mainWindow )


        mainWindow.mainloop()