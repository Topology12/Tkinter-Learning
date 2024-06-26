from tkinter import *
from tkinter import ttk


def button_action(*args):
    text = name.get()
    text_label.set(f"Wecomle {text}")


root = Tk()
root.geometry("600x600")
root.minsize(width=300, height=300)
s = ttk.Style()
s.configure('Danger.TFrame', background='red', borderwidth=5, relief='raised')
frame = ttk.Frame(root, style='Danger.TFrame')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
frame.grid(column=0, row=0, sticky=(N, W, E, S))
frame.configure(padding=(15, 15), borderwidth=2, relief="raised")
frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
text_label = StringVar()
label = ttk.Label(frame, textvariable=text_label, padding="10 10")
style = ttk.Style()
style.configure("Custom.TFrame", background="green")
f_level1 = ttk.Frame(frame, style="Custom.TFrame")
f_level1.grid(column=0, row=1)
name_label = ttk.Label(f_level1, text="Name", padding="10 10")
name_label.grid(column=0, row=0)
name = StringVar()
name_entry = ttk.Entry(f_level1, textvariable=name)
name_entry.focus()
name_entry.grid(column=1, row=0)
label.grid(column=0, row=0, sticky=(W, E))
name_entry.bind("<Return>", button_action)
f_level1.rowconfigure(0, weight=1)
f_level1.columnconfigure(0, weight=1)
f_level1.configure(borderwidth=1, relief="raised")
text_label.set("Helll World!")
button = ttk.Button(frame, text="Action", padding=5, command=button_action)
button.grid(column=0, row=2)
frame_1 = ttk.Frame(root, borderwidth=2, relief="flat")
frame_1.grid(row=0, column=1, sticky=(N, W, E, S))
root.columnconfigure(1, weight=1)
chk_button = ttk.Checkbutton(frame_1, padding=(5, 5), text="Music")
chk_button.grid(column=0, row=0, sticky=(W, E))
chk_button = ttk.Checkbutton(frame_1, padding=(5, 5), text="Game")
chk_button.grid(column=1, row=0, sticky=(W, E))
gender = StringVar()
ttk.Radiobutton(frame_1, padding=(5), text="Famale", value="Famale",
                variable=gender).grid(column=0, row=2, sticky=(W, E))
ttk.Radiobutton(frame_1, padding=(5), text="Male", value="Male",
                variable=gender).grid(column=1, row=2, sticky=(W, E), columnspan=2)
ttk.Combobox(frame_1, values=["VietNam", "England", "Japan",  "Korea"]).grid(
    row=3, column=1, sticky=(W, E))

root.mainloop()
