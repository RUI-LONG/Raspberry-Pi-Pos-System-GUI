from tkinter import *

class Calculator:
    def create_calculator(self, frame, frame_size):
        _width, _height = frame_size[0], frame_size[1]
        _button_size = (_width*0.013, _height*0.003)
        _pad_w = _width*0.06
        _pad_h = _height*0.12
        
        _buttons = {
                "7": (_pad_w, _pad_h),
                "8": (_pad_w*2+_button_size[0]*20, _pad_h),
                "9": (_pad_w*3+_button_size[0]*40, _pad_h),

                "6": (_pad_w, _pad_h*2+_button_size[1]*20),
                "5": (_pad_w*2+_button_size[0]*20, _pad_h*2+_button_size[1]*20),
                "4": (_pad_w*3+_button_size[0]*40, _pad_h*2+_button_size[1]*20),

                "3": (_pad_w, _pad_h*3+_button_size[1]*40),
                "2": (_pad_w*2+_button_size[0]*20, _pad_h*3+_button_size[1]*40),
                "1": (_pad_w*3+_button_size[0]*40, _pad_h*3+_button_size[1]*40),

                "0": (_pad_w, _pad_h*4+_button_size[1]*60),
                "*": (_pad_w*2+_button_size[0]*20, _pad_h*4+_button_size[1]*60),
                "BS": (_pad_w*3+_button_size[0]*40, _pad_h*4+_button_size[1]*60),
            }
        self.create_buttons(frame, _button_size, _buttons, "white")

class Cashier:
    def init_casher(self):
        self.change_input = StringVar()
        self.cash_input = StringVar()
        self.total_input = StringVar()
        self.item = StringVar()
        self.amount = StringVar()
        self.choice = StringVar()

    def create_casher(self, frame, frame_size):
        self.casher_frame = frame
        self.casher_width, self.casher_height = frame_size[0], frame_size[1]
        self._create_checkout_info()
        self._create_checkout_buttons()

    def _create_checkout_info(self):
        labels = {
            "數 量  : ": (self.casher_width*0.00, self.casher_height*0.02),
            "總 計  : ": (self.casher_width*0.00, self.casher_height*0.11),

            "現 金  : ": (self.casher_width*0.00, self.casher_height*0.30),
            "找 零  : ": (self.casher_width*0.00, self.casher_height*0.40),
        }

        _label_size = (self.casher_width*0.015, self.casher_height*0.003)
        self.create_labels(self.casher_frame, _label_size, labels)

        _split_line = {
            " "*5 + "-"*40:  (self.casher_width*0.00, self.casher_height*0.22)
        }
        _line_size = (self.casher_width*0.04, self.casher_height*0.001)
        self.create_labels(self.casher_frame, _line_size, _split_line)

        # self.cash = IntVar()
        # self.A.trace_add("write", self.calculate_sum)

    def change_button_color(self, index):
        index.widget.configure(bg="red")

    def _create_checkout_buttons(self):
        _buttons = {
            "折扣": (self.casher_width*0.03, self.casher_height*0.54),
            "信用卡": (self.casher_width*0.36, self.casher_height*0.54),
            "小計": (self.casher_width*0.03, self.casher_height*0.72),
            "結帳": (self.casher_width*0.36, self.casher_height*0.72),
        }
        _button_size = (self.casher_width*0.015, self.casher_height*0.003)
        self.create_buttons(self.casher_frame, _button_size, _buttons, "white", call_back=self.change_button_color)