class AssemblerSettings:

    """ This is the Assembler object.
        It is necessary to store all the
        data entered by the user and to create
        the actual GUI """

    def __init__(self, title='CodeGenie - Test App', geometry='600x400', resize='False, False', background='#2b2b2b'):
        
        # Stored data
        self.title = title
        self.geometry = geometry
        self.resize = resize
        self.background = background

        # Initialize settings in GUI code
        with open("code.py", "w") as code:
            code.write(f"""
import tkinter
import customtkinter

class Gui(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title('{self.title}')
        self.geometry('{self.geometry}')
        self.resizable({self.resize})
        self.configure(fg_color='{self.background}')

Gui().mainloop()""")
            
            code.close()