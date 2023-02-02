
""" This is the Assembler object.
    It is necessary to store all the
    data entered by the user and to create
    the actual GUI """

class AssemblerSettings:
    def __init__(self, title, geometry, resize, background):
        
        # Stored data
        self.titleProject = title
        self.geometryProject = geometry
        self.resizeProject = resize
        self.backgroundProject = background

        # Initialize settings in GUI code
        with open("code.py", "w") as self.code:
            self.code.write(f"""
# Used libraries
import customtkinter

# Class used to display the entire GUI
class Gui(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Initialize window's settings
        self.title('{self.titleProject}')
        self.geometry('{self.geometryProject}')
        self.resizable({self.resizeProject})
        self.configure(fg_color='{self.backgroundProject}')
        self.grid_columnconfigure(0, weight=1)

        # Widgets:
        """)
            
            self.code.close()

class AssemblerFrame:
    def __init__(self, parent, name, size, background, border, radius, column, row, padx, pady):
        
        # Stored data
        self.parentFrame = parent
        self.nameFrame = name
        self.sizeFrame = size.split('x')
        self.backgroundFrame = background
        self.borderFrame = border
        self.radiusFrame = radius
        self.columnFrame = column
        self.rowFrame = row
        self.padxFrame = padx
        self.padyFrame = pady

        # Add frame to the code
        with open("code.py", "a") as self.code:
            self.code.write(f"""
        self.{self.nameFrame} = customtkinter.CTkFrame(master={self.parentFrame}, width={self.sizeFrame[0]}, height={self.sizeFrame[1]}, fg_color='{self.backgroundFrame}', border_width=3, border_color='{self.borderFrame}', corner_radius={self.radiusFrame})
        self.{self.nameFrame}.grid(column={self.columnFrame}, row={self.rowFrame}, padx={self.padxFrame}, pady={self.padyFrame})""")   

        self.code.close()     