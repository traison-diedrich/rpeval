import customtkinter as ctk

from rpeval.NavigationFrame import NavigationFrame
from rpeval.HomeFrame import HomeFrame
from rpeval.NewLiftFrame import NewLiftFrame
from rpeval.PastLiftFrame import PastLiftFrame

class AthletePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, corner_radius=0, fg_color="gray5")

        self.controller = controller

        self.grid_rowconfigure((0), weight=1)
        self.grid_columnconfigure((1), weight=1)

        self.navigation_frame = NavigationFrame(
            parent=self, 
            controller=self)
        self.navigation_frame.grid(
            row=0, 
            column=0, 
            padx=(5,0), 
            pady=5, 
            sticky='nsew')

        container = ctk.CTkFrame(
            master=self, 
            fg_color="transparent")
        container.grid(
            row=0, 
            column=1, 
            sticky='nsew')

        container.grid_rowconfigure((0), weight=1)
        container.grid_columnconfigure((0), weight=1)

        self.frames = {}

        for name in ("HomeFrame", "NewLiftFrame", "PastLiftFrame"):
            cls = globals()[name]
            instance = cls(parent=container, controller=self)
            self.frames[name] = instance

        self.show_frame("HomeFrame")

    def show_frame(self, content):
        for name in ("HomeFrame", "NewLiftFrame", "PastLiftFrame"):
            frame = self.frames[name]
            frame.grid_forget()
            if name == content:
                frame.redraw()
                frame.grid(
                    row=0, 
                    column=0, 
                    padx=5, 
                    pady=5, 
                    sticky='nsew')

    def show_page(self, content):
        self.controller.show_page(content)

    def redraw(self):
        self.navigation_frame.redraw(content="HomeFrame")
        self.show_frame("HomeFrame")

    def get_athlete(self):
        return self.controller.get_athlete()