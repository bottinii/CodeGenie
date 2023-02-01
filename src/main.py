import customtkinter

customtkinter.set_appearance_mode('dark')

class App(customtkinter.CTk):

    """ This is the frontend file where is also
        used the assembled.py file to return the
        generated code """

    def __init__(self):
        super().__init__()

        # Window settings
        self.title('CodeGenie')
        self.geometry('700x450')
        self.resizable(False, False)

        # Landing page
        self.navbar = customtkinter.CTkSegmentedButton(self,
                                                values=["Settings", "Frame", "Label", "Button", "Input", "Switch", "Option-Menu", "CheckBox", "Popup"],
                                                selected_color='#3d2d6c',
                                                selected_hover_color='#3d2d6c',
                                                unselected_hover_color='#5e45a5')
        self.navbar.pack(padx=20, pady=10)

        self.preview()

    # GUI preview
    def preview(self):
        self.fake_preview_frame = customtkinter.CTkFrame(self, width=550, height=350, corner_radius=25, border_color='#5e45a5', border_width=3)
        self.fake_preview_frame.pack(expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()