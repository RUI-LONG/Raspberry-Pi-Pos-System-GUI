from tkinter import *

class CustomButtons:
    def set_all_button_fonts(self, font):
        self.button_font = font

    def create_exit_button(self, frame, position=(50, 50)):
        _height = int(self.max_h*0.001)
        _width = int(self.max_w*0.002)
        exit_button = Button(frame, command=self.root.destroy, \
            text="離開", font=self.button_font, \
            height=_height, width=_width)
        exit_button.place(x=int(position[0]), y=int(position[1]))

    def _handle_font_dict(self, font_dict):
        if font_dict:
            return {
                "bg": font_dict.get("bg", "#404040"),
                "fg": font_dict.get("fg", "#ffffff"),
                "font": font_dict.get("font", self.button_font),
                "bd": font_dict.get("bd", 0)
            }
        else:
            return {
                "bg": "#404040",
                "fg": "#ffffff",
                "font": self.button_font,
                "bd": 0
            }

    def place_buttons(self, frame, button_size, button_dict, font_dict=None, call_back=False):
        font_dict = self._handle_font_dict(font_dict)

        for k, v in button_dict.items():
            if isinstance(call_back, dict):
                _button = Button(frame, font=font_dict["font"], text=k, \
                    height=int(button_size[1]), width=int(button_size[0]), \
                    bg=font_dict["bg"], fg=font_dict["fg"], bd=font_dict["bd"],\
                    anchor="center", command = call_back[k])
            else:
                _button = Button(frame, font=font_dict["font"], text=k, \
                    height=int(button_size[1]), width=int(button_size[0]), \
                    bg=font_dict["bg"], fg=font_dict["fg"], bd=font_dict["bd"])
                if call_back:
                    _button.bind("<Button-1>", call_back)
            _button.place(x=int(v[0]), y=int(v[1]))

    def grid_buttons(self, frame, button_size, button_dict, font_dict=None, call_back=False):
        font_dict = self._handle_font_dict(font_dict)
        _grid_buttons = []

        for k, v in button_dict.items():
            if isinstance(call_back, dict):
                _button = Button(frame, font=font_dict["font"], text=k, \
                    height=int(button_size[1]), width=int(button_size[0]), \
                    bg=font_dict["bg"], fg=font_dict["fg"], bd=font_dict["bd"],\
                    anchor="center", command = call_back[k])
            else:
                _button = Button(frame, font=font_dict["font"], text=k, \
                    height=int(button_size[1]), width=int(button_size[0]), \
                    bg=font_dict["bg"], fg=font_dict["fg"], bd=font_dict["bd"])
                if call_back:
                    _button.bind("<Button-1>", call_back)
            _button.grid(row=v[0], column=v[1], padx=v[2], pady=v[3])
            _grid_buttons.append(_button)
        return _grid_buttons

    def create_radio_buttons(self, frame, button_size, button_dict, font_dict=None, call_back=False):
        font_dict = self._handle_font_dict(font_dict)
        _foo = 0

        for k, v in button_dict.items():
            if isinstance(call_back, dict):
                _button = Radiobutton(frame, font=font_dict["font"], text=k, \
                    height=int(button_size[1]), width=int(button_size[0]), \
                    bg=font_dict["bg"], fg=font_dict["fg"], bd=font_dict["bd"],\
                    anchor="center", command = call_back[k], \
                    variable=self.radio_var, value=_foo, indicatoron=0)
            else:
                _button = Radiobutton(frame, font=font_dict["font"], text=k, \
                    height=int(button_size[1]), width=int(button_size[0]), \
                    bg=font_dict["bg"], fg=font_dict["fg"], bd=font_dict["bd"], \
                    variable=self.radio_var, value=_foo, indicatoron=0)
                if call_back:
                    _button.bind("<Button-1>", call_back)
            _button.place(x=int(v[0]), y=int(v[1]))
            _foo += 1
            
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
            _label = Label(frame, font=font_dict["font"], text=k, fg=font_dict["fg"], \
                height=int(label_size[1]), width=int(label_size[0]), bg=font_dict["bg"])
            _label.place(x=int(v[0]), y=int(v[1]))

class CustomVariables:
    def create_variables(self, frame, var_size, var_dict=None, font_dict=None):
        if not font_dict:
            font_dict = {
                "bg": "#ffffff",
                "fg": "#404040",
                "font": self.label_font
            }
        for k, v in var_dict.items():
            _var = Label(frame, textvariable=getattr(self, k), \
                font=font_dict["font"], text=k, fg=font_dict["fg"], \
                height=int(var_size[1]), width=int(var_size[0]), bg=font_dict["bg"], \
                anchor="e"
            )
            _var.place(x=int(v[0]), y=int(v[1]))
