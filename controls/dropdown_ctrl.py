from ..actions.general_act import GeneralActions

class DropdownCtrl(GeneralActions):
    def __init__(self):
        super().__init__()
        self._dropdowns: dict = dict()

    # **************************************************************
    # *************** Selection actions: dropdown ******************
    # **************************************************************
    def dropdown_menu_selection(self, dropdown_menu_name, selections: list[str]):
        """Select an item or nested items from the dropdown menu

        Args:
            dropdown_menu_name: The dropdown menu's name
            selections: The available selections in the dropdown menu
        """
        dropdown_menu_dict: dict = self.__get_dict_act(dropdown_menu_name, "dropdown")
        self.__element_navigation_act(dropdown_menu_dict, selections)

    def get_text_from_dropdown_menu(self, dropdown_menu_name: str) -> str:
        """Gets text from a dropdown menu

        Args:
            dropdown_menu_name (str): The dropdown menu's name
            
        Returns:
            str: The text string in the dropdown menu
        """
        dropdown_menu_dict: dict = self.__get_dict_act(dropdown_menu_name, "textbox")
        dropdown_menu_label: str = self.__get_element_label_act(dropdown_menu_dict)
        return dropdown_menu_label

    # private methods        
    def __get_dict_act(self, element_name: str, dropdown_type: str) -> dict | None:
        """Gets the element's object

        Args:
            element_name (str): The element name
            dropdown_type (str): The dropdown type
        
        Returns:
            dict | None: obj dict
        """
        elem_repo: dict | None = None

        match dropdown_type:
            case "dropdown":
                elem_repo = self._dropdowns
            case _:
                pass

        if elem_repo is not None:
            elem_dict: dict | None = elem_repo.get(element_name, None)

            if elem_dict:
                return elem_dict
            else:
                print(f"{element_name} is not a valid input!")

        else:
            print(f"This window does not contain this dropdown_type of control: {dropdown_type}")
