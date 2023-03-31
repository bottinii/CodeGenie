import customtkinter
from tkinter import *

customtkinter.set_appearance_mode('dark')

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("CodeGenie - Home")
        self.geometry("750x450")
        self.resizable(False, False)

if __name__ == "__main__":
    app = App()
    app.mainloop()