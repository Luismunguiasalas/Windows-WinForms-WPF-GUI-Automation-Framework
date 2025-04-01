from ..actions.general_act import GeneralActions

class ComboboxCtrl(GeneralActions):
    def __init__(self):
        super().__init__()
        self._comboboxes: dict = dict()
        
        
    # **************************************************************
    # *************** Selection actions: ComboBox ******************
    # **************************************************************        
    def combobox_selection(self, combobox_name: str, selections: list[str]):
        combobox_dict: dict = self.__get_object_act(combobox_name, "combobox")
        self.__element_navigation_act(combobox_dict, selections)
        
    def type_into_combobox(self, combobox_name: str, string_input: str) -> None:
        """Types text into a textbox

        Args:
            combobox_name (str): The combobox name
            string_input (str): The text string to type into the combobox
        """
        textbox_dict: dict = self.__get_object_act(combobox_name, "combobox")
        self.__type_string_act(textbox_dict, string_input)
        
    def get_text_from_combobox(self, combobox_name: str) -> str:
        """Gets text from a combobox

        Args:
            combobox_name (str): The combobox name

        Returns:
            str: The text string in the combobox menu
        """
        combobox_dict: dict = self.__get_object_act(combobox_name, "textbox")
        combobox_label: str = self.__get_element_label_act(combobox_dict)
        return combobox_label
    
    def delete_text_from_combobox(self, combobox_name: str) -> None:
        """Deletes text from a combobox

        Args:
            combobox_name (str): The combobox name
        """
        combobox_dict: dict = self.__get_object_act(combobox_name, "combobox")
        self.__delete_string_act(combobox_dict)
        
    # private methods        
    def __get_object_act(self, element_name: str, combobox_type: str) -> dict | None:
        """Gets the element's object

        Args:
            element_name (str): The element's name
            combobox_type (str): The combobox type
        
        Returns:
            dict | None: obj dict
        """
        elem_repo: dict | None = None

        match combobox_type:
            case "combobox":
                elem_repo = self._comboboxes
            case _:
                pass

        if elem_repo is not None:
            elem_dict: dict | None = elem_repo.get(element_name, None)

            if elem_dict:
                return elem_dict
            else:
                print(f"{element_name} is not a valid input!")

        else:
            print(f"This window does not contain this combobox_type of control: {combobox_type}")
