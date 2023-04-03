import tkinter as tk
import random

class DumbApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Are You Dumb?")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        self.create_widgets()
        self.bind_events()
        self.root.mainloop()
        
    def create_widgets(self):
        self.message_label = tk.Label(self.root, text="Are you dumb?", font=("Arial", 28))
        self.message_label.pack(pady=50)
        
        self.yes_button = tk.Button(self.root, text="Yes", font=("Arial", 20), command=self.on_yes_clicked, width=10, height=2)
        self.yes_button.pack(side=tk.LEFT, padx=50, pady=50)
        
        self.no_button = tk.Button(self.root, text="No", font=("Arial", 20), command=self.on_no_clicked, width=10, height=2)
        self.no_button.pack(side=tk.RIGHT, padx=50, pady=50)
        self.no_button.bind("<Enter>", self.on_no_hover)
        
    def bind_events(self):
        self.root.protocol("WM_DELETE_WINDOW", lambda: None)
        self.root.bind("<Escape>", lambda event: self.root.quit())
        
    def on_yes_clicked(self):
        self.message_label.config(text="I knew it!")

    def on_no_clicked(self):
        self.message_label.config(text="Yes you are.")
        
    def on_no_hover(self, event):
        x = random.randint(50, self.root.winfo_width() - 100)
        y = random.randint(100, self.root.winfo_height() - 50)
        button_width = self.no_button.winfo_width()
        button_height = self.no_button.winfo_height()
        if x < 0:
            x = 0
        elif x + button_width > self.root.winfo_width():
            x = self.root.winfo_width() - button_width
        if y < 0:
            y = 0
        elif y + button_height > self.root.winfo_height():
            y = self.root.winfo_height() - button_height
        self.no_button.place(x=x, y=y)
        
app = DumbApp()
