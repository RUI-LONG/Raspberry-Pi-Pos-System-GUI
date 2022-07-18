import matplotlib
matplotlib.use('Agg')

from tkinter import *
import tkinter as tk
from utils.settings import Settings
from utils.frame import frameSettings
from utils.widgets import Cashier

class POS(Settings, frameSettings, Cashier):
    def __init__(self, root):
        self.root = root
        self.set_user_config()

        self.set_all_button_fonts(('Adobe 黑体 Std R', 24, 'normal'))
        self.init_casher()
        self.set_all_frames()
        

if __name__ == '__main__':
    root = Tk()
    app = POS(root)
    root.mainloop()
    