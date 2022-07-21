from tkinter import *

class Calculator:
    def create_calculator(self, frame, frame_size):
        _width, _height = frame_size[0], frame_size[1]
        _button_size = (int(_width*0.015), int(_height*0.004))
        _pad_w = int(_width*0.08)
        _pad_h = int(_height*0.1)
        
        _buttons = {
                "7": (_pad_w, _pad_h),
                "8": (_pad_w+_button_size[0]*18, _pad_h),
                "9": (_pad_w+_button_size[0]*36, _pad_h),

                "4": (_pad_w, _pad_h*2+_button_size[1]*20),
                "5": (_pad_w+_button_size[0]*18, _pad_h*2+_button_size[1]*20),
                "6": (_pad_w+_button_size[0]*36, _pad_h*2+_button_size[1]*20),

                "1": (_pad_w, _pad_h*3+_button_size[1]*40),
                "2": (_pad_w+_button_size[0]*18, _pad_h*3+_button_size[1]*40),
                "3": (_pad_w+_button_size[0]*36, _pad_h*3+_button_size[1]*40),

                "0": (_pad_w, _pad_h*4+_button_size[1]*60),
            }
        
        _call_back = {
            "0": lambda: self.press_number("0"),
            "1": lambda: self.press_number("1"),
            "2": lambda: self.press_number("2"),
            "3": lambda: self.press_number("3"),
            "4": lambda: self.press_number("4"),
            "5": lambda: self.press_number("5"),
            "6": lambda: self.press_number("6"),
            "7": lambda: self.press_number("7"),
            "8": lambda: self.press_number("8"),
            "9": lambda: self.press_number("9"),
        }
        _fonts = {
            "bg": "white",
            "fg": "black",
            "bd": 2
        }
        self.create_buttons(frame, _button_size, _buttons, _fonts, _call_back)

        _buttons = {
            "清除": (_pad_w+_button_size[0]*18, _pad_h*4+_button_size[1]*60),
        }
        _fonts = {
            "bg": "#6B6E70",
            "fg": "white",
            "bd": 2
        }
        self.create_buttons(frame, (_button_size[0]*2, _button_size[1]), _buttons, _fonts, \
            {"清除": lambda: self.press_clear("0")})

class Cashier:
    def create_vaiables(self):
        self.amount = StringVar()
        self.total = StringVar()
        self.cash_input = StringVar()
        self.change = StringVar()

        self.amount.set("0")
        self.total.set("0")
        self.cash_input.set("0")
        self.change.set("0")

    def create_casher(self, frame, frame_size):
        self.casher_frame = frame
        self.casher_width, self.casher_height = frame_size[0], frame_size[1]
        self._create_checkout_info()
        self._create_checkout_buttons()

    def _create_checkout_info(self):
        labels = {
            "數 量  : ": (0, self.casher_height*0.02),
            "總 計  : ": (0, self.casher_height*0.14),

            "現 金  : ": (0, self.casher_height*0.30),
            "找 零  : ": (0, self.casher_height*0.42),
        }
        _label_size = (self.casher_width*0.015, self.casher_height*0.003)
        self.create_labels(self.casher_frame, _label_size, labels)

        _split_line = {
            " "*5 + "—"*13:  (0, self.casher_height*0.22)
        }
        _line_size = (self.casher_width*0.04, self.casher_height*0.001)
        self.create_labels(self.casher_frame, _line_size, _split_line)

        var_dict = {
            "amount": (self.casher_width*0.23, self.casher_height*0.022),
            "total": (self.casher_width*0.23, self.casher_height*0.142),

            "cash_input": (self.casher_width*0.23, self.casher_height*0.300),
            "change": (self.casher_width*0.23, self.casher_height*0.422),
        }
        var_size = (self.casher_width*0.025, self.casher_height*0.003)
        
        self.create_variables(self.casher_frame, var_size, var_dict)

    def _create_checkout_buttons(self):
        _buttons = {
            "折扣": (self.casher_width*0.03, self.casher_height*0.54),
            "信用卡": (self.casher_width*0.36, self.casher_height*0.54),
            "小計": (self.casher_width*0.03, self.casher_height*0.72),
            "結帳": (self.casher_width*0.36, self.casher_height*0.72),
        }
        _button_size = (self.casher_width*0.015, self.casher_height*0.003)
        _fonts = {
            "bg": "white",
            "fg": "black",

        }
        self.create_buttons(self.casher_frame, _button_size, _buttons, _fonts, \
            call_back=self.change_button_color)