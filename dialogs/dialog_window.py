from ..peripherals import keyboard_peri, mouse_peri

class DialogWindow(keyboard_peri.Keyboard, mouse_peri.Mouse):
    def __init__(self):
        super().__init__()


    # TODO: need to complete this print method, should call inherited control print method, depending on which control type is entered as an argument.
    def print_dlg_methods(self, control_type: str) -> str:
        match control_type:
            case "button":
                #TODO: call print method for the corresponding control type
                pass
            case "checkbox":
                pass
            case "radio_button":
                pass
            case "label":
                pass
            case "textbox":
                pass
            case "coordinate":
                pass
            case "dropdown":
                pass
            case "combobox":
                pass
            case "tables":
                pass
            case _:
                print("error handling code info")
                pass
        return "string"

