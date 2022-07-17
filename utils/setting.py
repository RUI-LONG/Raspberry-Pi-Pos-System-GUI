
class Settings:
    def __init__(self):
        self.full_screen = False
        self.set_full_screen()
    
    def set_full_screen(self):
        self.root.overrideredirect(True)
        self.root.overrideredirect(False)
        self.root.attributes('-fullscreen',True)