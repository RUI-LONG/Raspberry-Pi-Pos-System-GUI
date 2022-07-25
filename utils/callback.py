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
        if self.receipt.get(item["name"]):
            _record_item = self.receipt[item["name"]]
            _index = _record_item[0]
            _unit = _record_item[1] + 1
            _price = int((_record_item[2] / _record_item[1]) * _unit)
            self.receipt_frame.item(int2hex(_index), text="blub", \
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
    
    def change_category(self):
        for _button in self.item_buttons:
            _button.grid_forget()
        selected_category = list(self.items.keys())[self.radio_var.get()]
        self.create_items(self.item_list_frame, selected_category)
