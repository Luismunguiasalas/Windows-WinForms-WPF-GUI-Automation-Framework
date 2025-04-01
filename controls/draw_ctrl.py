from ..actions.general_act import GeneralActions

class DrawCtrl(GeneralActions):
    def __init__(self):
        super().__init__()
        

    # **************************************************************
    # *************** Trace actions: Coordinates *******************
    # **************************************************************
    def trace_circle_at_coord(self, center_x: int, center_y: int, radius: int, speed: int):
        """Trace a circle

        Args:
            center_x (int): X coordinate
            center_y (int): Y coordinate
            radius (int): Radius of circle
            speed (int): Trace speed
        """
        self.__trace_circle_act(center_x, center_y, radius, speed)
        
    def trace_square_at_coord(self, center_x: int, center_y: int, radius: int, speed: int):
        """Trace a square

        Args:
            center_x (int): X coordinate
            center_y (int): Y coordinate
            radius (int): Radius of circle
            speed (int): Trace speed
        """
        self.__trace_square_act(center_x, center_y, radius, speed)
    
