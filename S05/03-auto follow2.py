import pyautogui, time
pyautogui.FAILSAFE = True

while True:
    try:
        location = pyautogui.locateCenterOnScreen('./follow.png', confidence=0.9)
        pyautogui.moveTo(location, duration=0.2)
        pyautogui.click()
    except pyautogui.ImageNotFoundException:
        pyautogui.scroll(-300)
    time.sleep(1.5)