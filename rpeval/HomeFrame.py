import customtkinter as ctk
from rpeval.VideoPlayer import VideoPlayer

class HomeFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        self.grid_rowconfigure((0,1), weight=1)
        self.grid_columnconfigure((0,1), weight=1)

        self.video_frame = ctk.CTkFrame(
            master=self, 
            fg_color="#333333")
        self.video_frame.grid_rowconfigure((1), weight=1)
        self.video_frame.grid_columnconfigure((0), weight=1)
        self.video_frame.grid(
            row=0, 
            column=0, 
            padx=30, 
            pady=30, 
            sticky='nsew')

        label_font = ctk.CTkFont(size=20)

        self.recent_label = ctk.CTkLabel(
            master=self.video_frame, 
            text=self.controller.get_athlete() + "'s Most Recent Lift", 
            font=label_font, 
            text_color="#ebebeb")
        self.recent_label.grid(row=0, column=0, sticky='ns', pady=(5,0))

        self.video_path = "./assets/video/Squat_01.mp4"
        self.player = VideoPlayer(
            parent=self.video_frame, 
            path=self.video_path, 
            size=(750, 422))
        self.player.grid(
            row=1, 
            column=0, 
            sticky='nsew')

    def redraw(self):
        self.recent_label.configure(
            text=f"{self.controller.get_athlete()}'s Most Recent Lift", 
            require_redraw=True)
        