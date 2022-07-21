from tkinter import *
from .widgets import CustomButtons, CustomLabels, CustomVariables
from .components import Calculator, Cashier
from .callback import Callback

class frameSettings(CustomButtons, CustomLabels, CustomVariables, Callback, Calculator, Cashier):
    def set_all_frames(self):
        # 1 layer
        self.seperate_main_frame()
        
        # 2 layer upper frame
        self.set_category_frame()
        self.set_goods_list_frame()
        self.set_options_frame()

        # 2 layer lower frame
        self.set_check_list_frame()
        self.set_calculator_frame()
        self.set_checkout_frame()

    def set_all_category_fonts(self, font):
        self.category_font = font

    def seperate_main_frame(self):
        self.main_frame = Frame(self.root, bg="#050505")
        self.main_frame.grid(padx=0, pady=0)
        
        # Seperate to upper & lower frame
        self.h_parition = self.max_h*0.45
        self.lower_frame = Frame(self.main_frame, bd=0, \
            width=self.max_w, height=int(self.h_parition), bg="#050505")
        self.lower_frame.pack(side="bottom")

        self.upper_frame = Frame(self.main_frame, bd=0, \
            width=self.max_w, height=int(self.max_h-self.h_parition), bg="#050505")
        self.upper_frame.pack(side="bottom")

    def set_category_frame(self):
        _width = self.max_w*0.2
        self.category_frame = LabelFrame(self.upper_frame, bd=5, \
            width=int(_width), height=int(self.max_h-self.h_parition), \
            bg="#404040", font=self.category_font, fg="#FFFFFF", text="類別", relief="flat")
        self.category_frame.grid(row=0, column=0, padx=15, pady=15)

    def set_goods_list_frame(self):
        _width = self.max_w*0.6
        goods_list_frame = Frame(self.upper_frame, bd=5, \
            width=int(_width), height=int(self.max_h-self.h_parition), \
            bg="#6B6E70", cursor="circle")
        goods_list_frame.grid(row=0, column=1, padx=0, pady=15)

    def set_options_frame(self):
        _width = self.max_w*0.2
        options_frame = Frame(self.upper_frame, bd=5, \
            width=int(_width), height=int(self.max_h-self.h_parition), \
            bg="#404040", cursor="circle")
        options_frame.grid(row=0, column=2, padx=15, pady=15)

    def set_check_list_frame(self):
        _width = self.max_w*0.4
        self.check_list_frame = LabelFrame(self.lower_frame, bd=5, \
            width=int(_width), height=int(self.h_parition), \
            bg="#6B6E70", font=self.category_font, text="類別", relief="flat")
        self.check_list_frame.grid(row=0, column=0, padx=15, pady=10)

    def set_calculator_frame(self):
        _width = self.max_w*0.3
        calculator_frame = Frame(self.lower_frame, bd=5, \
            width=int(_width), height=int(self.h_parition), \
            bg="#6B6E70", cursor="circle")
        calculator_frame.grid(row=0, column=1, padx=0, pady=10)

        # 7 = (padx/2)
        frame_size = (_width, self.h_parition)
        self.create_calculator(calculator_frame, frame_size)

    def set_checkout_frame(self):
        _width = self.max_w*0.3
        checkout_frame = Frame(self.lower_frame, bd=5, \
            width=int(_width), height=int(self.h_parition), \
            bg="#404040", cursor="circle")
        checkout_frame.grid(row=0, column=2, padx=15, pady=10)


        self.create_casher(checkout_frame, (_width, self.h_parition))

        self.exit_button(checkout_frame, (_width*0.72, self.h_parition*0.03))
    


