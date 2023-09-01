import random
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText


class type_tester:
    
    def __init__(self):
        #assignments
        self.spaces = 0
        self.time = 15
        with open('words.txt', 'r') as file:
            self.common_words = file.read().splitlines()
        self.common_words = random.sample(self.common_words, 350)
        
        #widgets
        self.window = tk.Tk()
        self.widgets = ttk.Frame(self.window)
        self.buttons = ttk.Frame(self.widgets)
        self.window.geometry("1000x700")
        self.label = ttk.Label(self.window, font=("Ariel", 14))
        self.text = ScrolledText(self.widgets, width=50,height=5, font=("Ariel", 14))
        self.first = ttk.Button(self.buttons, text="15s", command=self.set_time(0))
        self.second = ttk.Button(self.buttons, text="30s", command=self.set_time(1))
        self.third = ttk.Button(self.buttons, text="60s", command=self.set_time(2))
        
        #pack
        self.buttons.pack(side="left")
        self.widgets.pack()
        self.first.pack(); self.second.pack(); self.third.pack()
        self.text.pack()
        self.window.mainloop()
        
        self.text.bind("<keyRelease>", self.check)
        
    def check(self, event):
        pass
    
    def set_time(self, idx):
        lst = [15, 30, 60]
        self.time = lst[idx]
        
        
        
type_tester()