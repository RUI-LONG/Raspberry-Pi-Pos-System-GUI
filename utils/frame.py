from tkinter import *
from .widgets import CustomButtons, CustomLabels, CustomVariables, CustomTreeview
from .components import Calculator, Cashier, Merchandise, Receipt
from .callback import Callback

class frameSettings(CustomButtons, CustomLabels, CustomVariables, CustomTreeview, \
        Callback, Calculator, Cashier, Merchandise, Receipt):
    def set_all_frames(self):
        # 1 layer
        self.seperate_main_frame()

        # 2 layer upper frame
        self.set_category_frame()
        self.set_item_list_frame()
        self.set_options_frame()
        
        # 2 layer lower frame
        self.set_receipt_frame()
        self.set_calculator_frame()
        self.set_checkout_frame()

    def seperate_main_frame(self):
        self.main_frame = Frame(self.root, bg="#050505")
        self.main_frame.grid(padx=0, pady=0)
        
        # Seperate to upper & lower frame
        self.h_parition = int(self.max_h*0.45)
        self.lower_parition = int(self.max_h-self.h_parition)

        self.lower_frame = Frame(self.main_frame, bd=0, \
            width=self.max_w, height=self.h_parition, bg="#050505")
        self.lower_frame.pack(side="bottom")

        self.upper_frame = Frame(self.main_frame, bd=0, \
            width=self.max_w, height=self.lower_parition, bg="#050505")
        self.upper_frame.pack(side="bottom")

    def set_category_frame(self):
        _width = self.max_w*0.1
        category_frame = LabelFrame(self.upper_frame, bd=5, \
            width=int(_width), height=self.lower_parition, \
            bg="#404040", cursor="circle", fg="#FFFFFF", relief="flat")
        category_frame.grid(row=0, column=0, padx=15, pady=15)

        self.create_category(category_frame)

    def set_item_list_frame(self):
        self.item_frame_width = self.max_w*0.65
        self.item_list_frame = Frame(self.upper_frame, bd=5, \
            width=int(self.item_frame_width), height=self.lower_parition, \
            bg="#6B6E70", cursor="circle")
        self.item_list_frame.grid(row=0, column=1, padx=0, pady=15)
        self.item_list_frame.grid_propagate(False)

        selected_category = list(self.items.keys())[self.radio_var.get()]
        self.create_items(self.item_list_frame, selected_category)

    def set_options_frame(self):
        _width = self.max_w*0.25
        self.options_frame = Frame(self.upper_frame, bd=5, \
            width=int(_width), height=self.lower_parition, \
            bg="#404040", cursor="circle")
        self.options_frame.grid(row=0, column=2, padx=15, pady=15)
        self.options_frame.grid_propagate(False)
        
        selected_category = list(self.items.keys())[self.radio_var.get()]
        self.create_options(self.options_frame, selected_category)

    def set_receipt_frame(self):
        _width = self.max_w*0.4
        receipt_frame = LabelFrame(self.lower_frame, bd=5, \
            width=int(_width), height=self.h_parition, \
            bg="white", relief="flat")
        receipt_frame.grid(row=0, column=0, padx=15, pady=0)
        self.create_receipt(receipt_frame)

    def set_calculator_frame(self):
        _width = int(self.max_w*0.3)
        _height = int(self.h_parition*0.2)
        function_frame = Frame(self.lower_frame, bd=0, \
            width=_width, height=_height, \
            bg="#050505", cursor="circle")
        function_frame.grid(row=0, column=1, padx=0, pady=0, sticky="n")
        function_frame.grid_propagate(False)

        calculator_frame = Frame(self.lower_frame, bd=0, \
            width=_width, height=int(self.h_parition-_height), \
            bg="#050505", cursor="circle")
        calculator_frame.grid(row=0, column=1, padx=0, pady=0, sticky="s")

        calculator_frame.grid_propagate(False)
        self.create_calculator(calculator_frame)
        self.create_function_buttons(function_frame)

    def set_checkout_frame(self):
        _width = self.max_w*0.3
        checkout_frame = Frame(self.lower_frame, bd=5, \
            width=int(_width), height=self.h_parition, \
            bg="#404040", cursor="circle")
        checkout_frame.grid(row=0, column=2, padx=15, pady=0)

        checkout_frame.grid_propagate(False)
        self.create_casher(checkout_frame, (_width, self.h_parition))
        self.create_exit_button(checkout_frame, (_width*0.70, self.h_parition*0.03))
        self.create_clear_receipt_button(checkout_frame, (_width*0.70, self.h_parition*0.26))
