def int2hex(num):
    return "I" + str(hex(num)).upper().replace("0X", "").zfill(3)

class Callback:
    def change_button_color(self, index):
        index.widget.configure(bg="red")
        
    def press_number(self, item):
        try:
            if self.cash_input.get() == "0":
                if item == "00":
                    item = 0
                self.cash_input.set(str(item))
            else:
                self.cash_input.set(self.cash_input.get()+str(item))
            
            self.change.set(str(int(self.cash_input.get())-int(self.total.get())))

        except Exception as e:
            print(e)
            self.cash_input.set("Err")
    
    def cal_unit_and_total(self):
        self.unit.set(str(sum([k[1] for k in self.receipt.values()])))
        self.total.set(str(sum([k[2] for k in self.receipt.values()])))
        self.change.set(str(int(self.cash_input.get())-int(self.total.get())))
    
    def press_clear(self, item):
        self.cash_input.set("0")
        self.change.set("0")

    def press_item(self, item):
        if self.receipt.get(item["name"]):
            _record_item = self.receipt[item["name"]]
            _index = _record_item[0]
            _unit = _record_item[1] + 1
            _price = int((_record_item[2] / _record_item[1]) * _unit)
            _iid = _record_item[3]
            self.receipt_frame.item(_iid, text="blub", \
                values=(_index, item["name"], _unit, _price))

        else:
            _index = len(self.receipt) + 1
            _unit = 1
            _price = int(item["price"])

            # _values: (No Name Unit Amount)
            _iid = self.receipt_frame.insert('', 'end', text="1",
                values=(_index, item["name"], _unit, _price))

        self.receipt.update(
            {item["name"]: (_index, _unit, _price, _iid)}
        )
        self.cal_unit_and_total()

    def add_n_item(self, n=1):
        selected_item = self.receipt_frame.selection()
        if len(selected_item) > 0:
            _name = self.receipt_frame.item(selected_item[0])["values"][1]
        elif len(self.receipt_frame.get_children()) > 0:
            _name = self.receipt_frame.item(self.receipt_frame.get_children()[-1])["values"][1]
        else:
            return

        if self.receipt.get(_name):
            _index, _unit, _price, _iid = self.receipt.get(_name)
            _new_unit = _unit + n
            _new_price = int((_price / _unit) * _new_unit)
            self.receipt_frame.item(_iid, text="blub", \
                    values=(_index, _name, _new_unit, _new_price))
            self.receipt.update(
                {_name: (_index, _new_unit, _new_price, _iid)}
            )
        self.cal_unit_and_total()                

    def minus_one_item(self):
        selected_item = self.receipt_frame.selection()
        if len(selected_item) > 0:
            _name = self.receipt_frame.item(selected_item[0])["values"][1]
        elif len(self.receipt_frame.get_children()) > 0:
            _name = self.receipt_frame.item(self.receipt_frame.get_children()[-1])["values"][1]
        else:
            return
        if self.receipt.get(_name):
            _item = self.receipt.get(_name)
            if _item[1] <= 1:
                self.delete_item()
            else:
                self.add_n_item(-1)
        self.cal_unit_and_total()

    def delete_item(self):
        selected_item = self.receipt_frame.selection()
        if len(selected_item) > 0:
            _loc = selected_item[0]
            _name = self.receipt_frame.item(selected_item[0])["values"][1]
        elif len(self.receipt_frame.get_children()) > 0:
            _loc = self.receipt_frame.get_children()[-1]
            _name = self.receipt_frame.item(_loc)["values"][1]
        else:
            return
        self.receipt_frame.delete(_loc)
        self.receipt.pop(_name, None)
        self.cal_unit_and_total()
    
    def press_option(self, option):
        if len(self.receipt) == 0:
            return
        if "$" in option["name"]:
            option["name"] = option["name"][:option["name"].index("$")-1]

        selected_item = self.receipt_frame.selection()

        if len(selected_item) > 0:
            _name = self.receipt_frame.item(selected_item[0])["values"][1]
        else:
            _name = self.receipt_frame.item(self.receipt_frame.get_children()[-1])["values"][1]
        if option["name"] in _name:
            return

        _index, _unit, _price, _iid = self.receipt.get(_name)
        _name_with_option = _name + " "+ option["name"]
        
        self.receipt_frame.item(_iid, text="blub", \
            values=(_index, _name_with_option, \
                _unit, _price))

        self.receipt.pop(_name, None)
        self.receipt.update({_name_with_option: (_index, _unit, _price, _iid)})
        self.cal_unit_and_total()

    def change_category(self):
        for _button in self.item_buttons:
            _button.grid_forget()
        
        for _button in self.option_buttons:
            _button.grid_forget()
        selected_category = list(self.items.keys())[self.radio_var.get()]
        self.create_items(self.item_list_frame, selected_category)
        self.create_options(self.options_frame, selected_category)

    def clear_receipt(self):
        for item in self.receipt_frame.get_children():
            self.receipt_frame.delete(item)
        self.receipt = dict()
        self.cal_unit_and_total()
        self.change.set("0")
        self.cash_input.set("0")