from ..actions.general_act import GeneralActions

class TableCtrl(GeneralActions):
    def __init__(self):
        super().__init__()
        self._tables: dict = dict()

    # **************************************************************
    # ***************** Selection actions: Tables ******************
    # **************************************************************
    def move_table_selection_up(self, table_name: str, selection_index: int):
        """Move selection up

        Args:
            table_name (str): The table's name
            selection_index (int): The amount of times to move selection up
        """
        table_dict: dict = self.__get_object_act(table_name, "table")
        self.__move_selection_up_act(table_dict, selection_index)

    def move_table_selection_down(self, table_name: str, selection_index: int):
        """Move selection downward

        Args:
            table_name (str): The table's name
            selection_index (int): The amount of times to move selection down
        """
        table_dict: dict = self.__get_object_act(table_name, "table")
        self.__move_selection_down_act(table_dict, selection_index)
        
    def get_text_from_table(self, table_name: str) -> str:
        """Gets text from a dropdown menu

        Args:
            table_name (str): The dropdown menu's name
            
        Returns:
            str: The text string in the dropdown menu
        """
        table_dict: dict = self.__get_object_act(table_name, "table")
        table_label: str = self.__get_element_label_act(table_dict)
        return table_label

    # private methods        
    def __get_object_act(self, element_name: str, table_type: str) -> dict | None:
        """Gets the element's object

        Args:
            element_name (str): The element's name
            table_type (str): The table type
        
        Returns:
            dict | None: obj dict
        """
        elem_repo: dict | None = None

        match table_type:
            case "table":
                elem_repo = self._tables
            case _:
                pass

        if elem_repo is not None:
            elem_dict: dict | None = elem_repo.get(element_name, None)

            if elem_dict:
                return elem_dict
            else:
                print(f"{element_name} is not a valid input!")

        else:
            print(f"This window does not contain this table_type of control: {table_type}")
