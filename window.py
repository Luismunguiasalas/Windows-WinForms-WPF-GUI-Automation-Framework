class Window():
    def __init__(self):
        pass
    
    
    
    # private methods
    def __get_object_act(self, name: str, type: str) -> object:
        """Gets the element's object

        Args:
            name (str): The element's name
            type (str): The button type
        
        Returns:
            object: button object
        """
        elem_repo: dict = None

        match type:
            case "button":
                elem_repo = self._buttons
            case "checkbox":
                elem_repo = self._checkboxes
            case "radio_button":
                elem_repo = self._radio_buttons
            case "label":                 
                elem_repo = self._labels
            case "textbox":               #TODO: add textbox selection methods
                elem_repo = self._textboxes
            case "coordinate":            #TODO: add coordinate selection methods
                elem_repo = self._coordinates
            case "table":                 #TODO: add table selection methods
                elem_repo = self._tables
            case "list":                  #TODO: add list selection methods
                elem_repo = self._lists
            case "menu":                  #TODO: add menu selection methods
                elem_repo = self._menus
            case _:
                pass

        if elem_repo is not None:
            elem_dict = elem_repo.get(name, False)

            if elem_dict:
                return elem_dict
            else:
                print(f"{name} is not a valid input!")
                #TODO: update the print statement
                print("Use the .PrintControlIdentifiers(controlType) to get a windows control names for a window's labels, buttons, textboxes, menus, elements, etc.")
                print()
        else:
            print(f"This window does not contain this type of control: {type}")