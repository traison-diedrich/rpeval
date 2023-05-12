import customtkinter as ctk

class NewLiftFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        self.new_lift_text = ctk.CTkLabel(
            master=self, 
            text="This is the new lift frame for " +
                    self.controller.get_athlete())
        self.new_lift_text.grid(row = 0, column = 0, sticky = 'nsew')

    def redraw(self):
        self.new_lift_text.configure(
            text=f"This is the new lift frame for {self.controller.get_athlete()}", 
            require_redraw=True)