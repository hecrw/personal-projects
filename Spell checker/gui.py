import re
import tkinter as tk
import ttkbootstrap as ttk
from tkinter.font import Font
from tkinter.scrolledtext import ScrolledText
from Trie import dictionary

class spellingchecker:
    
    def __init__(self):
        self.spaces = 0
        #window
        self.window = ttk.Window(themename='darkly')
        self.window.geometry("1000x700")
        
        
        #text box buttons and frames
        self.frame = ttk.Frame(self.window)
        self.buttons = ttk.Frame(self.frame)
        self.label = ttk.Label(self.buttons, text="Suggested words:")
        self.text = ScrolledText(self.frame, font=("Ariel", 12), width=60, height=20)
        self.text.bind("<KeyRelease>", self.check)
        
        
        #packs
        self.text.pack(side="left")
        self.label.pack()
        self.buttons.pack(side="left", fill="both", expand=True, padx=10, pady=(0, 10))
        self.frame.pack()
        self.window.mainloop()
        
    def check(self, event):
        content = self.text.get("1.0", "end-1c")
        curr = content.count(" ")
        if curr != self.spaces:
            self.spaces = curr
            
        for tag in self.text.tag_names():
            self.text.tag_delete(tag)
            
        for word in content.split(" "):
            temp = re.sub(r'[^\w\s]', '', word)
            
            if not dictionary.search(temp):
                pos = content.index(word)
                tag_name = f"misspelled_{pos}"
                self.text.tag_add(tag_name, f"1.{pos}", f"1.{pos + len(word)}")
                self.text.tag_config(tag_name, underline=True, foreground="red")
                self.text.tag_bind(tag_name, "<Button-1>", lambda event, w = word : self.show_suggestions(event, w))
        
    def show_suggestions(self, event, misspelled_word):
        suggestions = dictionary.suggestions(misspelled_word)
        if suggestions:
            suggestions_text = ", ".join(suggestions)
            suggestion_popup = tk.Toplevel(self.window)
            suggestion_popup.title("Suggestions")
            suggestion_label = tk.Label(suggestion_popup, text="Choose a suggestion:")
            suggestion_label.pack()
            for suggestion in suggestions:
                suggestion_button = tk.Button(suggestion_popup, text=suggestion, command=lambda s=suggestion: self.replace_word(misspelled_word, s))
                suggestion_button.pack()

    def replace_word(self, misspelled_word, replacement):
        content = self.text.get("1.0", tk.END)
        new_content = content.replace(misspelled_word, replacement)
        self.text.delete("1.0", tk.END)
        self.text.insert("1.0", new_content)
        self.check(None)

                    
spellingchecker()
