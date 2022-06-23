from python_imagesearch.imagesearch import imagesearch
import pyautogui
pos = imagesearch("Png Files/Full_1.png")
i = 1
while pos[0] == -1:
    pos = imagesearch("Png Files/Full_"+str(i)+".png")
    if i == 3:
        i = 0
    i+=1
print("position : ", pos[0], pos[1])
pyautogui.moveTo(pos)


