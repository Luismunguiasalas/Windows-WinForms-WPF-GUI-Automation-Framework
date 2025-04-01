from ..actions.general_act import GeneralActions
# 
class LabelCtrl(GeneralActions):
    def __init__(self):
        super().__init__()
        self._labels: dict = dict()
    
    # **************************************************************
    # ****************** String actions: Labels ********************
    # **************************************************************    

    def get_elem_label(self, element_name: str) -> str:
        """Gets an element's label

        Args:
            element_name (str): The element's name

        Returns:
            str: The element's text string
        """
        elem_dict: dict = self.__get_dict_act(element_name, "elements")
        elem_label: str = self.__get_element_label_act(elem_dict)
        return elem_label
    

    # private methods
    
    def __get_dict_act(self, element_name: str, label_type: str) -> dict | None:
        """Gets the element's object

        Args:
            element_name (str): The element name
            label_type (str): The label type
        
        Returns:
            dict | None: obj dict
        """
        elem_repo: dict | None = None

        match label_type:
            case "elements":
                elem_repo = self._labels
            case _:
                pass

        if elem_repo is not None:
            elem_dict: dict | None = elem_repo.get(element_name, None)

            if elem_dict:
                return elem_dict
            else:
                print(f"{element_name} is not a valid input!")
                #TODO: update the print statement
                # print("Use the .PrintControlIdentifiers(controlType) to get a windows control names for a window's labels, buttons, textboxes, menus, elements, etc.")
                # print()
        else:
            print(f"This window does not contain this label_type of control: {label_type}")
