import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("1024x768")
app.title("ATEM Transition Creator")

frame = ctk.CTkFrame(master=app)
frame.pack(pady=5, padx=5, fill="both", expand=True)




app.mainloop()