import pyautogui
import time

pyautogui.FAILSAFE = True  # Move mouse to a screen corner to stop the script

icon_path = './icons/follow.png'
scroll_amount = -300
wait_between_attempts = 1.5
max_click = 1000
print("Bot started. Press Ctrl+C to stop.")

clicked_count = 0
while True:
    if clicked_count > max_click: break
    print("[Searching for the follow icon...]")

    try:
        location = pyautogui.locateCenterOnScreen(icon_path, confidence=0.9)
    except pyautogui.ImageNotFoundException:
        location = None

    if location:
        print(f"✅ Icon found at {location}, clicking...")
        pyautogui.moveTo(location, duration=0.2)
        pyautogui.click()
        clicked_count+=1
        time.sleep(1)  # Wait after clicking (optional: avoid double-click)
    else:
        print("🔍 Icon not found, scrolling down...")
        pyautogui.scroll(scroll_amount)
        time.sleep(wait_between_attempts)
