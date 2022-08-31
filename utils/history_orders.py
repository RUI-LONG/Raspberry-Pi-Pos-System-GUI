from os import listdir
from os.path import isfile, join
from datetime import datetime
from turtle import width
from .data_loader import read_json
from tkinter import Toplevel, Frame, Label, Button, OptionMenu

class OrderPanelCallBack:
    def change_order_date(self, *args):
        if self._search_date != args[0]:
            self._scroll_index = 0
            self._search_date = args[0]
            self.pase_order_data()
            self.create_order_panel()

    def exit_order_pannel(self):
        if self.order_window:
            self.order_window.destroy()
            self.order_window = None

    def scroll_left(self):
        if len(self.history_data) < 7:
            return
        self._scroll_index += 1
        if self._scroll_index > len(self.history_data)-7:
            self._scroll_index = len(self.history_data)-7
        self.pase_order_data(self._scroll_index)

    def scroll_right(self):
        if len(self.history_data) < 7:
            return
        self._scroll_index -= 1
        if self._scroll_index < 0:
            self._scroll_index = 0
        self.pase_order_data(self._scroll_index)

class OrderPanels(OrderPanelCallBack):
    def _create_date_label(self, frame):
        _text = ""
        date = datetime.now().strftime("%Y-%m-%d")
        self.date_select.set(date)
        _text += f"\n顯示日期:"
        _label = Label(frame, text=_text)
        _label.config(font=("Courier", 11))
        _label.pack(side='top', fill="both")

    def _get_file_list(self):
        _path = "./data/"
        files = [f for f in listdir(_path) if isfile(join(_path, f))]
        return [f.replace(".json", "") for f in files if f.endswith(".json")]
        
    def _create_option_menu(self, frame, width):
        options = self._get_file_list()
        date = datetime.now().strftime("%Y-%m-%d")
        options.append(date)
        options = list(set(options))
        menu = OptionMenu(frame, self.date_select, *options, \
            command=self.change_order_date)
        menu.config(width=width, height=int(self.window_height/200))
        menu.config(bd=3)
        menu.pack()

    def _create_labels(self, frame):
        _text = ""
        _text += f"\n當日訂單數: \n{len(self.history_data)}\n\n"
        
        _total = sum([int(r["total"]) for r in self.history_data])
        _text += f"\n當日營業額: \n${_total}\n"

        _label = Label(frame, text=_text)
        _label.config(font=("Courier", 11))
        _label.pack(side='top', fill="both")

    def _create_buttons(self, frame):
        button = Button(frame, bd=2, command=self.exit_order_pannel, \
            text="關閉", font=('Adobe 黑体 Std R', 20, 'normal'))
        button.pack(side='bottom')

        button = Button(frame, bd=4, command=self.scroll_left, \
            text="<", font=('Adobe 黑体 Std R', 25, 'normal'))
        button.pack(side='left')

        button = Button(frame, bd=4, command=self.scroll_right, \
            text=">", font=('Adobe 黑体 Std R', 25, 'normal'))
        button.pack(side='right')

    def create_order_panel(self):
        _frame = Frame(self.order_window, height=self.window_height, \
            width=self.panel_width, highlightthickness=2, highlightbackground="#6B6E70")
        _frame.pack_propagate(False)
        _frame.place(x=self.window_width-self.panel_width, y=0)
        self._create_date_label(_frame)
        self._create_option_menu(_frame, self.panel_width)
        self._create_labels(_frame)
        self._create_buttons(_frame)

class HistoryOrders(OrderPanels):
    def _parse_label(self, frame, data={}):
        _text = ""
        _text += f"\n 交易序號 {data.get('receipt_count', '')}\n"
        _text += f"{data.get('date', '')}\n {data.get('time', '')}\n\n"

        _receipt = data.get('receipt', {})
        for item, value in _receipt.items():
            if len(item) < 9:
                _text += f"\n{item} x {value[1]}\n"
            else:
                _text += f"\n{item[:9]}\n"
                _text += f"{item[9:]} x {value[1]}\n"
        _text += f"\n 金額 {data.get('total', '')} \n"
        _label = Label(frame, text=_text)
        _label.pack(side='top', fill="both")
        return _label

    def pase_order_data(self, index=0):
        self.history_data = read_json(f"./data/{self._search_date}.json")

        for n in range(7):
            _frame = Frame(self.order_window, height=self.window_height, \
                width=self.panel_width, highlightthickness=1, highlightbackground="#6B6E70")
            _frame.pack_propagate(False)
            _frame.place(x=self.panel_width*(7-n-1), y=0)
            if n < len(self.history_data):
                self._parse_label(_frame, self.history_data[len(self.history_data)-n-1-index])

    def create_order_window(self, root):
        if self.order_window:
            self._scroll_index = 0
            self.order_window.destroy()
            self.order_window = None
        else:
            self._scroll_index = 0
            self.order_window = Toplevel(root)
            self.order_window.attributes('-topmost', True)
            self.order_window.title('歷史訂單')
            
            self.window_width, self.window_height = int(self.max_w/2), int(self.max_h/2)
            center_x, center_y = int(self.max_w/4), int(self.max_h/4)
            self.order_window.geometry(f'{self.window_width}x{self.window_height}+{center_x}+{center_y}')
            self.order_window.focus_force()

            self.panel_width = int(self.window_width/8)

            self._search_date = datetime.now().strftime("%Y-%m-%d")
            self.pase_order_data()
            self.create_order_panel()
