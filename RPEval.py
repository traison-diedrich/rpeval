import customtkinter as ctk
from rpeval.SelectPage import SelectPage
from rpeval.AthletePage import AthletePage

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("RPEval")
        self.geometry("1400x788")

        self.athlete_name = "Traison"

        container = ctk.CTkFrame(master=self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.pages = {}

        for name in ("SelectPage", "AthletePage"):
            cls = globals()[name]
            instance = cls(container, self)
            self.pages[name] = instance

            instance.grid(row=0, column=0, sticky="nsew")

        self.show_page("SelectPage")

    def show_page(self, content):
        for name in ("SelectPage", "AthletePage"):
            page = self.pages[name]
            page.grid_forget()
            if name == content:
                page.redraw()
                page.grid(row=0, column=0, sticky='nsew')

    def set_athlete(self, name):
        self.athlete_name = name

    def get_athlete(self):
        return self.athlete_name

if __name__ == "__main__":
    ctk.set_appearance_mode("Dark")
    theme_path = "./assets/theme/rpeTheme.json"
    ctk.set_default_color_theme(theme_path)
    app = App()
    app.mainloop()
