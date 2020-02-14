import tkinter as tk

class TextArea:
    def __init__(self, root):
        textArea = tk.Text(root)
        textArea.pack(
            expand=True,
            fill='both'
        )