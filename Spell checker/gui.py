import re
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from Trie import dictionary

class spellingchecker:
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("600x500")
        self.text = ScrolledText(self.window, font=("Ariel", 14))
        self.text.bind("<KeyRelease>", self.check)
        self.text.pack()
        self.spaces = 0
        self.window.mainloop()
        
    def check(self, event):
        content = self.text.get("1.0", tk.END)
        space_count = content.count(" ")
        
        if space_count != self.spaces:
            self.spaces = space_count
            
            for tag in self.text.tag_names():
                self.text.tag_delete(tag)
            
            for word in content.split(" "):
                t = re.sub(r"[\W]", '', word.lower())
                if not dictionary.search(t):
                    position = content.index(word)
                    tag_name = f"misspelled_{position}"
                    self.text.tag_add(tag_name, f"1.{position}", f"1.{position + len(word)}")
                    self.text.tag_config(tag_name, foreground="red", underline=True)
                    self.text.tag_bind(tag_name, "<Button-1>", lambda event, w=word: self.show_suggestions(event, w))
        
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
