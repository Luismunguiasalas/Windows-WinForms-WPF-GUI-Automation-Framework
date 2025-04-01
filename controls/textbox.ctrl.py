from ..actions.general_act import GeneralActions


class TextboxCtrl(GeneralActions):
    def __init__(self):
        super().__init__()
        self._textboxes: dict = dict()
    
    
    # public methods
    
    # **************************************************************
    # *************** Keyboard actions: Textbox ********************
    # **************************************************************    
    
    def set_focus_on_textbox(self, textbox_name: str) -> None:
        """Focus on a textbox

        Args:
            textbox_name (str): The textbox's name
        """
        textbox_dict: dict = self.__get_dict_act(textbox_name, "textbox")
        self.__set_element_focus_act(textbox_dict)
    
    def type_into_textbox(self, textbox_name: str, string_input: str) -> None:
        """Types text into a textbox

        Args:
            textbox_name (str): The textbox's name
            string_input (str): The text string to type into the textbox
        """
        textbox_dict: dict = self.__get_dict_act(textbox_name, "textbox")
        self.__type_string_act(textbox_dict, string_input)
    
    def delete_text_from_textbox(self, textbox_name: str) -> None:
        """Deletes text from a textbox

        Args:
            textbox_name (str): The textbox's name
        """
        textbox_dict: dict = self.__get_dict_act(textbox_name, "textbox")
        self.__delete_string_act(textbox_dict)
        
    def get_text_from_textbox(self, textbox_name: str) -> str:
        """Gets text from a textbox

        Args:
            textbox_name (str): The textbox's name
            
        Returns:
            str: The text string in the textbox
        """
        textbox_dict: dict = self.__get_dict_act(textbox_name, "textbox")
        textbox_label: str = self.__get_element_label_act(textbox_dict)
        return textbox_label
    
    def capture_textbox_as_image(self, textbox_name: str, test_id: str, image_name: str, baseline: bool) -> None:
        """Captures a textbox element as an image

        Args:
            test_id: The testcase id
            image_name: The image name
            baseline: True/False
            textbox_name (str): The textbox's name
        """
        textbox_dict: dict = self.__get_dict_act(textbox_name, "textbox")
        self.__capture_element_as_image_act(textbox_dict, test_id, image_name, baseline)


        
    # private methods
    
    def __get_dict_act(self, element_name: str, textbox_type: str) -> dict | None:
        """Gets the element's object

        Args:
            element_name (str): The element's name
            textbox_type (str): The textbox type
        
        Returns:
            dict | None: obj dict
        """
        elem_repo: dict | None = None

        match textbox_type:
            case "textbox":
                elem_repo = self._textboxes
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
            print(f"This window does not contain this textbox_type of control: {textbox_type}")
