from python_imagesearch.imagesearch import imagesearch
from PIL import Image
import pyautogui
import time

#ERROR 401 Cant Find image


COLLECTBUTTON_PNG_PATH = "Png Files/Collect Button.png"
PAWBUTTON_PNG_PATH = "Png Files/Paw Button.png"
FULLSAMPLE_PNG_PATH = "Png Files/Full_"

PASSWORD = ["Bb1249ArTiS","Ma118BGy293","Pn178ORTA817","KAPtar0701RAT","Xx768Bgy223","PtR128LKA991","L178Mm2XYB","Wx179Oo0jMXeUY64k"]

def searchAndAddBrowsersPositions(countBrowsers):
    browsersPositions = []
    for sec in range(1,6):
        print(sec)
        time.sleep(1)

    start = pyautogui.position()
    pyautogui.click()

    time.sleep(1)

    startX,startY = start

    if isHorizontalOrientationWindows:
        offsetX = 50
        for i in range(countBrowsers):
            nextPos = (startX+(offsetX*i),startY)
            browsersPositions.append(nextPos)
    else:
        offsetY = 50
        for i in range(countBrowsers):
            nextPos = (startX,startY+(offsetY*i))
            browsersPositions.append(nextPos)
        
    return browsersPositions        

def getXYpositionFromTuple(position):
    return position[0],position[1]

def findImageCenter(startImagePosition,imagePath):
    im = Image.open(imagePath)
    (width, height) = im.size
    startImagePositionX,startImagePositionY = getXYpositionFromTuple(startImagePosition)
    centerX = startImagePositionX + width//2
    centerY = startImagePositionY + height//2
    return centerX,centerY

def findButtonImageAndPress(imagePath):
    imagePosition = imagesearch(imagePath)
    imagePositionX,imagePositionY = getXYpositionFromTuple(imagePosition)
    if imagePositionX == -1 or imagePositionY == -1:
        print("Cannot find",imagePath)
        return 401
    time.sleep(0.5)
    centerButtonPosition = findImageCenter(imagePosition,imagePath)
    pyautogui.moveTo(centerButtonPosition)
    time.sleep(1)
    pyautogui.click()

def resetMousePosition():
    pyautogui.click(200,200)

def pressButtonAndWait(positionToClick,sleep = 0):
    result = findButtonImageAndPress(positionToClick)
    if result == 401:
        return 401
    time.sleep(sleep)

def moveMouseAndClickToHive(hivePosition):
    pyautogui.moveTo(hivePosition)
    time.sleep(1)
    pyautogui.click(clicks=2, interval=0.5)
    time.sleep(1)

def collectHoneyFromHive(hivePosition,currentIndexFarm):
    moveMouseAndClickToHive(hivePosition)
    
    result = pressButtonAndWait(PAWBUTTON_PNG_PATH,sleep = 2.5)
    countTry = 0
    while result == 401:
        result = pressButtonAndWait(PAWBUTTON_PNG_PATH,sleep = 2.5)
        countTry+=1
        if countTry >= 5:
            return 401
        
    result = pressButtonAndWait(COLLECTBUTTON_PNG_PATH,sleep = 2.5)
    countTry = 0
    while result == 401:  
        result = pressButtonAndWait(COLLECTBUTTON_PNG_PATH,sleep = 2.5)
        countTry+=1
        if countTry >= 5:
            return 401
        
    # 8 second collecting
    time.sleep(8)

def generateFullPngPath(count):
    return FULLSAMPLE_PNG_PATH+str(count)+".png"

def checkOnExceedCount(count):
    return count+1 if count < 4 else 1

def checkOnExceedCountFarm(count):
    return count+1 if count < maxCountFarm-1 else 0
    
def getPositionOfFullTitle(countFullTitle):
    FULL_PNG_PATH = generateFullPngPath(countFullTitle)
    position = imagesearch(FULL_PNG_PATH)
    print("Try to find FULL title",FULL_PNG_PATH,position)
    return position


def switchTab():
    global currentIndexFarm
    #pyautogui.hotkey("ctrl","tab")
    currentIndexFarm = checkOnExceedCountFarm(currentIndexFarm)
    browserPosition = browsersPositions[currentIndexFarm]
    pyautogui.click(browserPosition)
    time.sleep(1)
    resetMousePosition()
    

def findFullTitleOnFarm(tryCount):
    countFullTitle = 1
    
    check = True
    for countTryToFindFullTitle in range(tryCount):
        fullTitlePosition = getPositionOfFullTitle(countFullTitle)
        fullTitlePositionX,fullTitlePositionY = getXYpositionFromTuple(fullTitlePosition)
        countFullTitle = checkOnExceedCount(countFullTitle)
        if fullTitlePositionX <= 0 or fullTitlePositionY <= 0:
            continue
        else:
            centerFullTitle = (fullTitlePositionX+20,fullTitlePositionY+200)
            result = collectHoneyFromHive(centerFullTitle,currentIndexFarm)
            check = False
            break
    if check:
        switchTab()
    return

def run():
    while gameLoaded:
        findFullTitleOnFarm(20)

isHorizontalOrientationWindows = False
accountCount = len(PASSWORD)
browsersPositions = searchAndAddBrowsersPositions(accountCount)
maxCountFarm = accountCount
currentIndexFarm = 0
gameLoaded = True

run()

