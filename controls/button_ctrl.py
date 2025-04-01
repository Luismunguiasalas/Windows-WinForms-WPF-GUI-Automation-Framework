from ..actions.general_act import GeneralActions


class ButtonCtrl(GeneralActions):
    def __init__(self) -> None:
        super().__init__()
        self._buttons: dict = dict()
        self._checkboxes: dict = dict()
        self._radio_buttons: dict = dict()
        self._control_names: dict = dict()
        
    # public methods

    # methods that support clicking the mouse in order to select a button
    # **************************************************************
    # ****************** Mouse actions: Buttons ********************
    # **************************************************************
    def left_mouse_click_btn(self, button_name: str) -> None:
        """Left mouse click a button

        Args:
            button_name (str): The button's name
        """
        button_dict: dict = self.__get_dict_act(button_name, "button")
        self.__left_mouse_click_act(button_dict)
    
    def right_mouse_click_btn(self, button_name: str) -> None:
        """Right mouse click a button

        Args:
            button_name (str): The button's name
        """
        button_dict: dict = self.__get_dict_act(button_name, "button")
        self.__right_mouse_click_act(button_dict)

    def double_left_mouse_click_btn(self, button_name: str) -> None:
        """Double left mouse click a button

        Args:
            button_name (str): The button's name
        """
        button_dict: dict = self.__get_dict_act(button_name, "button")
        self.__double_left_mouse_click_act(button_dict)

    def get_button_label(self, button_name: str) -> str:
        """Get a button's text string

        Args:
            button_name (str): The button's name

        Returns:
            str: The button's text string
        """
        button_dict: dict = self.__get_dict_act(button_name, "button")
        button_label: str = self.__get_element_label_act(button_dict)
        return button_label

    def left_mouse_click_btn_coord(self, button_name: str) -> None:
        """Left mouse click at x/y coordinate

        Args:
            button_name (str): The buttons name
        """
        elem_dict: dict = self.__get_dict_act(button_name, "button")
        self.__left_mouse_click_coordinates_act(elem_dict)

    def double_left_mouse_click_btn_coord(self, button_name: str) -> None:
        """Double left mouse click at x/y coordinate

        Args:
            button_name (str): The button's name
        """
        elem_dict: dict = self.__get_dict_act(button_name, "button")
        self.__double_left_mouse_click_coordinates_act(elem_dict)


    # methods that support clicking the mouse in order to select a checkbox
    # **************************************************************
    # ****************** Mouse actions: Checkbox *******************
    # **************************************************************
    def left_mouse_click_checkbox(self, checkbox_name: str) -> None:
        """Left mouse click a checkbox

        Args:
            checkbox_name (str): The checkboxes name
        """
        checkbox_dict: dict = self.__get_dict_act(checkbox_name, "checkbox")
        self.__left_mouse_click_act(checkbox_dict)

    def right_mouse_click_checkbox(self, checkbox_name: str) -> None:
        """Right mouse click a  checkbox


        Args:
            checkbox_name (str): The checkboxes name
        """
        checkbox_dict: dict = self.__get_dict_act(checkbox_name, "checkbox")
        self.__right_mouse_click_act(checkbox_dict)

    def double_left_mouse_click_checkbox(self, checkbox_name: str) -> None:
        """Double left mouse click a checkbox

        Args:
            checkbox_name (str): The checkboxes name
        """
        checkbox_dict: dict = self.__get_dict_act(checkbox_name, "checkbox")
        self.__double_left_mouse_click_act(checkbox_dict)

    def get_checkbox_label(self, checkbox_name: str) -> str:
        """Get a checkboxes text string

        Args:
            checkbox_name (str): The checkboxes name

        Returns:
            str: The checkboxes text string
        """
        checkbox_dict: dict = self.__get_dict_act(checkbox_name, "checkbox")
        checkbox_label: str = self.__get_element_label_act(checkbox_dict)
        return checkbox_label

    def toggle_checkbox(self, checkbox_name: str) -> None:
        """Toggles a checkbox on/off

        Args:
            checkbox_name (str): The checkboxes name
        """
        checkbox_dict: dict = self.__get_dict_act(checkbox_name, "checkbox")
        self.__toggle_element_state_act(checkbox_dict)

    def get_checkbox_toggle_state(self, checkbox_name: str) -> int:
        """Gets a checkboxes toggle state

        Args:
            checkbox_name (str): The checkboxes name

        Returns:
            int: 1 on/ 0 off
        """
        checkbox_dict: dict = self.__get_dict_act(checkbox_name, "checkbox")
        toggle_state: int = self.__get_toggle_state_act(checkbox_dict)
        return toggle_state
    def left_mouse_click_checkbox_coord(self, checkbox_name: str) -> None:
        """Left mouse click at x/y coordinate

        Args:
            checkbox_name (str): The checkbox name
        """
        elem_dict: dict = self.__get_dict_act(checkbox_name, "checkbox")
        self.__left_mouse_click_coordinates_act(elem_dict)

    def double_left_mouse_click_checkbox_coord(self, checkbox_name: str) -> None:
        """Double left mouse click at x/y coordinate

        Args:
            checkbox_name (str): The checkbox name
        """
        elem_dict: dict = self.__get_dict_act(checkbox_name, "checkbox")
        self.__double_left_mouse_click_coordinates_act(elem_dict)



    # methods that support clicking the mouse in order to select a radio button
    # **************************************************************
    # ****************** Mouse actions: Radio button ***************
    # **************************************************************

    def capture_checkbox_as_image(self, checkbox_name: str, test_id: str, image_name: str, baseline: bool) -> None:
        """Captures a checkbox element as an image

        Args:
            test_id: The testcase id
            image_name: The image name
            baseline: True/False
            checkbox_name (str): The checkboxes name
        """
        checkbox_dict: dict = self.__get_dict_act(checkbox_name, "checkbox")
        self.__capture_element_as_image_act(checkbox_dict, test_id, image_name, baseline)

    def left_mouse_click_radio_btn(self, radio_button_name: str) -> None:
        """Left mouse click a radio button

        Args:
            radio_button_name (str): The radio button's name
        """
        radio_button_dict: dict = self.__get_dict_act(radio_button_name, "radio_button")
        self.__left_mouse_click_act(radio_button_dict)

    def right_mouse_click_radio_btn(self, radio_button_name: str) -> None:
        """Right mouse click a radio button

        Args:
            radio_button_name (str): The radio button's name
        """
        radio_button_dict: dict = self.__get_dict_act(radio_button_name, "radio_button")
        self.__right_mouse_click_act(radio_button_dict)

    def double_left_mouse_click_radio_btn(self, radio_button_name: str) -> None:
        """Double left mouser click a radio button

        Args:
            radio_button_name (str): The radio button's name
        """
        radio_button_dict: dict = self.__get_dict_act(radio_button_name, "radio_button")
        self.__double_left_mouse_click_act(radio_button_dict)



    # **************************************************************
    # *************** Mouse actions: Coordinates *******************
    # **************************************************************

    #TODO: make coord method for each btn, checkbox, radio btn

    def get_radio_button_label(self, radio_button_name: str) -> str:
        """Get a radio button's text string

        Args:
            radio_button_name (str): The radio button's name

        Returns:
            str: The radio button's text string
        """
        radio_button_dict: dict = self.__get_dict_act(radio_button_name, "radio_button")
        radio_button_label: str = self.__get_element_label_act(radio_button_dict)
        return radio_button_label

    def capture_radio_button_as_image(self, radio_button_name: str, test_id: str, image_name: str, baseline: bool) -> None:
        """Captures a radio button element as an image

        Args:
            test_id: The testcase id
            image_name: The image name
            baseline: True/False
            radio_button_name (str): The radio button's name
        """
        radio_button_dict: dict = self.__get_dict_act(radio_button_name, "radio_button")
        self.__capture_element_as_image_act(radio_button_dict, test_id, image_name, baseline)

    def left_mouse_click_radio_btn_coord(self, radio_button_name: str) -> None:
        """Left mouse click at x/y coordinate

        Args:
            radio_button_name (str): The radio button's name
        """
        elem_dict: dict = self.__get_dict_act(radio_button_name, "radio_button")
        self.__left_mouse_click_coordinates_act(elem_dict)

    def double_left_mouse_click_radio_btn_coord(self, radio_button_name: str) -> None:
        """Double left mouse click at x/y coordinate

        Args:
            radio_button_name (str): The radio button's name
        """
        elem_dict: dict = self.__get_dict_act(radio_button_name, "radio_button")
        self.__double_left_mouse_click_coordinates_act(elem_dict)


    def __get_dict_act(self, element_name: str, button_type: str) -> dict | None:
        """Gets the element's object

        Args:
            element_name (str): The element's name
            button_type (str): The button type
        
        Returns:
            dict | None: obj dict
        """
        elem_repo: dict | None = None

        match button_type:
            case "button":
                elem_repo = self._buttons
            case "checkbox":
                elem_repo = self._checkboxes
            case "radio_button":
                elem_repo = self._radio_buttons
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
            print(f"This window does not contain this type of control: {type}")
