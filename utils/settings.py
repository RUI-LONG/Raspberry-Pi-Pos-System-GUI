from .data_loader import read_json, write_json

class Settings:
    def load_configs(self):
        self._get_screen_info()
        self._load_configs()
        if self.config.get("full_screen"): 
            self.set_full_screen()
        else:
            self.root.geometry("1350x750+0+0")

    def set_full_screen(self):
        self.root.overrideredirect(True)
        self.root.overrideredirect(False)
        self.root.attributes('-fullscreen',True)

    def _load_configs(self):
        _config_path = "./utils/"
        self.items = read_json(_config_path + "item_config.json")
        self.options = read_json(_config_path + "option_config.json")

    def _get_screen_info(self):
        _config_path = "./utils/app_config.json"
        self.config = read_json(_config_path)
        if not self.config.get("screen_width") or not self.config.get("screen_height"):
            self.config["screen_width"] = self.root.winfo_screenwidth()
            self.config["screen_height"] = self.root.winfo_screenheight()
        write_json(self.config, _config_path)
        self.max_w = self.config["screen_width"]
        self.max_h = self.config["screen_height"]