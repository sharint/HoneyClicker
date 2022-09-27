
import pyautogui
import time

#print(pyautogui.position())
pyautogui.moveTo(353, 425)
pyautogui.click()
time.sleep(0.5)
pyautogui.drag(-200, 0, 0.3,button='left')
