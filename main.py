import matplotlib
matplotlib.use('Agg')

from tkinter import *
from utils.settings import Settings
from utils.frame import frameSettings

class POS(Settings, frameSettings):
    def __init__(self, root):
        self.root = root
        self.load_configs()
        
        self.create_vaiables()
        self.set_all_button_fonts(('Adobe 黑体 Std R', 24, 'normal'))
        self.set_all_category_fonts(('Adobe 黑体 Std R', 24, 'normal'))
        self.set_all_label_fonts(('Adobe 黑体 Std R', 20, 'normal'))
        self.set_all_frames()

if __name__ == '__main__':
    root = Tk()
    app = POS(root)
    root.mainloop()
    