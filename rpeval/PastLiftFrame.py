import customtkinter as ctk

class PastLiftFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        self.past_lift_text = ctk.CTkLabel(
            master=self, 
            text="This is the past lift frame for " + 
                    self.controller.get_athlete())
        self.past_lift_text.grid(row = 0, column = 0, sticky = 'nsew')

    def redraw(self):
        self.past_lift_text.configure(
            text=f"This is the past lift frame for {self.controller.get_athlete()}", 
            require_redraw=True)