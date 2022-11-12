import pyautogui
import time
times = 100
while times>0:
    time.sleep(1)
    pyautogui.typewrite('I love Programmig. I love this one')
    time.sleep(1)
    pyautogui.press('Enter')
