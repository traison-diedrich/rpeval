import datetime
from typing import Tuple
from PIL import Image

import customtkinter as ctk
from rpeval.utils.tkvideoplayer import TkinterVideo

class VideoPlayer(ctk.CTkFrame):
    def __init__(self, parent, path, size):
        super().__init__(master=parent, 
                         fg_color="#333333", 
                         bg_color="gray13", 
                         background_corner_colors=("#333333", "#333333", 
                                                   "gray13", "gray13"))

        self.grid_rowconfigure((0), weight = 1)
        self.grid_columnconfigure((0), weight = 1)

        self.vid_frame = ctk.CTkFrame(master=self)
        self.vid_frame.grid(
            row=0, 
            column=0, 
            sticky='nsew', 
            padx=10, 
            pady=(5,10))

        self.path = path

        self.player = TkinterVideo(
            master=self.vid_frame, 
            keep_aspect=True, 
            background="#333333")
        self.player.set_size(size)
        self.player.load(self.path)
        self.player.pack(
            expand=True, 
            fill="both", 
            side="bottom")

        self.ui_frame = ctk.CTkFrame(master=self)
        self.ui_frame.grid_rowconfigure((0, 1), weight=0)
        self.ui_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.ui_frame.grid(
            row=1, 
            column=0, 
            sticky='sew', 
            padx=10, 
            pady=(0, 10))

        self.progress = ctk.CTkSlider(
            master=self.ui_frame, 
            orientation="horizontal", 
            progress_color="#f8a01f",
            button_color="#f8a01f", 
            button_hover_color="#a36914",
            command=self.seek)
        self.progress.grid(
            row=0, 
            column=0, 
            sticky='ew', 
            columnspan=3, 
            padx=5, 
            pady=5)
        self.progress.set(0)

        self.icon_path = './assets/images/icons/'
        self.play_icon = ctk.CTkImage(
            Image.open(self.icon_path + "play.png"), 
            size=(30, 30))
        self.pause_icon = ctk.CTkImage(
            Image.open(self.icon_path + "pause.png"), 
            size=(30, 30))

        self.play_pause_button = ctk.CTkButton(
            master=self.ui_frame, 
            fg_color='#f8a01f', 
            command=self.play_pause,
            image=self.play_icon, 
            text="",
            hover_color="#a36914", 
            width=40, 
            height=30, 
            border_width=0)
        self.play_pause_button.grid(
            row=1, 
            column=1, 
            pady=(0, 5))

        label_font = ctk.CTkFont(family="Eras Demi ITC", size=20)

        self.cur_label = ctk.CTkLabel(
            master=self.ui_frame, 
            text="0:00:00", 
            font=label_font)
        self.cur_label.grid(
            row=1, 
            column=0, 
            sticky="sw", 
            padx=(5, 0), 
            pady=(0,5))

        self.total_label = ctk.CTkLabel(
            master=self.ui_frame, 
            text="0:00:00", 
            font=label_font)
        self.total_label.grid(
            row=1, 
            column=2, 
            sticky="se", 
            padx=(0, 5), 
            pady=(0,5))

        self.player.bind("<<FrameChanged>>", self.update_duration)
        self.player.bind("<<Ended>>", self.end)
        
    def play_pause(self):
        if self.player.is_paused():
            self.player.play()
            self.play_pause_button.configure(
                image=self.pause_icon, 
                require_redraw=True)
        else:
            self.player.pause()
            self.play_pause_button.configure(
                image=self.play_icon, 
                require_redraw=True)

    def end(self, e):
        self.play_pause_button.configure(
            image=self.play_icon, 
            require_redraw=True)
        self.progress.set(1)

    def update_duration(self, e):
        self.progress.configure(to=self.player.video_info()["frames"])
        self.progress.set(int(self.player.current_frame_number()))

        self.cur_label.configure(
            text=str(datetime.timedelta(
            seconds=int(self.player.current_duration()))))

        duration = int(self.player.video_info()["duration"])
        self.total_label.configure(
            text=str(datetime.timedelta(seconds=duration)))

    def seek(self, e):
        self.player.seek_frame(
            int(self.progress.get()), 
            pause=True, 
            delay=.3)
        self.play_pause_button.configure(
            image=self.play_icon, 
            require_redraw=True)

    def set_video(self, path):
        self.path = path
        self.player.load(self.path)

    def set_size(self, size: Tuple[int, int]):
        self.player.set_size(size)
