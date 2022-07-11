from datetime import datetime
from threading import Timer
from python_imagesearch.imagesearch import imagesearch

def on_10th_second():
    print('yo-ho-ho', datetime.now())
FULLSAMPLE_PNG_PATH = "Png Files/Full_"

def shedule(func, nth_sec):
    wait = 7200
    Timer(wait, func).start()
    Timer(wait + 1, lambda: shedule(func, nth_sec)).start()

def generateFullPngPath(count):
    return FULLSAMPLE_PNG_PATH+str(count)+".png"

def getPositionOfFullTitle(countFullTitle):
    FULL_PNG_PATH = generateFullPngPath(countFullTitle)
    print("Try to find FULL title",FULL_PNG_PATH)
    position = imagesearch(FULL_PNG_PATH)
    return position

#shedule(on_10th_second, 10)

print('ok')
while True:
    print(getPositionOfFullTitle(3))

#center house:
#440 400


# start position house : 358 328


# offset x +82
# offset y +72
