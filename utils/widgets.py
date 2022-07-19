from tkinter import *

class CustomButtons:
    def set_all_button_fonts(self, font):
        self.font = font

    def exit_button(self, frame, position=(50, 50)):
        _height = int(self.max_h*0.001)
        _width = int(self.max_w*0.002)
        exit_button = Button(frame, command=self.root.destroy, \
            text="離開", font=self.font, \
            height=_height, width=_width)
        exit_button.place(x=int(position[0]), y=int(position[1]))

    def create_buttons(self, frame, button_size, button_dict):
        for k, v in button_dict.items():
            b = Button(frame, font=self.font, text=k, \
                height=int(button_size[1]), width=int(button_size[0]))
            b.bind("<Button-1>", self.pressed)
            b.place(x=int(v[0]), y=int(v[1]))

    def pressed(self, index):
        index.widget.configure(bg="red")

class Calculator:
    def create_calculator(self, frame, frame_size):
        _width, _height = frame_size[0], frame_size[1]
        _button_size = (_width*0.01, _height*0.003)
        _pad_w = _width*0.1
        _pad_h = _height*0.14
        
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
        self.create_buttons(frame, _button_size, _buttons)


class Cashier:
    def init_casher(self):
        self.change_input = StringVar()
        self.cash_input = StringVar()
        self.total_input = StringVar()
        self.item = StringVar()
        self.amount = StringVar()
        self.choice = StringVar()

    