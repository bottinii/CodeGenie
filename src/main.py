import os
import tkinter.messagebox as MsBx
import customtkinter
from widgets.frame import Frame

customtkinter.set_appearance_mode('dark')

class App(customtkinter.CTk):

    """ This is the main frontend class where is 
        initialized the navbar and the preview
        frame """

    def __init__(self, title, background):
        super().__init__()

        # Stored data
        self.title_preview = title
        self.background_preview = background

        # On closing protocol
        def on_closing():
            if MsBx.askokcancel("Quit", "Your work will be lost. Are you sure you want to exit?"):
                self.destroy()

        # Window settings
        self.title(f'CodeGenie - \'{self.title_preview}\'')
        self.geometry('700x450')
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", on_closing)

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
        
        try:
            # Fake preview frame only for aesthetic purpose
            self.fake_preview_frame = customtkinter.CTkFrame(self,
                                                    fg_color=self.background_preview,
                                                    corner_radius=25,
                                                    border_color='#5e45a5',
                                                    border_width=3)
            self.fake_preview_frame.pack(padx=70, pady=40, expand=True, fill='both')

            # The actual frame used to preview the interface
            self.actual_preview_frame = customtkinter.CTkFrame(self.fake_preview_frame,
                                                fg_color=self.background_preview,
                                                width=540,
                                                height=300,
                                                corner_radius=0)
            self.actual_preview_frame.pack(expand=True)
        
        except Exception as err:
            MsBx.showerror('Error', err)
            os.remove("code.py")
            self.destroy()