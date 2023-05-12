from PIL import Image
import customtkinter as ctk

class SelectPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        self.grid_rowconfigure((0,1,3), weight=1)
        self.grid_columnconfigure((0,1,2), weight=1)

        profile_pic_dir = "./assets/images/profile_pics/"

        self.traison_profile_img = ctk.CTkImage(
            Image.open(profile_pic_dir + "TraisonProfPic.jpeg"),
            size=(120,140))
        self.rayand_profile_img = ctk.CTkImage(
            Image.open(profile_pic_dir + "RayandProfPic.jpeg"),
            size=(120,140))
        self.trevor_profile_img = ctk.CTkImage(
            Image.open(profile_pic_dir + "TrevorProfPic.jpeg"),
            size=(120,140))

        title_font = ctk.CTkFont(size=60)
        subtitle_font = ctk.CTkFont(size=30)

        self.select_label = ctk.CTkLabel(
            master=self, 
            text="Select an Athlete", 
            font=title_font).grid(
            row=0, 
            column=0, 
            columnspan=3, 
            padx=20, 
            pady=(20,0), 
            sticky='s')

        self.athlete_button1 = ctk.CTkButton(
            master=self, 
            text="Traison",
            image=self.traison_profile_img, 
            compound="top",
            command=lambda: [self.controller.set_athlete("Traison"),
                             self.controller.show_page("AthletePage")]).grid(
            row=1, 
            column=0, 
            padx=20, 
            pady=(40,0), 
            ipady=5, 
            sticky='e')

        self.athlete_button2 = ctk.CTkButton(
            master=self, 
            text="Rayand",
            image=self.rayand_profile_img, 
            compound="top",
            command=lambda: [self.controller.set_athlete("Rayand"),
                            self.controller.show_page("AthletePage")]).grid(
            row=1, 
            column=1, 
            padx=20, 
            pady=(40,0), 
            ipady=5)

        self.athlete_button3 = ctk.CTkButton(
            master=self, 
            text="Trevor",
            image=self.trevor_profile_img, 
            compound="top",
            command=lambda: [self.controller.set_athlete("Trevor"),
                            self.controller.show_page("AthletePage")]).grid(
            row=1, 
            column=2, 
            padx=20, 
            pady=(40,0), 
            ipady=5, 
            sticky='w')

        self.new_athlete_label = ctk.CTkLabel(
            master=self, 
            text="New Athlete?", 
            font=subtitle_font).grid(
            row=2, 
            column=0, 
            columnspan=3, 
            padx=20, 
            pady=(50,0), 
            sticky="s")
        
        self.add_athlete_button = ctk.CTkButton(
            master=self, 
            text="Create an Athlete Profile", 
            font=subtitle_font).grid(
            row=3, 
            column=0, 
            columnspan=3, 
            padx=20, 
            pady=(15, 50), 
            sticky="n")

    def redraw(self):
        return 0