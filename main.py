import pyautogui, time, keyboard

pyautogui.PAUSE = 0.1
pyautogui.MINIMUM_DURATION = 0
pyautogui.FAILSAFE = False

time.sleep(2)

region = (300, 210, 1250, 676)

for i in range(31):
    loc = pyautogui.locateOnScreen("target.png", region=region, confidence=0.4)
    if loc:
        x, y = pyautogui.center(loc)
        pyautogui.click(x, y, duration=0)
    if keyboard.is_pressed('esc'):
        break