import customtkinter
from widgets.frame import Frame

customtkinter.set_appearance_mode('dark')

class App(customtkinter.CTk):

    """ This is the main frontend class where is 
        initialized the navbar and the preview
        frame """

    def __init__(self):
        super().__init__()

        # Window settings
        self.title('CodeGenie - Build')
        self.geometry('700x450')
        self.resizable(False, False)

        # Landing page
        self.navbar = customtkinter.CTkSegmentedButton(self,
                                                values=["Frame", "Label", "Button", "Input", "Switch", "Option-Menu", "CheckBox", "Popup"],
                                                command=self.navbar_callback,
                                                selected_color='#3d2d6c',
                                                selected_hover_color='#3d2d6c',
                                                unselected_hover_color='#5e45a5')
        self.navbar.pack(padx=20, pady=10)

        self.preview()

    # Callback of each button in the navbar
    def navbar_callback(self, button):
        if button.lower() == 'frame': return Frame()

    # GUI preview
    def preview(self):

        # Fake preview frame only for aesthetic purpose
        self.fake_preview_frame = customtkinter.CTkFrame(self,
                                                corner_radius=25,
                                                border_color='#5e45a5',
                                                border_width=3)
        self.fake_preview_frame.pack(padx=70, pady=40, expand=True, fill='both')

        # The actual frame used to preview the interface
        self.actual_preview_frame = customtkinter.CTkFrame(self.fake_preview_frame,
                                                width=540,
                                                height=300,
                                                corner_radius=0,
                                                fg_color='#2b2b2b')
        self.actual_preview_frame.pack(expand=True)