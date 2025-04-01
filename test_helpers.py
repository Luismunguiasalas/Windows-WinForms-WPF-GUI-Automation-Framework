"""Library contains pre-written methods that you may add to a test class."""
import re
import cv2
import pyautogui

import json
import base64
from pathlib import Path

import allure

# when entering the navigation window, unique identifier for window
def modify_date(date: str) -> str:
    """Replaces '/' with '-'

    Args:
        date (str): date

    Returns:
        str: date
    """
    date = date.replace("/", "-")
    return date

def modify_time(ttime: str) -> str:
    """Replaces ':' with '-'

    Args:
        ttime (str): time

    Returns:
        str: time
    """
    ttime = ttime.replace(":", "-")[:-3]
    return ttime

def concatenate_window_name(last_name: str, first_name: str, mi: str, date: str, ttime: str) -> str:
    window_name = "Sierra Summit - " + last_name + ", " + first_name + " " + mi + " " + date + " " + ttime
    return window_name

def split_directory_path(directory_path:str) -> str:
    return directory_path.split("\\")[-1]

# shared steps,
def shared_steps(step_dict: dict, repeat: int = 1) -> None:
    """Able to repeat test steps many times, this function takes a dictionary as input and iterates over the method calls.

    Args:
        step_dict (dict): The dictionary containing all the methods and their inputs
        repeat (int, optional): The number of times to repeat. Defaults to 1.
    """
    for _ in range(repeat):
        for arr in step_dict.values():
            obj = arr[0]
            num_of_args = len(arr)
            if num_of_args == 2:
                obj(arr[1])
            elif num_of_args == 3:
                obj(arr[1], arr[2])
            elif num_of_args == 4:
                obj(arr[1], arr[2], arr[3])
            elif num_of_args == 5:
                obj(arr[1], arr[2], arr[3], arr[4])

            # if len(arr) > 2:
            #     obj(arr[1], arr[2])
            # else:
            #     obj(arr[1])

# def test(obj, method_name, *args):
#     method = getattr(obj, method_name)
#     argsLen = len(args)

#     print(args)

#     if argsLen == 1:
#         method(args)
#     elif argsLen == 2:
#         arg1, arg2 = args
#         method(arg1, arg2)
#     elif argsLen == 3:
#         arg1, arg2, arg3 = args
#         method(arg1, arg2, arg3)

# def repeatSteps(arr: list[callable], input: list[list[str]], repeat: int = 1):
#     for i in range(repeat):
#         for j in range(len(arr)):
#             obj, inp = arr[j], input[j]
#             if len(inp) > 1:
#                 obj(inp[0], inp[1])
#             else:
#                 obj(inp[0])
#         print("cycle: ", i+1)


def extract_arguments(code_string):
    pattern = r"methodName\(([^()]*?)(\[[^\]]*\])([^()]*)?\)"
    match = re.search(pattern, code_string)

    if match:
        arguments = [match.group(1), match.group(2), match.group(3)]
        return arguments
    else:
        # Handle cases where no array is present
        pattern = r"methodName\(([^()]*)\)"
        match = re.search(pattern, code_string)
        if match:
            arguments = match.group(1).split(",")
            return arguments
        else:
            return []  # No match found


# code_string1 = "methodName('arg1Value')"
# code_string2 = "methodName('arg1Value', ['arg2Value', 'arg3Value'])"
# code_string3 = "methodName('arg1Value', ['arg2Value', 'arg3Value'], 'arg4Value')"

# print(extract_arguments(code_string1))  # Output: ['arg1Value']
# print(extract_arguments(code_string2))  # Output: ['arg1Value', '[arg2Value, arg3Value]', '']
# print(extract_arguments(code_string3))  # Output: ['arg1Value', '[arg2Value, arg3Value]', 'arg4Value']


def extract_method_and_arguments(code_string):
    pattern = r"(\w+)\(([^()]*?)(\[[^\]]*\])([^()]*)?\)"
    match = re.search(pattern, code_string)

    if match:
        method_name = match.group(1)
        arguments = []
        if match.group(2) != "":
            arguments.append(match.group(2))
        if match.group(3) != "":
            arguments.append(match.group(3))
        if match.group(4) != "":
            arguments.append(match.group(4))
        # arguments = [match.group(2), match.group(3)]
        return method_name, arguments
    else:
        # Handle cases where no array is present
        pattern = r"(\w+)\(([^()]*)\)"
        match = re.search(pattern, code_string)
        if match:
            method_name = match.group(1)
            arguments = match.group(2).split(",")
            return method_name, arguments
        else:
            return None, []  # No match found

# code_string1 = "methodName('arg1Value')"
# code_string2 = "methodName('arg1Value', ['arg2Value', 'arg3Value'])"
# code_string3 = "methodName('arg1Value', ['arg2Value', 'arg3Value'], 'arg4Value')"

# method_name, arguments = extract_method_and_arguments(code_string1)
# print(method_name, arguments)  # Output: methodName ['arg1Value']

# method_name, arguments = extract_method_and_arguments(code_string2)
# print(method_name, arguments)  # Output: methodName ['arg1Value', '[arg2Value, arg3Value]']

# method_name, arguments = extract_method_and_arguments(code_string3)
# print(method_name, arguments)  # Output: methodName ['arg1Value', '[arg2Value, arg3Value]', 'arg4Value']

# # Function to capture screen video
# def capture_screen_video(output_file, duration=10, fps=20):
#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4 format
#     screen_size = pyautogui.size()  # Get the size of the primary monitor
#     writer = cv2.VideoWriter(output_file, fourcc, fps, screen_size)

#     start_time = time.time()

#     while True:
#         screenshot = pyautogui.screenshot()
#         frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

#         # Get current mouse position
#         x, y = pyautogui.position()
#         cursor_radius = 5  # Cursor size
#         cv2.circle(frame, (x, y), cursor_radius, (0, 255, 0), -1)  # Draw cursor

#         writer.write(frame)  # Write the frame to the video file

#         if time.time() - start_time > duration:
#             break

#         time.sleep(1 / fps)

#     writer.release()
