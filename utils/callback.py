def int2hex(num):
    return "I" + str(hex(num)).upper().replace("0X", "").zfill(3)

class Callback:
    def change_button_color(self, index):
        index.widget.configure(bg="red")
        
    def press_number(self, item):
        try:
            if self.cash_input.get() == "0":
                self.cash_input.set(str(item))
            else:
                self.cash_input.set(self.cash_input.get()+str(item))
            
            if int(self.cash_input.get()) >= int(self.total.get()):
                self.change.set(str(int(self.cash_input.get())-int(self.total.get())))

        except Exception as e:
            print(e)
            self.cash_input.set("Err")
    
    def press_clear(self, item):
        self.cash_input.set("0")
        self.change.set("0")

    def press_item(self, item):
        # for press_option
        self.item = item
        if self.receipt.get(item["name"]):
            _record_item = self.receipt[item["name"]]
            _index = _record_item[0]
            _unit = _record_item[1] + 1
            _price = int((_record_item[2] / _record_item[1]) * _unit)
            _iid = self.receipt_frame.get_children()[_index-1]

            self.receipt_frame.item(_iid, text="blub", \
                values=(_index, item["name"], _unit, _price))

        else:
            _index = len(self.receipt) + 1
            _unit = 1
            _price = int(item["price"])

            # _values: (No Name Unit Amount)
            self.receipt_frame.insert('', 'end', text="1",
                values=(_index, item["name"], _unit, _price))

        self.receipt.update(
            {item["name"]: (_index, _unit, _price)}
        )

        self.unit.set(str(int(self.unit.get()) + 1))
        self.total.set(str(int(self.total.get()) + int(item["price"])))
    
    def press_option(self, option):
        if len(self.receipt) == 0:
            return
        elif option["name"] in self.item["name"]:
            return
        else:
            if "$" in option["name"]:
                option["name"] = option["name"][:option["name"].index("$")-1]
            _index = len(self.receipt)
            _record_item = self.receipt[self.item["name"]]
            _unit = _record_item[1]
            _price = _record_item[2]
            _name_with_option = self.item["name"] + " "+ option["name"]
            _iid = self.receipt_frame.get_children()[_index-1]

            self.receipt_frame.item(_iid, text="blub", \
                values=(_index, _name_with_option, \
                    _unit, _price))


            self.receipt.pop(self.item["name"], None)
            self.item = {"name": _name_with_option, "price": _price}
            self.receipt.update({_name_with_option: (_index, _unit, _price)})

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