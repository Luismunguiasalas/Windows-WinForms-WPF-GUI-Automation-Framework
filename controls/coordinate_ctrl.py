from ..actions.general_act import GeneralActions

class CoordinateCtrl(GeneralActions):
    def __init__(self):
        super().__init__()
        self._elements: dict = dict()
        
    # **************************************************************
    # *************** Mouse actions: Coordinates *******************
    # **************************************************************
    # public methods

    #TODO: update the arguments of these methods, so that it takes actual x/y coordinates
    def left_mouse_click_element_coord(self, element_name: str) -> None:
        """Left mouse click at x/y coordinate

        Args:
            element_name (str): The elements name
        """
        elem_dict: dict = self.__get_dict_act(element_name, "elements")
        self.__left_mouse_click_coordinates_act(elem_dict)
        
    def double_left_mouse_click_element_coord(self, element_name: str) -> None:
        """Double left mouse click at x/y coordinate

        Args:
            element_name (str): The element's name
        """
        elem_dict: dict = self.__get_dict_act(element_name, "elements")
        self.__double_left_mouse_click_coordinates_act(elem_dict)
                
    # private methods
    def __get_dict_act(self, element_name: str, coordinate_type: str) -> dict | None:
        """Gets the element's object

        Args:
            element_name (str): The element's name
            coordinate_type (str): The coordinate type
        
        Returns:
            dict | None: obj dict
        """
        elem_repo: dict | None = None

        match coordinate_type:
            case "elements":
                elem_repo = self._elements
            case _:
                pass

        if elem_repo is not None:
            elem_dict: dict | None = elem_repo.get(element_name, None)

            if elem_dict:
                return elem_dict
            else:
                print(f"{element_name
                } is not a valid input!")
        else:
            print(f"This window does not contain this type of control: {coordinate_type}")
