import pyautogui
import time

def print_mouse_position():
    print("Press Ctrl-C to quit.")
    try:
        while True:
            x, y = pyautogui.position()
            position_str = f"X: {x:4d} Y: {y:4d}"
            print(position_str, end='\r')
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nDone.")

# Usage:
# print_mouse_position()


# import pyautogui
# import time

# print("Click anywhere on the screen. Press Ctrl-C to quit.")
# try:
#     while True:
#         if pyautogui.mouseDown():
#             x, y = pyautogui.position()
#             print(f"Mouse clicked at X: {x}, Y: {y}")
#         time.sleep(0.1)
# except KeyboardInterrupt:
#     print("\nDone.")



# def mouse_scroll():
#     print("Press Ctrl-C to quit.")
#     try:
#         while True:
#             amount = input()
#             pyautogui.scroll(int(amount))
#     except:
#         print("\nDone.")


# mouse_scroll()