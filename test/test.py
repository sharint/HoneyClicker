import pyperclip
import pyautogui

def closest (num, arr):
    curr = arr[0]
    for val in arr:
        if abs (num - val) < abs (num - curr):
            curr = val
    return curr


array = [464,614,764]
number = 475
#print(closest(number, array))
#print(pyautogui.position())

def checkOnExceedCount(count):
    return count+1 if count < 3 else 0

print(checkOnExceedCount(0))


#center house:
#440 400


# start position house : 358 328


# offset x +82
# offset y +72
