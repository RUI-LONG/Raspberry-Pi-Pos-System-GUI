from tkinter import *

class CustomButtons:
    def set_all_button_fonts(self, font):
        self.font = font

    def exit_button(self, frame):
        _height = int(self.max_h*0.002)
        _width = int(self.max_w*0.003)
        Button(frame, command=self.root.destroy, \
            text="離開", font=self.font, \
            height=_height, width=_width).pack(pady=50, expand=True)

    def create_buttons(self, frame, text_list=[]):
        for i in range(len(text_list)):
            b = Button(frame, text=text_list[i])
            b.bind("<Button-1>", self.pressed)
            b.place(x=10,y=(10+(25*i)))

    def pressed(self, index):
        index.widget.configure(bg="red")


class Cashier:
    def init_casher(self):
        self.change_input = StringVar()
        self.cash_input = StringVar()
        self.total_input = StringVar()
        self.item = StringVar()
        self.amount = StringVar()
        self.choice = StringVar()

    