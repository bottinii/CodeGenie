
# Libraries
import tkinter
import customtkinter
from tkinter.colorchooser import askcolor
import random
import json

# Profile window object
class Profile(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()

        # Window settings
        self.title("CodeGenie - Profile")
        self.geometry("500x370")
        self.resizable(False, False)

        # Column configuration
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)

        # Colors list
        self.colors = [
                            "#E9D740", "#40ACE9", "#E85A46",
                            "#185A1E", "#1E50B6", "#6A29DC"
                       ]
        
        # Open json
        with open("./storedData/data.json", "r") as self.jsonFile:
            self.data = json.load(self.jsonFile)

        # Set the profile image color
        if (self.data["profileColor"] == ''):
            randomColor = random.choice(self.colors)
            self.data["profileColor"] = randomColor

        with open("./storedData/data.json", "w") as self.jsonFile:
            json.dump(self.data, self.jsonFile)

        # Widgets
        backToMenu = customtkinter.CTkButton(self,
                                             text="Exit",
                                             fg_color="#242424",
                                             hover_color="#424242",
                                             border_width=1,
                                             border_color="#ffffff",
                                             font=(None, 15),
                                             width=80,
                                             height=25,
                                             command=self.destroy)
        backToMenu.grid(row=0, column=0, padx=10)

        self.profileLabel = customtkinter.CTkLabel(self,
                                                   text="Profile",
                                                   font=(None, 27))
        self.profileLabel.grid(row=0, column=1, pady=13)

        saveChanges = customtkinter.CTkButton(self,
                                             text="Save",
                                             fg_color="#242424",
                                             hover_color="#424242",
                                             border_width=1,
                                             border_color="#ffffff",
                                             font=(None, 15),
                                             width=80,
                                             height=25,
                                             command=self.changeSettings)
        saveChanges.grid(row=0, column=2, padx=10)

        self.profileImage = customtkinter.CTkLabel(self,
                                                    text='',
                                                    width=80,
                                                    height=80,
                                                    fg_color=self.data["profileColor"],
                                                    corner_radius=100)
        self.profileImage.grid(column=1, row=1, pady=15)

        self.changeColorImage = customtkinter.CTkButton(self,
                                                        text="Change color",
                                                        fg_color="#242424",
                                                        hover_color="#424242",
                                                        corner_radius=10,
                                                        border_width=1,
                                                        border_color="#ffffff",
                                                        height=30,
                                                        font=(None, 17),
                                                        command=self.updateColorImage)
        self.changeColorImage.grid(column=1, row=2)

        spacer = customtkinter.CTkLabel(self, text='')
        spacer.grid(row=3, column=1)

        self.nameProfile = customtkinter.CTkEntry(self,
                                                  width=550,
                                                  font=(None, 14),
                                                  corner_radius=20,
                                                  border_width=1,
                                                  border_color="#B491FF")
        self.nameProfile.grid(row=4, column=1, pady=10)
        self.nameProfile.insert(0, self.data["name"])

        self.bioProfile = customtkinter.CTkEntry(self,
                                                  width=550,
                                                  font=(None, 14),
                                                  corner_radius=20,
                                                  border_width=1,
                                                  border_color="#B491FF")
        self.bioProfile.grid(row=5, column=1)
        self.bioProfile.insert(0, self.data["bio"])

        self.emailProfile = customtkinter.CTkEntry(self,
                                                  width=550,
                                                  font=(None, 14),
                                                  corner_radius=20,
                                                  border_width=1,
                                                  border_color="#B491FF")
        self.emailProfile.grid(row=6, column=1, pady=10)
        self.emailProfile.insert(0, self.data["email"])
    
    # Update settings in the json (this code sucks)
    def changeSettings(self):
        with open("./storedData/data.json", "w") as self.jsonFile:
            self.data["name"] = self.nameProfile.get()
            json.dump(self.data, self.jsonFile)

        with open("./storedData/data.json", "w") as self.jsonFile:
            self.data["bio"] = self.bioProfile.get()
            json.dump(self.data, self.jsonFile)

        with open("./storedData/data.json", "w") as self.jsonFile:
            self.data["email"] = self.emailProfile.get()
            json.dump(self.data, self.jsonFile)

        return self.destroy()

    # Updates the profile image color
    def updateColorImage(self):
        color = askcolor(title="Select color")
        with open("./storedData/data.json", "w") as self.jsonFile:
            self.data["profileColor"] = color[1]
            json.dump(self.data, self.jsonFile)
        self.destroy()
        self.__init__()