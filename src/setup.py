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

        # Used to avoid writing repetitive code for the labels
        list_of_labels = [
                            ['Project\'s name', 1, 0],
                            ['Window\'s geometry', 1, 1],
                            ['Resizable (x, y)', 4, 0],
                            ['Background color (hex)', 4, 1]
                        ]

        # Spacers
        c = 3
        while c >= 0:
            self.spacer = customtkinter.CTkLabel(self, text='')
            self.spacer.grid(row=c, column=0)
            c -= 3

        # Labels
        for i in range(len(list_of_labels)):
            self.label = customtkinter.CTkLabel(self,
                                                text=list_of_labels[i][0],
                                                font=(None, 18))
            self.label.grid(row=list_of_labels[i][1], column=list_of_labels[i][2], pady=5, padx=30)

        # Name of the project
        self.project_title = customtkinter.CTkEntry(self,
                                                placeholder_text='Example: SnapTask',
                                                width=200, corner_radius=10,
                                                border_color='#5e45a5')
        self.project_title.grid(row=2, column=0, padx=30)

        # Dimensions of the window
        self.window_geometry = customtkinter.CTkEntry(self,
                                                placeholder_text='Example: 500x400',
                                                width=200,
                                                corner_radius=10,
                                                border_color='#5e45a5')
        self.window_geometry.grid(row=2, column=1, padx=30)

        # Resizability of the window
        self.resizable_property = customtkinter.CTkEntry(self, 
                                                placeholder_text='Example: True, False',
                                                width=200,
                                                corner_radius=10,
                                                border_color='#5e45a5')
        self.resizable_property.grid(row=5, column=0, padx=30)

        # Background color of the window
        self.background_color = customtkinter.CTkEntry(self,
                                                placeholder_text='Example: #2D659C',
                                                width=200,
                                                corner_radius=10,
                                                border_color='#5e45a5')
        self.background_color.grid(row=5, column=1, padx=30)

        # Button to cancel changes
        self.settings_cancel = customtkinter.CTkButton(self,
                                                text='Cancel',
                                                fg_color='#242424',
                                                border_width=2,
                                                border_color='#3d2d6c',
                                                hover_color='#3d2d6c',
                                                width=100,
                                                height=35,
                                                font=(None, 15),
                                                corner_radius=13,
                                                command=lambda *args, **kwargs: self.destroy())
        self.settings_cancel.grid(row=6, column=0, sticky='e', pady=40, padx=3)

        # Button to save current settings
        self.settings_save_button = customtkinter.CTkButton(self,
                                                text='Save',
                                                fg_color='#5e45a5',
                                                border_width=2,
                                                border_color='#3d2d6c',
                                                hover_color='#3d2d6c',
                                                width=100,
                                                height=35,
                                                font=(None, 15),
                                                corner_radius=13,
                                                command=self.save_settings)
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

        app = App(title=self.project_title.get(), background=self.background_color.get())
        return self.destroy()

if __name__ == "__main__":
    setup = Setup()
    setup.mainloop()