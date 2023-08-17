import tkinter as tk
from tkinter import ttk

#Main Window
window = tk.Tk()
window.geometry("1366x768")
window.title("ATEM Transition Creator")
window.iconbitmap("app_icon.ico")
#Main Frame
frame = tk.Frame(window)
frame.pack(fill="both", expand=True)

bframe = tk.Frame(window)
bframe.pack(side="bottom")

#Main Menu
menu = tk.Menu(window)
#File Menu
file_menu = tk.Menu(menu, tearoff = False)
file_menu.add_command(label="Quit", command = lambda: quit())
menu.add_cascade(label = "File", menu = file_menu)
window.configure(menu = menu)

#Screen Frame
 
screen_frame = tk.Frame(frame, width=1024, height=576, background="black")
screen_frame.pack(side = "left", padx=5)

#Right Frame
right_main_frame = tk.Frame(frame, width = 332 ,height= 576,background= "light grey")
right_main_frame.pack(side ="left")

#Bottom Frame
bottom_main_frame = tk.Frame(bframe, width = 1356, height = 192, background= "light grey")
bottom_main_frame.pack(side="bottom", padx=5)

#Right Menu
right_menu_style = ttk.Style()
right_menu_style.configure("rmenu.TNotebook", font=("Open Sans",12), background="light grey")

right_menu=ttk.Notebook(right_main_frame, style="rmenu.TNotebook")


tab_box1 = tk.Frame(right_menu, background="light grey", width=302, height=525)
tab_box2 = tk.Frame(right_menu, background="light grey", width=302, height=525)
tab_box3 = tk.Frame(right_menu, background="light grey", width=302, height=525)
tab_box4 = tk.Frame(right_menu, background="light grey", width=302, height=525)
right_menu.add(tab_box1, text="Box1")
right_menu.add(tab_box2, text="Box2")
right_menu.add(tab_box3, text="Box3")
right_menu.add(tab_box4, text="Box4")
right_menu.pack()




window.mainloop()