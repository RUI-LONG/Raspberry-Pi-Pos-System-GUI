from tkinter import *

class Calculator:
    def create_calculator(self, frame):
        _width, _height = frame["width"], frame["height"]
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
        
        _lambda_fcns = [lambda i=i:self.press_number(str(i)) for i in range(10)]
        _call_back = dict(zip([str(i) for i in range(10)], _lambda_fcns))

        _fonts = {
            "bg": "white",
            "fg": "black",
            "bd": 2
        }
        self.place_buttons(frame, _button_size, _buttons, _fonts, _call_back)

        _buttons = {
            "清除": (_pad_w+_button_size[0]*18, _pad_h*4+_button_size[1]*60),
        }
        _fonts = {
            "bg": "#6B6E70",
            "fg": "white",
            "bd": 2
        }
        self.place_buttons(frame, (_button_size[0]*2, _button_size[1]), _buttons, _fonts, \
            {"清除": lambda: self.press_clear("0")})

class Cashier:
    def create_vaiables(self):
        self.unit = StringVar()
        self.total = StringVar()
        self.cash_input = StringVar()
        self.change = StringVar()

        self.unit.set("0")
        self.total.set("0")
        self.cash_input.set("0")
        self.change.set("0")
        
        # for treeview selection
        self.receipt = dict()

        # for selcet category
        self.radio_var = IntVar()
        self.radio_var.set(0)

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

        _position_x = self.casher_width*0.23
        var_dict = {
            "unit": (_position_x, self.casher_height*0.022),
            "total": (_position_x, self.casher_height*0.142),

            "cash_input": (_position_x, self.casher_height*0.3),
            "change": (_position_x, self.casher_height*0.422),
        }
        var_size = (self.casher_width*0.025, self.casher_height*0.003)
        self.create_variables(self.casher_frame, var_size, var_dict)

    def _create_checkout_buttons(self):
        _grid_x0, _grid_y0 = self.casher_width*0.03, self.casher_height*0.54
        _grid_x1, _grid_y1 = self.casher_width*0.36, self.casher_height*0.72

        _buttons = {
            "折扣": (_grid_x0, _grid_y0),
            "信用卡": (_grid_x1, _grid_y0),
            "小計": (_grid_x0, _grid_y1),
            "結帳": (_grid_x1, _grid_y1),
        }
        _button_size = (self.casher_width*0.015, self.casher_height*0.003)
        _fonts = {
            "bg": "white",
            "fg": "black",
        }
        self.place_buttons(self.casher_frame, _button_size, _buttons, _fonts, \
            call_back=self.change_button_color)

class Merchandise:
    def create_category(self, frame):
        _width, _height = frame["width"], frame["height"]
        _button_size = (int(_width*0.03), int(_height*0.004))
        _pos_x, _pos_y = _button_size[0]*5, _button_size[1]*18

        _buttons = {
                _category: (_pos_x + _button_size[0], _pos_y + _button_size[1]*i*70)
                for i, _category in enumerate(self.items.keys())
            }
        _call_back = {
            _category: self.change_category for _category in self.items.keys()
        }
        _fonts = {
            "bg": "white",
            "fg": "black",
            "bd": 10
        }
        self.create_radio_buttons(frame, _button_size, _buttons, _fonts, _call_back)

    def _iter_items(self, item_list, pads, call_back_fcn, row_max=3):
        _output_dict = {}
        _x, _y = 0, 0
        for item in item_list:
            if _y > row_max:
                _x, _y = _x+1, 0
            _output_dict[item["name"]] = (_x, _y, pads[0], pads[1])
            _y += 1

        _lambda_fcns = [lambda i=i:call_back_fcn(i) for i in item_list]
        _call_back = dict(zip([i["name"] for i in item_list], _lambda_fcns))

        return _output_dict, _call_back


    def create_items(self, frame, selected_category):
        _width, _height = frame["width"], frame["height"]
        _padx, _pady = (int(_width*0.02), int(_height*0.02))
        _button_size = (int(_width*0.01), int(_height*0.007))

        _buttons, _call_back = self._iter_items(self.items[selected_category], \
            (_padx, _pady), self.press_item)

        _fonts = {
            "bg": "white",
            "fg": "black",
            "bd": 1
        }
        self.item_buttons = self.grid_buttons(frame, _button_size, _buttons, _fonts, _call_back)

    def create_options(self, frame, selected_category):
        _width, _height = frame["width"], frame["height"]
        _padx, _pady = (int(_width*0.02), int(_height*0.02))
        _button_size = (int(_width*0.02), int(_height*0.005))

        _buttons, _call_back = self._iter_items(self.options[selected_category], \
            (_padx, _pady), self.press_option, row_max=1)

        _fonts = {
            "bg": "white",
            "fg": "black",
            "bd": 1
        }
        self.option_buttons = self.grid_buttons(frame, _button_size, _buttons, _fonts, _call_back)

class Receipt:
    def create_receipt(self, frame):
        _width, _height = frame["width"], frame["height"]
        tree_size = (int(_width*0.1), int(_height*0.043))
        frame.pack_propagate(False)

        tree_dict = {
            'No': (tree_size[0], "No"), 
            'Name': (int(tree_size[0]*6.5), "名稱"), 
            'Unit': (tree_size[0], "數量"), 
            'Amount': (tree_size[0], "小記")
        }

        _font = ('Adobe 黑体 Std R', 20, 'normal')
        self.receipt_frame = self.create_treeview(frame, tree_size, tree_dict, _font)
