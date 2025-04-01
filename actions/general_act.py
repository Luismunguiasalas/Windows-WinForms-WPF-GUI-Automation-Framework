from os import path, makedirs
from PIL import Image
from pyautogui import click, position, scroll, moveTo, moveRel, PAUSE
from math import radians, cos, sin


class GeneralActions:
    def __init__(self) -> None:
        self._self = None
        pass

    #     #TODO: Need to get rid of these: these belong somewhere else. don't know yet.
    #     self._self = None

    #     self._buttons: dict = dict()
    #     self._checkboxes: dict = dict()
    #     self._radio_buttons: dict = dict()

    #     self._labels: dict = dict()
    #     self._textboxes: dict = dict()
    #     self._coordinates: dict = dict()

    #     self._tables: dict = dict()
    #     self._lists: dict = dict()
    #     self._menus: dict = dict()

    #     self._controlNames: list = list()
    #     #TODO: END
    # # Public methods

    # # private methods

    # #TODO: Need to get rid of this method, belongs somewhere else. don't know yet.
    # def __get_object_act(self, name: str, type: str) -> object:
    #     """Gets the element's object

    #     Args:
    #         name (str): The element's name
    #         type (str): The button type

    #     Returns:
    #         object: button object
    #     """
    #     elem_repo: dict = None

    #     match type:
    #         case "button":
    #             elem_repo = self._buttons
    #         case "checkbox":
    #             elem_repo = self._checkboxes
    #         case "radio_button":
    #             elem_repo = self._radio_buttons
    #         case "label":                 
    #             elem_repo = self._labels
    #         case "textbox":               #TODO: add textbox selection methods
    #             elem_repo = self._textboxes
    #         case "coordinate":            #TODO: add coordinate selection methods
    #             elem_repo = self._coordinates
    #         case "table":                 #TODO: add table selection methods
    #             elem_repo = self._tables
    #         case "list":                  #TODO: add list selection methods
    #             elem_repo = self._lists
    #         case "menu":                  #TODO: add menu selection methods
    #             elem_repo = self._menus
    #         case _:
    #             pass

    #     if elem_repo is not None:
    #         elem_dict: dict = elem_repo.get(name, False)

    #         if elem_dict:
    #             return elem_dict
    #         else:
    #             print(f"{name} is not a valid input!")
    #             #TODO: update the print statement
    #             print("Use the .PrintControlIdentifiers(controlType) to get a windows control names for a window's labels, buttons, textboxes, menus, elements, etc.")
    #             print()
    #     else:
    #         print(f"This window does not contain this type of control: {type}")
    # #TODO: END

    # **************************************************************
    # ****************** Mouse actions *****************************
    # **************************************************************
    def __left_mouse_click_act(self, dictionary: dict) -> None:
        """Left mouse click action

        Args:
            dictionary (dict): The dictionary that contains the element's object
        """
        self.__set_element_focus_act(dictionary)
        elem_obj: object = dictionary["object"]
        elem_obj.click_input()
        self.__print_clicked_element_coordinates_act(dictionary)

    def __double_left_mouse_click_act(self, dictionary: dict) -> None:
        """Double left mouse click action

        Args:
            dictionary (dict): The dictionary that contains the element's object
        """
        self.__set_element_focus_act(dictionary)
        elem_obj: object = dictionary["object"]
        elem_obj.click_input()
        elem_obj.click_input()

    def __right_mouse_click_act(self, dictionary: dict) -> None:
        """Right mouse click action

        Args:
            dictionary (dict): The dictionary that contains the element's object
        """
        self.__set_element_focus_act(dictionary)
        elem_obj: object = dictionary["object"]
        elem_obj.right_click_input()

    # **************************************************************
    # ****************** X/Y Coordinate actions ********************
    # **************************************************************        
    def __left_mouse_click_coordinates_act(self, dictionary: dict) -> None:
        """Left mouse click at coordinates

        Args:
            dictionary (dict): The dictionary that contains the element's coordinates
        """
        relative_x, relative_y = self.__calculate_relative_coordinates_act(dictionary)
        click(relative_x, relative_y)

    def __double_left_mouse_click_coordinates_act(self, dictionary: dict) -> None:
        """Double left mouse click at coordinates

        Args:
            dictionary (dict): The dictionary that contains the element's coordinates
        """
        relative_x, relative_y = self.__calculate_relative_coordinates_act(dictionary)
        click(relative_x, relative_y)
        click(relative_x, relative_y)

    # # def __left_mouse_click_coordinates_act(self, elem_name: str, child_elem_obj: object = None) -> None:
    # def __left_mouse_click_coordinates_act(self, target_obj_dict: dict, child_elem_obj_dict: dict = None) -> None:
    #     parent_elem_obj: object = self._self                                        # < -------------- May need to get rid of this HERE TODO
    #     target_elem_obj: object = target_obj_dict["object"]
    #     # target_elem_obj = self.__get_object_act(elem_name)

    #     # if child_elem_obj is not None:
    #     if child_elem_obj_dict is not None:
    #         child_elem_obj: object = child_elem_obj_dict["object"]
    #         x_coord, y_coord = self.__calculate_element_coordinates_act(target_elem_obj, parent_elem_obj, child_elem_obj)
    #         # x_coord, y_coord = self.__calculate_element_coordinates_act(target_elem_obj, parent_elem_obj, child_elem_obj_dict)
    #         parent_elem_obj.click_input(coordinates=(x_coord, y_coord))
    #     else:
    #         x_coord, y_coord = self.__calculate_element_coordinates_act(target_elem_obj)
    #         parent_elem_obj.click_input(coordinates=(x_coord, y_coord))

    # def __double_left_mouse_click_coordinates_act(self, target_obj_dict: dict, child_elem_obj_dict: dict = None) -> None:
    # # def __double_left_mouse_click_coordinates_act(self, elem_name: str, child_elem_obj: object = None) -> None:
    #     parent_elem_obj: object = self._self                                    # < -------------- May need to get rid of this HERE TODO
    #     target_elem_obj: object = target_obj_dict["object"]
    #     # target_elem_obj = self.__get_object_act(elem_name)

    #     if child_elem_obj_dict is not None:
    #     # if child_elem_obj is not None:
    #         child_elem_obj: object = child_elem_obj_dict["object"]
    #         x_coord, y_coord = self.__calculate_element_coordinates_act(target_elem_obj, parent_elem_obj, child_elem_obj)
    #         parent_elem_obj.click_input(coordinates=(x_coord, y_coord))
    #         parent_elem_obj.click_input(coordinates=(x_coord, y_coord))
    #     else:
    #         x_coord, y_coord = self.__calculate_element_coordinates_act(target_elem_obj)
    #         parent_elem_obj.click_input(coordinates=(x_coord, y_coord))
    #         parent_elem_obj.click_input(coordinates=(x_coord, y_coord))

    # def __calculate_element_coordinates_act(self, target_elem_obj: object, parent_elem_obj: object = None, child_elem_obj: object = None) -> int:
    #     """Mouse click 

    #     Args:
    #         parent_elem_obj (object): Parent object
    #         child_elem_obj (object): Child object
    #         target_elem_obj (object): Target object

    #     Returns:
    #         int: X/Y coordinates
    #     """
    #     # get coordinates
    #     target_coordinates: dict = self.__get_element_coordinates_act(target_elem_obj)

    #     # calculate the center of the target element
    #     center_x_coord: int = (target_coordinates["left"] + target_coordinates["right"]) // 2
    #     center_y_coord: int = (target_coordinates["top"] + target_coordinates["bottom"]) // 2

    #     # if targeting an element that is within a child floating window.
    #     if (parent_elem_obj is not None) and (child_elem_obj is not None):
    #         # get coordinates
    #         parent_coordinates: dict = self.__get_element_coordinates_act(parent_elem_obj)
    #         child_coordinates: dict = self.__get_element_coordinates_act(child_elem_obj)

    #         # calculate the offset
    #         offset_x_coord: int = child_coordinates["left"] - parent_coordinates["left"]
    #         offset_y_coord: int = child_coordinates["right"] - parent_coordinates["right"]

    #         # calculate the abs coordinates for the click
    #         abs_x_coord: int = parent_coordinates["left"] + offset_x_coord + (center_x_coord - child_coordinates["left"])
    #         abs_y_coord: int = parent_coordinates["top"] + offset_y_coord + (center_y_coord - child_coordinates["top"])

    #         return abs_x_coord, abs_y_coord
    #     else:
    #         return center_x_coord, center_y_coord

    def __calculate_relative_coordinates_act(self, dictionary: dict) -> tuple[int, int]:
        """Calculates the relative coordinates for a target element

        Args:
            dictionary (dict): The dictionary containing the element's object

        Returns:
            int: X/Y coordinates
        """
        window_coordinates: dict = self.__get_element_coordinates_act(self._self)

        relative_x: int = dictionary["relative_x"]
        relative_y: int = dictionary["relative_y"]

        relative_x += window_coordinates["left"]
        relative_y += window_coordinates["top"]

        return relative_x, relative_y

    @staticmethod
    def __get_element_coordinates_act(elem_obj: object) -> dict:
        """Gets an element's coordinates. It has attributes - top, left, right, bottom and width(), height() methods.

        Args:
            elem_obj (object): The element's object

        Returns:
            dict: RECT structure.
        """
        rectangle: object = elem_obj.rectangle()
        return {
            "left": rectangle.left,
            "right": rectangle.right,
            "bottom": rectangle.bottom,
            "top": rectangle.top,
            "width": rectangle.width(),
            "height": rectangle.height()
        }

    # **************************************************************
    # ********************* Keyboard actions ***********************
    # **************************************************************
    @staticmethod
    def __delete_string_act(dictionary: dict) -> None:
        """Deletes a text string

        Args:
            dictionary (dict): The dictionary containing the element's object
        """
        elem_obj: object = dictionary["object"]
        elem_obj.type_keys("{VK_CONTROL down}" "a" "{DELETE}" "{VK_CONTROL up}")

    @staticmethod
    def __type_string_act(dictionary: dict, string_input: str) -> None:
        """Types the string input

        Args:
            dictionary (dict): The dictionary containing the element's object
            string_input (str): The string to type
        """
        elem_obj: object = dictionary["object"]
        elem_obj.type_keys(string_input)

    @staticmethod
    def __move_selection_up_act(dictionary: dict, selection_index: int) -> None:
        """Moves the selection up, a specified amount of times

        Args:
            dictionary (dict): The dictionary containing the element's object
            selection_index (str): Amount of times to move selection upwards
        """
        elem_obj: object = dictionary["object"]
        elem_obj.type_keys("{UP " + str(selection_index) + "}")

    @staticmethod
    def __move_selection_down_act(dictionary: dict, selection_index: int) -> None:
        """Moves the selection down, a specified amount of times

        Args:
            dictionary (dict): The dictionary containing the element's object
            selection_index (int): Amount of times to move selection downwards
        """
        elem_obj: object = dictionary["object"]
        if selection_index == 0:
            elem_obj.type_keys("{ENTER}")
        else:
            elem_obj.type_keys("{DOWN " + str(selection_index) + "}{ENTER}")

    # **************************************************************
    # ***************** Set Element Focus actions ******************
    # **************************************************************
    @staticmethod
    def __set_element_focus_act(dictionary: dict) -> None:
        """Set focus on an element

        Args:
            dictionary (dict): The dictionary containing the element's object
        """
        elem_obj: object = dictionary["object"]
        elem_obj.set_focus()

    # **************************************************************
    # ***************** Get Label/String actions *******************
    # **************************************************************
    @staticmethod
    def __get_element_label_act(dictionary: dict) -> str:
        """Get an element's text string

        Args:
            dictionary (dict): The dictionary containing the element's object
            
        Returns:
            str: The element's text string
        """
        elem_obj: object = dictionary["object"]
        return elem_obj.window_text()

    # **************************************************************
    # ****************** Element State actions *********************
    # **************************************************************
    @staticmethod
    def __toggle_element_state_act(dictionary: dict) -> None:
        """Toggles an element on/off

        Args:
            dictionary (dict): The dictionary containing the element's object
        """
        elem_obj: object = dictionary["object"]
        elem_obj.toggle()

    @staticmethod
    def __get_toggle_state_act(dictionary: dict) -> int:
        """Gets an element's toggle state

        Args:
            dictionary (dict): The dictionary containing the element's object

        Returns:
            int: 1 enabled | 0 disabled
        """
        elem_obj: object = dictionary["object"]
        toggle_state: int = elem_obj.get_toggle_state()
        return toggle_state

    # **************************************************************
    # **************** Element Navigation actions ******************
    # **************************************************************
    def __element_navigation_act(self, dictionary: dict, selections: list[str]) -> None:
        btn_compatible: bool = dictionary["btn_compatible"]
        reset_compatible: bool = dictionary["reset_compatible"]
        current_dict: dict = dictionary

        for selection in selections:
            btn_dict: dict = current_dict["buttons"]
            selected_dict: dict | None = btn_dict.get(selection, None)

            if "buttons" in selected_dict:
                current_dict: dict = selected_dict

            if selected_dict is not None:
                if btn_compatible:
                    self.__left_mouse_click_act(selected_dict)
                else:
                    selection_index: int = selected_dict["selection_index"]
                    if reset_compatible:
                        self.__reset_element_navigation_act(dictionary)
                    else:
                        self.__element_navigation_selection_act(dictionary, selection_index)
            else:
                print(f"{selection} is not a valid input")

    def __reset_element_navigation_act(self, dictionary: dict) -> None:
        """Resets element navigation to top

        Args:
            dictionary (dict): The dictionary containing the element's object
        """
        reset_index: int = dictionary["reset_index"]
        self.__move_selection_up_act(dictionary, reset_index)

    def __element_navigation_selection_act(self, dictionary: dict, selection_index: int) -> None:
        """Navigates down and selects an element

        Args:
            dictionary (dict): The dictionary containing the element's object
            selection_index (int): The element to select at the specified index
        """
        self.__move_selection_down_act(dictionary, selection_index)

    # **************************************************************
    # ************ Capture Image/Regression actions  ***************
    # **************************************************************
    def __capture_element_as_image_act(self, dictionary: dict, test_id: str, image_name: str, baseline: bool) -> None:
        """Captures an element as an image and saves it to the 'Desktop/AutomationResources/Images/[test_id] directory.

        Args:
            dictionary (dict): The dictionary that contains the element's object
            test_id (str): The test case's id
            image_name (str): The image's name
            baseline (bool): True - Capture baseline state | False - Capture current state

        Returns:
            _type_: _description_
        """
        if baseline:
            self.__create_image_directory_act(test_id)
            img_path: str = self.__get_image_directory_act()
            baseline_img_path: str = self.__update_image_directory_act(img_path, test_id, image_name, True)

            elem_obj: object = dictionary["object"]
            elem_img: object = elem_obj.capture_as_image()
            elem_img.save(baseline_img_path)
        else:
            img_path: str = self.__get_image_directory_act()
            baseline_img_path: str = self.__update_image_directory_act(img_path, test_id, image_name, True)

            if self.__directory_exists_act(baseline_img_path):
                current_img_path: str = self.__update_image_directory_act(img_path, test_id, image_name, False)

                elem_obj: object = dictionary["object"]
                elem_img: object = elem_obj.capture_as_image()
                elem_img.save(current_img_path)
            else:
                print("Error: Baseline image directory does not exist")

    def __visual_regression_act(self, test_id: str, image_name: str) -> bool:  #TODO:  should this be in test helpers??
        """Performs a visual regression test on the captured images (baseline/current)

        Args:
            test_id (str): The test case id
            image_name (str): The image's name

        Returns:
            bool: True - No visual changes/ False - visual changes
        """

        img_path: str = self.__get_image_directory_act()

        baseline_img_path: str = self.__update_image_directory_act(img_path, test_id, image_name, True)
        current_img_path: str = self.__update_image_directory_act(img_path, test_id, image_name, False)

        baseline_img: object = Image.open(baseline_img_path)
        current_img: object = Image.open(current_img_path)
        visual_change: bool = self.__compare_image_bytes_act(baseline_img, current_img)
        return visual_change

    def __get_images_directory_act(self, test_id: str, image_name: str) -> tuple[str, str]:  #TODO:  should this be in test helpers??
        """Performs a visual regression test on the captured images (baseline/current)

        Args:
            test_id (str): The test case id
            image_name (str): The image's name

        Returns:
            tuple: True - baseline and current image paths
        """

        img_path: str = self.__get_image_directory_act()

        baseline_img_path: str = self.__update_image_directory_act(img_path, test_id, image_name, True)
        current_img_path: str = self.__update_image_directory_act(img_path, test_id, image_name, False)

        return baseline_img_path, current_img_path

    # **** 1
    @staticmethod
    def __create_image_directory_act(directory_name: str) -> None:
        """
        Will create the 'Desktop/AutomationResources' directory if it doesn't exist
        Will create the 'Desktop/AutomationResources/Images' directory if it doesn't exist
        Will create the 'Desktop/AutomationResources/Images/[directory_name]' directory if it doesn't exist
        
        Args:
            directory_name (str): The directory name (testcase id) to store the images within
        """
        desktop_path: str = path.join(path.expanduser("~"), "Desktop")
        directory_path: str = path.join(desktop_path, "AutomationResources")

        if not path.exists(directory_path):
            makedirs(directory_path)
        directory_path: str = path.join(directory_path, "Images")

        if not path.exists(directory_path):
            makedirs(directory_path)
        directory_path: str = path.join(directory_path, directory_name)

        if not path.exists(directory_path):
            makedirs(directory_path)

    # **** 2
    @staticmethod
    def __get_image_directory_act() -> str:
        """Returns the "[user]/Desktop/AutomationResources/Images" directory

        Returns:
            str: Images directory path
        """
        image_directory: str = path.join(path.expanduser("~"), r"Desktop\AutomationResources\Images")
        return image_directory

    # **** 3
    @staticmethod
    def __update_image_directory_act(image_path: str, test_id: str, image_name: str, baseline: bool = False) -> str:
        """Creates an image path by concatenating the input parameters and adds a unique id

        Args:
            image_path (str): The path to the directory in where the image is stored
            test_id (str): The test case id
            image_name (str): The image's name
            baseline (bool, optional): Image is the baseline/current image. Defaults to False.

        Returns:
            str: The image's path
        """
        if baseline:
            image_path: str = image_path + "\\" + test_id + "\\" + "baseline-" + image_name + ".jpg"
        else:
            image_path: str = image_path + "\\" + test_id + "\\" + "current-" + image_name + ".jpg"
        return image_path

    # **** 4
    @staticmethod
    def __directory_exists_act(directory_path: str) -> bool:
        """Verifies if a directory path exists

        Args:
            directory_path (str): The directory path to verify

        Returns:
            bool: True - directory path exists | False - directory path does not exist
        """
        if not path.exists(directory_path):
            return False
        else:
            return True

    # **** 5
    @staticmethod
    def __compare_image_bytes_act(image1: object, image2: object) -> bool:
        """Compares pixel data of two images in order to verify that they are the same

        Args:
            image1 (object): First image
            image2 (object): Second images

        Returns:
            bool: True - they are the same | False - they are not the same
        """

        # resize images to the same dimensions, if necessary
        image1: object = image1.resize(image2.size)

        # compare the pixel data
        if image1.tobytes() == image2.tobytes():
            return True
        else:
            return False

    # **************************************************************
    # ********************* Print actions  *************************
    # **************************************************************

    def __print_clicked_element_coordinates_act(self, dictionary: dict):
        """Prints the X/Y coordinates of the mouse relative to the window that is in focus

        Args:
            dictionary (dict): The dictionary containing the element's object
        """
        window_coordinates: dict = self.__get_element_coordinates_act(self._self)
        elem_name: str = dictionary["name"]

        x, y = position()

        position_str = f"{elem_name} - Static Position - X: {x:4d} Y: {y:4d}"

        print(position_str)

        x_relative = x - window_coordinates["left"]
        y_relative = y - window_coordinates["top"]

        relative_position_str = f"{elem_name} - Relative Position - X: {x_relative:4d} Y: {y_relative:4d}"

        print(relative_position_str, end="\n---\n")
        print()

    # **************************************************************
    # ******************** Scroll actions  *************************
    # **************************************************************
    @staticmethod
    def __mouse_wheel_scroll_act(amount: int) -> None:
        scroll(amount)

    # **************************************************************
    # ******************** Trace/Draw actions  **************************
    # **************************************************************
    @staticmethod
    def __trace_circle_act(center_x: int, center_y: int, radius: int = 50, speed: float = 0.001):
        """Trace a circle

        Args:
            center_x (int): X coordinate
            center_y (int): Y coordinate
            radius (int, optional): Radius of circle. Defaults to 50.
            speed (float, optional): Trace speed. Defaults to 0.001.
        """
        # PAUSE = speed  # Adjust this value to control speed

        for angle in range(0, 360, 5):  # Increment by 5 degrees for smoother circle
            radian: float = radians(angle)
            x: float = center_x + radius * cos(radian)
            y: float = center_y + radius * sin(radian)
            # moveTo(x, y)
            moveTo(x, y, duration=speed)

    @staticmethod
    def __trace_square_act(center_x: int, center_y: int, radius: int = 50, speed: float = 0.5):
        """Trace a square

        Args:
            center_x (int): X coordinate
            center_y (int): Y coordinate
            radius (int, optional): Radius of square. Defaults to 50.
            speed (float, optional): Trace speed. Defaults to 0.001.
        """
        side_length: float = radius * 2
        top_left_x: float = center_x - radius
        top_left_y: float = center_y - radius

        # Move to the starting position
        moveTo(top_left_x, top_left_y)

        # Trace the square
        for _ in range(4):
            moveRel(side_length, 0, duration=speed)
            moveRel(0, side_length, duration=speed)
            moveRel(-side_length, 0, duration=speed)
            moveRel(0, -side_length, duration=speed)
