
import tkinter
import customtkinter

class Gui(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title('alemenec')
        self.geometry('1000x50')
        self.resizable(True, False)
        self.configure(fg_color='blue')
        
Gui().mainloop()