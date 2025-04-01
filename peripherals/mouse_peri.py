from ..controls import button_ctrl, coordinate_ctrl, draw_ctrl, label_ctrl, mousewheel_ctrl, dropdown_ctrl
class Mouse(button_ctrl.ButtonCtrl, coordinate_ctrl.CoordinateCtrl, draw_ctrl.DrawCtrl, label_ctrl.LabelCtrl, mousewheel_ctrl.MouseWheelCtrl, dropdown_ctrl.DropdownCtrl):
    def __init__(self):
        super().__init__()

