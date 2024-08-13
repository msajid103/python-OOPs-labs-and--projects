import time
# import pyautogui
time.sleep(4)
# i = 0
# #
# while i != 200:
# # #
# #     pyautogui.typewrite(".")
#     pyautogui.typewrite("dill tu he bata")
# #     pyautogui.typewrite("dill tu he bata")
# #     pyautogui.typewrite("dill tu he bata")
# #
#     pyautogui.press("enter")
# #     pyautogui.press("enter")
#     i += 1
from pynput.keyboard import Key,Controller
keyb = Controller()
i = 0
while i != 10:

    # keyb.press('j')
    # keyb.release('j')
    keyb.press('l')
    keyb.release('l')
    keyb.press(Key.down)
    keyb.release(Key.down)
    time.sleep(2)
    i+=1
# keyb.release('Window')tT