class AssemblerSettings:

    """ This is the Assembler object.
        It is necessary to store all the
        data entered by the user and to create
        the actual GUI """

    def __init__(self, title, geometry, resize, background):
        
        # Stored data
        self.titleProject = title
        self.geometryProject = geometry
        self.resizeProject = resize
        self.backgroundProject = background

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
        self.title('{self.titleProject}')
        self.geometry('{self.geometryProject}')
        self.resizable({self.resizeProject})
        self.configure(fg_color='{self.backgroundProject}')""")
            
            code.close()