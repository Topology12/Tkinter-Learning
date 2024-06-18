from tkinter import *
from tkinter import ttk
import re


class DollartoVietNamDong:
    def __init__(self, root: Tk):
        root.title("Dollar to VietNamDong")
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        self.dollar = StringVar()
        dollar_entry = ttk.Entry(mainframe, width=5, textvariable=self.dollar)
        dollar_entry.grid(column=2, row=1, sticky=(W, E))
        self.vietnamdong = StringVar()
        ttk.Label(mainframe, textvariable=self.vietnamdong).grid(
            column=2, row=2, sticky=(W, E))
        ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(
            column=3, row=3, sticky=(W))
        ttk.Label(mainframe, text="Dollar").grid(
            column=3, row=1, sticky=(W, E))
        ttk.Label(mainframe, text="is vequivalent to ").grid(
            column=1, row=2, sticky=(E))
        ttk.Label(mainframe, text="VietNamDong").grid(
            column=3, row=2, sticky=(W))
        for child in mainframe.winfo_children():
            child.grid(padx=5, pady=5)
        dollar_entry.focus()
        root.bind("<Return> ", self.calculate)

    def calculate(self, *args):
        try:
            value = int(self.dollar.get()) * 25000
            count = 0
            temp = ""
            list_str = list()
            for i in reversed(str(value)):
                temp += i
                count += 1
                if count == 3:
                    list_str.append(temp)
                    count = 0
                    temp = ""
            if temp != "":
                list_str.append(temp)
            string_money = ".".join(list_str)
            string_money = string_money[::-1]
            self.vietnamdong.set(string_money)
        except ValueError:
            pass


root = Tk()
DollartoVietNamDong(root)
root.mainloop()
