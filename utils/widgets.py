from tkinter import *

class CustomButtons:
    def set_all_button_fonts(self, font):
        self.button_font = font

    def exit_button(self, frame, position=(50, 50)):
        _height = int(self.max_h*0.001)
        _width = int(self.max_w*0.002)
        exit_button = Button(frame, command=self.root.destroy, \
            text="離開", font=self.button_font, \
            height=_height, width=_width)
        exit_button.place(x=int(position[0]), y=int(position[1]))

    def create_buttons(self, frame, button_size, button_dict, bg, call_back=False):
        for k, v in button_dict.items():
            b = Button(frame, font=self.button_font, text=k, \
                height=int(button_size[1]), width=int(button_size[0]), bg=bg)
            if call_back:
                b.bind("<Button-1>", call_back)
            b.place(x=int(v[0]), y=int(v[1]))

class CustomLabels:
    def set_all_label_fonts(self, font):
        self.label_font = font

    def create_labels(self, frame, label_size, label_dict, font_dict=None):
        if not font_dict:
            font_dict = {
                "bg": "#404040",
                "fg": "#ffffff",
                "font": self.label_font
            }
        for k, v in label_dict.items():
            l = Label(frame, font=font_dict["font"], text=k, fg=font_dict["fg"], \
                height=int(label_size[1]), width=int(label_size[0]), bg=font_dict["bg"])
            l.place(x=int(v[0]), y=int(v[1]))

class CustomVariables:
    pass