from python_imagesearch.imagesearch import imagesearch
import pyautogui

pos = imagesearch("home1.png")
pyautogui.moveTo(pos)
pyautogui.drag(-720, -115, 0.3,button='left')


