import customtkinter
from assembler import AssemblerFrame

class Frame(customtkinter.CTk):

    """ This is the Frame object. It
        is used to create new frames and
        to add them to the code """

    def __init__(self):
        super().__init__()

        # Window's settings
        self.title('CodeGenie - Frame')
        self.geometry('550x580')
        self.resizable(False, False)

        # Used to avoid writing repetitive code for the labels
        list_of_labels = [
                            ['Frame\'s parent', 1, 0],
                            ['Frame\'s name', 1, 1],
                            ['Frame\'s dimensions', 4, 0],
                            ['Background color', 4, 1],
                            ['Border color', 7, 0],
                            ['Border radius', 7, 1],
                            ['Column (y)', 10, 0],
                            ['Row (x)', 10, 1],
                            ['Padding x', 13, 0],
                            ['Padding y', 13, 1]
                        ]

        # Spacers
        c = 12
        while c >= 0:
            self.spacer = customtkinter.CTkLabel(self, text='')
            self.spacer.grid(row=c, column=0)
            c -= 3

        # Lables
        for i in range(len(list_of_labels)):
            self.label = customtkinter.CTkLabel(self,
                                                text=list_of_labels[i][0],
                                                font=(None, 18))
            self.label.grid(row=list_of_labels[i][1], column=list_of_labels[i][2], pady=5, padx=30)

        # Parent of the frame
        self.parent_frame = customtkinter.CTkEntry(self,
                                                placeholder_text='Example: self',
                                                width=200,
                                                corner_radius=10,
                                                border_color='#5e45a5')
        self.parent_frame.grid(row=2, column=0, padx=30)

        # Name of the frame
        self.name_frame = customtkinter.CTkEntry(self,
                                                placeholder_text='Example: main_frame',
                                                width=200,
                                                corner_radius=10,
                                                border_color='#5e45a5')
        self.name_frame.grid(row=2, column=1, padx=30)

        # Dimensions of the frame
        self.size_frame = customtkinter.CTkEntry(self,
                                                placeholder_text='Example: 200x200',
                                                width=200,
                                                corner_radius=10,
                                                border_color='#5e45a5')
        self.size_frame.grid(row=5, column=0, padx=30)

        # Background color of the frame
        self.background_frame = customtkinter.CTkEntry(self,
                                                placeholder_text='Example: #2D9C7F',
                                                width=200,
                                                corner_radius=10,
                                                border_color='#5e45a5')
        self.background_frame.grid(row=5, column=1, padx=30)

        # Border color of the frame
        self.border_frame = customtkinter.CTkEntry(self,
                                                placeholder_text='Example: #B2721C',
                                                width=200,
                                                corner_radius=10,
                                                border_color='#5e45a5')
        self.border_frame.grid(row=8, column=0, padx=30)

        # Border radius
        self.radius_frame = customtkinter.CTkEntry(self,
                                                placeholder_text='Example: 20',
                                                width=200,
                                                corner_radius=10,
                                                border_color='#5e45a5')
        self.radius_frame.grid(row=8, column=1, padx=30)

        # Column x
        self.column_frame = customtkinter.CTkEntry(self,
                                                placeholder_text='Example: 0',
                                                width=200,
                                                corner_radius=10,
                                                border_color='#5e45a5')
        self.column_frame.grid(row=11, column=0, padx=30)

        # Row y
        self.row_frame = customtkinter.CTkEntry(self,
                                                placeholder_text='Example: 0',
                                                width=200,
                                                corner_radius=10,
                                                border_color='#5e45a5')
        self.row_frame.grid(row=11, column=1, padx=30)

        # Padding x
        self.padx_frame = customtkinter.CTkEntry(self,
                                                placeholder_text='Example: 20',
                                                width=200,
                                                corner_radius=10,
                                                border_color='#5e45a5')
        self.padx_frame.grid(row=14, column=0, padx=30)

        # Padding y
        self.pady_frame = customtkinter.CTkEntry(self,
                                                placeholder_text='Example: 20',
                                                width=200,
                                                corner_radius=10,
                                                border_color='#5e45a5')
        self.pady_frame.grid(row=14, column=1, padx=30)

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
        self.frame_cancel.grid(row=15, column=0, sticky='e', pady=40, padx=3)

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
                                                corner_radius=13,
                                                command=self.save_frame)
        self.frame_save_button.grid(row=15, column=1, sticky='w', pady=40, padx=3)

    # Transfer the data to the assembler to add the frame to the code
    def save_frame(self):
        AssemblerFrame(parent=self.parent_frame.get(),
                        name=self.name_frame.get(),
                        size=self.size_frame.get(),
                        background=self.background_frame.get(),
                        border=self.border_frame.get(),
                        radius=self.radius_frame.get(),
                        column=self.column_frame.get(),
                        row=self.row_frame.get(),
                        padx=self.padx_frame.get(),
                        pady=self.pady_frame.get())

        return self.destroy()