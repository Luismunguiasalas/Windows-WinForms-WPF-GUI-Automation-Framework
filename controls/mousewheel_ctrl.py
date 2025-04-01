from ..actions.general_act import GeneralActions

class MouseWheelCtrl(GeneralActions):
    def __init__(self):
        super().__init__()
        
    def scroll_mouse_wheel(self, amount: int):
        """Scroll mouse wheel up (pos value) \ down (neg value)

        Args:
            amount (int): Amount
        """
        self.__mouse_wheel_scroll_act(amount)
