import customtkinter

class Frame(customtkinter.CTk):

    """ This is the Frame object. It
        is used to create new frames and
        to add them to the code """

    def __init__(self):
        super().__init__()

        # Window's settings
        self.title('CodeGenie - Frame')
        self.geometry('550x300')
        self.resizable(False, False)

        # Used to avoid writing repetitive code for the labels
        list_of_labels = [
                            ['Frame\'s name', 1, 0],
                            ['Frame\'s dimensions', 1, 1],
                            ['Background color', 4, 0],
                            ['Border color', 4, 1]
                        ]

        # First Spacer
        self.spacer = customtkinter.CTkLabel(self, text='')
        self.spacer.grid(row=0, column=0)

        # Second Spacer
        self.spacer = customtkinter.CTkLabel(self, text='')
        self.spacer.grid(row=3, column=0)

        # Lables
        for i in range(len(list_of_labels)):
            self.label = customtkinter.CTkLabel(self,
                                                text=list_of_labels[i][0],
                                                font=(None, 18))
            self.label.grid(row=list_of_labels[i][1], column=list_of_labels[i][2], pady=5, padx=30)

        # Name of the frame
        self.name_frame = customtkinter.CTkEntry(self,
                                                placeholder_text='Example: main_frame',
                                                width=200, corner_radius=10,
                                                border_color='#5e45a5')
        self.name_frame.grid(row=2, column=0, padx=30)

        # Dimensions of the frame
        self.size_frame = customtkinter.CTkEntry(self,
                                                placeholder_text='Example: 200x200',
                                                width=200, corner_radius=10,
                                                border_color='#5e45a5')
        self.size_frame.grid(row=2, column=1, padx=30)

        # Background color of the frame
        self.background_frame = customtkinter.CTkEntry(self,
                                                placeholder_text='Example: #2D9C7F',
                                                width=200, corner_radius=10,
                                                border_color='#5e45a5')
        self.background_frame.grid(row=5, column=0, padx=30)

        # Border color of the frame
        self.border_frame = customtkinter.CTkEntry(self,
                                                placeholder_text='Example: #B2721C',
                                                width=200, corner_radius=10,
                                                border_color='#5e45a5')
        self.border_frame.grid(row=5, column=1, padx=30)

        # Button to cancel frame creation
        self.frame_cancel = customtkinter.CTkButton(self,
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
        self.frame_cancel.grid(row=6, column=0, sticky='e', pady=40, padx=3)

        # Button to save the frame
        self.frame_save_button = customtkinter.CTkButton(self,
                                                text='Save',
                                                fg_color='#5e45a5',
                                                border_width=2,
                                                border_color='#3d2d6c',
                                                hover_color='#3d2d6c',
                                                width=100,
                                                height=35,
                                                font=(None, 15),
                                                corner_radius=13)
        self.frame_save_button.grid(row=6, column=1, sticky='w', pady=40, padx=3)