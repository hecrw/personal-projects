import random
import tkinter as tk
import ttkbootstrap as ttk
from tkinter.scrolledtext import ScrolledText

class type_tester:
    
    def __init__(self):
        #assignments
        self.time, self.idx, self.spaces, self.num = 15, 0, 0, 0
        self.raw_wpm, self.wpm, self.times = [], [], [15, 30, 60]
        with open('words.txt', 'r') as file:
            self.common_words = file.read().splitlines()
        self.common_words = random.sample(self.common_words, 400)
        self.portion = self.common_words[self.idx: self.idx + 10] 
        self.portion = " ".join(self.portion)
        
        #window
        self.window = ttk.Window(themename="darkly")
        self.window.geometry("1000x700")
        #widgets
        self.widgets = ttk.Frame(self.window)
        self.label = ttk.Label(self.window, font=("Helvetica", 14), text=self.portion)
        self.text = ScrolledText(self.widgets, width=50, height=5, font=("Helvetica", 14))
        self.text.config(state="disabled")
        #buttons
        self.buttons = ttk.Frame(self.widgets)
        self.first = ttk.Button(self.buttons, text="15s", command=lambda: self.set_time(0))
        self.second = ttk.Button(self.buttons, text="30s", command=lambda: self.set_time(1))
        self.third = ttk.Button(self.buttons, text="60s", command=lambda: self.set_time(2))
        #timer
        self.timer = ttk.Label(self.window, text=self.time, font=("Helvetica", 14))
        #controls
        self.controls = ttk.Frame(self.window)
        self.restart = ttk.Button(self.controls, text="reset",command=self.reset)
        self.start = ttk.Button(self.controls,text="start",command=self.start_countdown)
        
        #bind
        self.text.bind("<KeyRelease>", self.check)
        
        #pack
        self.label.pack(pady=10)
        self.buttons.pack(side="left")
        self.widgets.pack()
        self.first.pack()
        self.second.pack()
        self.third.pack()
        self.text.pack()
        self.start.pack(side="left")
        self.restart.pack(side="left")
        self.controls.pack()
        self.timer.pack()
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
                elif content.split()[i] == self.portion.split()[i] and i < len(self.portion.split()):
                    if content.split()[i] not in self.wpm:
                        self.wpm.append(content.split()[i])
                if content.split()[i] not in self.raw_wpm:
                    self.raw_wpm.append(content.split()[i])
            

    
    def set_time(self, idx):
        self.time = self.times[idx]
        self.num = idx
        self.timer.config(text=str(self.time))
        self.reset()
        
        
    def start_countdown(self): 
        self.time = self.times[self.num]
        self.text.config(state="normal")
        self.update_countdown()
        
    def update_countdown(self):
        if self.time > 0:
            self.timer.config(text=str(self.time))
            self.time -= 1
            self.timer.after(1000, self.update_countdown)
        else:
            raw_word_count = len("".join(self.raw_wpm))
            correct_word_count = len("".join(self.wpm))
            accuracy = (correct_word_count / raw_word_count) * 100 if raw_word_count > 0 else 0
            words_per_minute = ((correct_word_count / 5) / (self.times[self.num] / 60))
            
            result_text = f"Time's up!\n\nWords per minute: {words_per_minute:.2f}\nAccuracy: {accuracy:.2f}%"
            self.label.config(text=result_text)
            self.text.config(state=tk.DISABLED
                
    
    def reset(self):
        self.text.delete("1.0", tk.END)
        self.raw_wpm.clear()
        self.wpm.clear()
        self.common_words = random.sample(self.common_words, 400)
        self.idx = 0
        self.portion = " ".join(self.common_words[self.idx:self.idx + 10])
        self.label.config(text=self.portion)
        self.text.config(state=tk.NORMAL)
            

type_tester()
