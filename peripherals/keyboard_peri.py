from ..controls import combobox_ctrl, textbox_ctrl, table_ctrl

class Keyboard(combobox_ctrl.ComboboxCtrl, textbox_ctrl.TextboxCtrl, table_ctrl.TableCtrl):
    def __init__(self):
        super().__init__()