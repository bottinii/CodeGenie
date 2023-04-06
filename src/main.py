
# Libraries
import tkinter
import customtkinter
import tkinter.messagebox as MsB
from PIL import Image

# My classes
from pages.profilePage import Profile

# Library settings
customtkinter.set_appearance_mode('dark')
customtkinter.deactivate_automatic_dpi_awareness()

# Main window object
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Window settings
        self.title("CodeGenie - Home")
        self.geometry("800x500")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.deleteWindow)

        # Column configuration
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)

        self.segButtonValues = [
                                    "Window", "Frame", "Label",
                                    "Button", "Entry", "Seg-Button",
                                    "Combo-Box","Check-Box", "Radio-Button"
                                ]

        self.landingPage()

    # This function creates the home page widgets
    def landingPage(self):
        for i in self.winfo_children():
            i.destroy()

        self.profile = customtkinter.CTkImage(Image.open("./img/user.png"), size=(25, 25))
        self.profileButton = customtkinter.CTkButton(self,
                                                  image=self.profile,
                                                  text='',
                                                  fg_color="#242424",
                                                  hover_color="#242424",
                                                  width=0, 
                                                  height=0,
                                                  command=Profile)
        self.profileButton.grid(column=0, row=0, pady=10, padx=20)

        self.mainSegementedButton = customtkinter.CTkSegmentedButton(self,
                                                                     fg_color="#B491FF",
                                                                     selected_color="#6333AD",
                                                                     selected_hover_color="#5422A0",
                                                                     unselected_color="#925FFF",
                                                                     unselected_hover_color="#6333AD",
                                                                     values=self.segButtonValues,
                                                                     command=self.createWidget)
        self.mainSegementedButton.grid(row=0, column=1)

        self.download = customtkinter.CTkImage(Image.open("./img/download.png"), size=(28, 28))
        self.downloadButton = customtkinter.CTkButton(self,
                                                  image=self.download,
                                                  text='',
                                                  fg_color="#242424",
                                                  hover_color="#242424",
                                                  width=0, 
                                                  height=0)
        self.downloadButton.grid(column=2, row=0, pady=10, padx=20)

        self.previewFrame = customtkinter.CTkFrame(self,
                                                corner_radius=25,
                                                fg_color="#242424",
                                                border_color="#B491FF",
                                                border_width=10,
                                                width=700,
                                                height=400)
        self.previewFrame.grid(column=1, row=1, pady=15)

    # Creates the widgets in the segmented button used to create the UI
    def createWidget(self, widget):
        match widget:
            case "Window": return 0
            case "Frame": return 0

    # Callback for the WM_DELETE_WINDOW protocol
    def deleteWindow(self):
        if (MsB.askyesno('Confirm', 'Are you sure that you want to quit?')):
            return self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()