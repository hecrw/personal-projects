import random
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText


class type_tester:
    
    def __init__(self):
        #assignments
        self.time, self.idx, self.spaces = 15, 0, 0
        with open('words.txt', 'r') as file:
            self.common_words = file.read().splitlines()
        self.common_words = random.sample(self.common_words, 400)
        self.portion = self.common_words[self.idx: self.idx + 10] 
        self.portion = " ".join(self.portion)
        
        #widgets
        self.window = tk.Tk()
        self.widgets = ttk.Frame(self.window)
        self.buttons = ttk.Frame(self.widgets)
        self.window.geometry("1000x700")
        self.label = ttk.Label(self.window, font=("Ariel", 14), text=self.portion)
        self.text = ScrolledText(self.widgets, width=50,height=5, font=("Ariel", 14))
        self.first = ttk.Button(self.buttons, text="15s", command=self.set_time(0))
        self.second = ttk.Button(self.buttons, text="30s", command=self.set_time(1))
        self.third = ttk.Button(self.buttons, text="60s", command=self.set_time(2))
        
        #bind
        self.text.bind("<KeyRelease>", self.check)
        
        #pack
        self.label.pack(pady=10)
        self.buttons.pack(side="left")
        self.widgets.pack()
        self.first.pack(); self.second.pack(); self.third.pack()
        self.text.pack()
        self.window.mainloop()
        
        
    def check(self, event):
        content = self.text.get("1.0", tk.END)
        curr = content.count(" ")
        word_count = len(content.split())
        size = len(self.portion.split())
        if curr != self.spaces:
            self.spaces = curr
            
            for tag in self.text.tag_names():
                self.text.tag_delete(tag)
                
            for i in range(len(content.split())):
                if content.split()[i] != self.portion.split()[i] and i < len(self.portion.split()):
                    pos = content.index(content.split()[i])
                    tag_name = f"misspelled_{pos}"
                    self.text.tag_add(tag_name, f"1.{pos}", f"1.{pos + len(content.split()[i])}")
                    self.text.tag_config(tag_name, underline=True, foreground="red")
                    
            
        if word_count == 10 and event.keysym == 'space':
            self.idx += 10
            self.portion = " ".join(self.common_words[self.idx:self.idx+10])
            self.label.config(text=self.portion)
            self.text.delete("1.0", tk.END)

    
    def set_time(self, idx):
        lst = [15, 30, 60]
        self.time = lst[idx]
        
        
        
type_tester()
