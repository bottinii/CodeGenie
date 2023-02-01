class AssemblerSettings:

    """ This is the Assembler object.
        It is necessary to store all the
        data entered by the user and to create
        the actual GUI """

    def __init__(self, title='CodeGenie - Test App', geometry='600x400', resize='False, False', background='#2b2b2b'):
        
        # Stored data
        self.title = title
        self.geometry = geometry.split('x')
        self.resize = resize
        self.background = background

        # Initialize settings in GUI code
        with open("code.py", "w") as code:
            code.write(f"""
# Used libraries
import tkinter
import customtkinter

# Class used to display the entire GUI
class Gui(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Initialize window's settings
        self.title('{self.title}')
        self.geometry('{self.geometry[0]}x{self.geometry[1]}')
        self.resizable({self.resize})
        self.configure(fg_color='{self.background}')

        # FIX THIS SHIT NOW!!!!
        self.minsize({int(self.geometry[0]*0.5)}x{int(self.geometry[1]*0.5)})

Gui().mainloop()""")
            
            code.close()