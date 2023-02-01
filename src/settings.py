import customtkinter

class Settings(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()

        # Window settings
        self.title('CodeGenie - Settings')
        self.geometry('550x300')
        self.resizable(False, False)

        # Project Title
        self.customtkinter.CTkLabel(self)