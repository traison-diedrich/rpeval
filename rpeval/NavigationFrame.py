from PIL import Image
import customtkinter as ctk

class NavigationFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(master=parent, fg_color="#333333")

        self.controller = controller

        self.grid_rowconfigure(4, weight=1)

        self.athlete_image_path = ("./assets/images/profile_pics/" + 
                                   self.controller.get_athlete() + 
                                   "ProfPic.jpeg")
        
        self.athlete_image = ctk.CTkImage(
            Image.open(self.athlete_image_path),size=(80, 93))
        
        self.icon_dir = './assets/images/icons/'
        self.home_icon = ctk.CTkImage(
            Image.open(self.icon_dir + "home.png"), size=(20, 20))
        self.pencil_icon = ctk.CTkImage(
            Image.open(self.icon_dir + "pencil.png"), size=(20, 20))
        self.history_icon = ctk.CTkImage(
            Image.open(self.icon_dir + "history.png"), size=(20, 20))

        self.athlete_button = ctk.CTkButton(
            master=self, 
            text=self.controller.get_athlete(),
            image=self.athlete_image, 
            fg_color='transparent', 
            text_color="#ebebeb",
            hover_color="gray30",
            command=lambda: [self.controller.show_page("SelectPage"),
                            self.redraw("HomeFrame")],
            corner_radius=8, 
            border_spacing=10, 
            height=50, 
            compound="top", 
            border_width=0,
            background_corner_colors=("gray5","gray5",
                                      "#333333","#333333"))
        self.athlete_button.grid(
            row=0, 
            column=0, 
            sticky="ew")

        self.home_button = ctk.CTkButton(
            master=self, 
            corner_radius=0, 
            height=40, 
            border_spacing=10, 
            text="Home", 
            fg_color="gray25", 
            text_color="#ebebeb", 
            hover_color= "gray30",
            border_width=0,
            image=self.home_icon, 
            anchor="w",
            hover=False,
            state="disabled",
            text_color_disabled="#ebebeb", 
            command=lambda: [self.controller.show_frame("HomeFrame"),
                            self.redraw("HomeFrame")])
        self.home_button.grid(
            row=1, 
            column=0, 
            sticky="ew")

        self.new_lift_button = ctk.CTkButton(
            master=self, 
            corner_radius=0, 
            height=40, 
            border_spacing=10, 
            text="New Lift", 
            fg_color="transparent", 
            text_color="#ebebeb", 
            hover_color= "gray30",
            border_width=0,
            image=self.pencil_icon, 
            anchor="w", 
            command=lambda: [self.controller.show_frame("NewLiftFrame"),
                            self.redraw("NewLiftFrame")])
        self.new_lift_button.grid(
            row=2, 
            column=0, 
            sticky="ew")

        self.past_lift_button = ctk.CTkButton(
            master=self, 
            corner_radius=0, 
            height=40, 
            border_spacing=10, 
            text="Past Lifts", 
            fg_color="transparent", 
            text_color="#ebebeb", 
            hover_color= "gray30",
            border_width=0,
            image=self.history_icon, 
            anchor="w", 
            command=lambda: [self.controller.show_frame("PastLiftFrame"),
                            self.redraw("PastLiftFrame")])
        self.past_lift_button.grid(
            row=3, 
            column=0, 
            sticky="ew")

    def redraw(self, content):
        if self.athlete_button.cget("text") != self.controller.get_athlete():
            self.athlete_image_path = ("./assets/images/profile_pics/" + 
                                       self.controller.get_athlete() + 
                                       "ProfPic.jpeg")
            self.athlete_image = ctk.CTkImage(
                Image.open(self.athlete_image_path), size=(80, 93))

            self.athlete_button.configure(
                text=self.controller.get_athlete(),
                image = self.athlete_image, 
                require_redraw=True)   

        if content == "HomeFrame":
            self.home_button.configure(
                fg_color = "gray25",
                hover=False,
                state="disabled",
                require_redraw=True)
        else:
            self.home_button.configure(
                fg_color = "transparent",
                hover=True,
                state="enabled",
                require_redraw=True)

        self.new_lift_button.configure(fg_color = "gray25" 
                                       if content == "NewLiftFrame" 
                                       else "transparent",
                                       require_redraw=True)
        self.past_lift_button.configure(fg_color = "gray25" 
                                        if content == "PastLiftFrame" 
                                        else "transparent", 
                                        require_redraw=True)
