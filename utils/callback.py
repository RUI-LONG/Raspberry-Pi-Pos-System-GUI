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