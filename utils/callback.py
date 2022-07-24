class Callback:
    def change_button_color(self, index):
        index.widget.configure(bg="red")
        
    def press_number(self, item):
        try:
            if self.cash_input.get() == "0":
                self.cash_input.set(str(item))
            else:
                self.cash_input.set(self.cash_input.get()+str(item))
        except Exception as e:
            print(e)
            self.cash_input.set("Err")
    
    def press_clear(self, item):
        self.cash_input.set("0")
    
    def change_category(self):

        for _button in self.item_buttons:
            _button.grid_forget()
        selected_category = list(self.items.keys())[self.radio_var.get()]
        self.create_items(self.item_list_frame, selected_category)
