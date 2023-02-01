import os
import customtkinter
from main import App
from assembler import AssemblerSettings

customtkinter.set_appearance_mode('dark')

class Setup(customtkinter.CTk):

    """ This is the Setup object.
        Used to setup the project's most
        important options at the project
        startup """

    def __init__(self):
        super().__init__()

        # Window settings
        self.title('CodeGenie - Setup')
        self.geometry('550x300')
        self.resizable(False, False)

        # First Spacer
        self.spacer = customtkinter.CTkLabel(self, text='')
        self.spacer.grid(row=0, column=0)

        # Project Title
        self.label_title = customtkinter.CTkLabel(self, text='Project\'s name', font=(None, 18))
        self.label_title.grid(row=1, column=0, pady=5, padx=30)

        self.project_title = customtkinter.CTkEntry(self, placeholder_text='Example: SnapTask', width=200, corner_radius=10, border_color='#5e45a5')
        self.project_title.grid(row=2, column=0, padx=30)

        # Window geometry
        self.label_geometry = customtkinter.CTkLabel(self, text='Window\' geometry', font=(None, 18))
        self.label_geometry.grid(row=1, column=1, pady=5, padx=30)

        self.window_geometry = customtkinter.CTkEntry(self, placeholder_text='Example: 500x400', width=200, corner_radius=10, border_color='#5e45a5')
        self.window_geometry.grid(row=2, column=1, padx=30)

        # Second Spacer
        self.spacer2 = customtkinter.CTkLabel(self, text='')
        self.spacer2.grid(row=3, column=0)

        # Resizable property
        self.label_resizable = customtkinter.CTkLabel(self, text='Resizable (x, y)', font=(None, 18))
        self.label_resizable.grid(row=4, column=0, pady=5, padx=30)

        self.resizable_property = customtkinter.CTkEntry(self, placeholder_text='Example: (True, False)', width=200, corner_radius=10, border_color='#5e45a5')
        self.resizable_property.grid(row=5, column=0, padx=30)

        # Background color
        self.label_background = customtkinter.CTkLabel(self, text='Background Color (hex)', font=(None, 18))
        self.label_background.grid(row=4, column=1, padx=30, pady=5)

        self.background_color = customtkinter.CTkEntry(self, placeholder_text='Example: #2D659C', width=200, corner_radius=10, border_color='#5e45a5')
        self.background_color.grid(row=5, column=1, padx=30)

        # Button to cancel changes
        self.settings_cancel = customtkinter.CTkButton(self, text='Cancel', fg_color='#242424', border_width=2, border_color='#3d2d6c', hover_color='#3d2d6c', width=100, height=35, font=(None, 15), corner_radius=13, command=lambda *args, **kwargs: self.destroy())
        self.settings_cancel.grid(row=6, column=0, sticky='e', pady=40, padx=3)

        # Button to save current settings
        self.settings_save_button = customtkinter.CTkButton(self, text='Save', fg_color='#5e45a5', border_width=2, border_color='#3d2d6c', hover_color='#3d2d6c', width=100, height=35, font=(None, 15), corner_radius=13, command=self.save_settings)
        self.settings_save_button.grid(row=6, column=1, sticky='w', pady=40, padx=3)

    # Save settings and transfer them to the assembler
    def save_settings(self):

        # Create the file to write down the GUI (if it already exists it is first deleted)
        if os.path.exists("code.py"):
            os.remove("code.py")
        open("code.py", "w").close()

        AssemblerSettings(title=self.project_title.get(),
                        geometry=self.window_geometry.get(),
                        resize=self.resizable_property.get(),
                        background=self.background_color.get())

        app = App()
        return self.destroy()

if __name__ == "__main__":
    setup = Setup()
    setup.mainloop()