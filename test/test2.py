import time
import pyautogui


for sec in range(1,6):
    print(sec)
    time.sleep(1)


start = pyautogui.position()
pyautogui.click()

time.sleep(1)

offsetX = 50

startX,startY = start
browsersPositions = []
for i in range(5):
    nextPos = (startX+(offsetX*i),startY)
    browsersPositions.append(nextPos)
    pyautogui.moveTo(nextPos)

