import matplotlib
matplotlib.use('Agg')

from tkinter import ttk, messagebox, Tk
import tkinter as tk

class POS:
    def __init__(self, root):
        self.root = root
        self.root.title("Point of Sale")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background="cadetblue")


if __name__ == '__main__':
    root = Tk()
    app = POS(root)
    root.mainloop()