import tkinter as tk

# Grid system

root = tk.Tk()

labelName = tk.Label(root, text="My name is Duong")
labelName.grid(row=0, column=0)

labelAge = tk.Label(root, text="Im 20 years old")
labelAge.grid(row=1, column=0)

# Creating button widget


def myClick():
    myLabel = tk.Label(root, text="Look! I clicked a Button!!")
    myLabel.grid()


myButton = tk.Button(root, text="Click me", padx=50, pady=50, command=myClick,fg="blue", bg="orange")
myButton.grid(row=0, column=1)


root.mainloop()
