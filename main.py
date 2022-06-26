from python_imagesearch.imagesearch import imagesearch
import pyautogui
import pyperclip
import time
from PIL import Image
from datetime import datetime
from threading import Timer

#ERROR 401 Cant Find image


HOME_PNG_PATH = "Png Files/home1.png"
COLLECTBUTTON_PNG_PATH = "Png Files/Collect Button.png"
PAWBUTTON_PNG_PATH = "Png Files/Paw Button.png"
EXITBUTTON_PNG_PATH = "Png Files/Exit Button.png"
PLAYBUTTON_PNG_PATH = "Png Files/Play Button.png"
APPROVEBUTTON_PNG_PATH = "Png Files/Approve Button.png"
INPUTFIELD_PNG_PATH = "Png Files/Input Field.png"
FULLSAMPLE_PNG_PATH = "Png Files/Full_"

PASSWORD = "Bb1249ArTiS"

hexagonOffsetX = 200
hexagonOffsetY = 150

def findHomeOnScreen():
    homePosition = imagesearch(HOME_PNG_PATH)
    x,y = homePosition
    if x== -1 or y == -1:
        print("image not found")
        return 0,0
    homeCenterPosition = findImageCenter(homePosition,HOME_PNG_PATH)
    homeCenterPositionX = homeCenterPosition[0]
    homeCenterPositionY = homeCenterPosition[1]
    print("home position : ", homeCenterPositionX, homeCenterPositionY)
    moveMouse(homeCenterPosition)
    return homeCenterPosition
    
# sleep 1 sec after move
def moveMouse(positionToMove):
    pyautogui.moveTo(positionToMove)
    time.sleep(1)

def checkAllHives(countHivesInRow):
    currentHiveIndex = 0
    hivePositions = []
    homeCenterPositionX,homeCenterPositionY = getXYpositionFromTuple(homeCenterPosition)
    for y in range(len(countHivesInRow)):
        for x in range(countHivesInRow[y]):
            hivePositionX = homeCenterPositionX+hexagonOffsetX*(x+1)-y*(hexagonOffsetX/2)
            hivePositionY = homeCenterPositionY+hexagonOffsetY*(y)
            hivePosition = (hivePositionX,hivePositionY)
            currentHiveIndex +=1 
            print(currentHiveIndex,"hive position : ",hivePosition)
            moveMouse(hivePosition)
            hivePositions.append(hivePosition)
    return hivePositions

def getXYpositionFromTuple(position):
    return position[0],position[1]

def findImageCenter(startImagePosition,imagePath):
    im = Image.open(imagePath)
    (width, height) = im.size
    time.sleep(0.5)
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

def reloadSite():
    alertText = 'Сделайте главным окно браузера(игры)'
    alertTitle = 'Предупреждение'
    alertButtonText = 'OK'
    reloadSiteHotKey = "F5"
    
    pyautogui.alert(text = alertText, title = alertTitle, button = alertButtonText)
    time.sleep(5)
    pyautogui.press(reloadSiteHotKey)
    time.sleep(10)
    result = findButtonImageAndPress(PLAYBUTTON_PNG_PATH)
    while result == 401:
        result = findButtonImageAndPress(PLAYBUTTON_PNG_PATH)
    time.sleep(5)

def exitWindow():
    findButtonImageAndPress(EXITBUTTON_PNG_PATH)
    resetMousePosition()

def insertPasswordToField():
    pyperclip.copy(PASSWORD)
    pyautogui.hotkey("ctrl","v")
    
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

def collectHoneyFromHive(hivePosition,isFirstLoadGame):
    
    moveMouseAndClickToHive(hivePosition)
    
    result = pressButtonAndWait(PAWBUTTON_PNG_PATH,sleep = 5)
    if result == 401:
        return 401
    
    result = pressButtonAndWait(COLLECTBUTTON_PNG_PATH,sleep = 2.5)
    while result == 401:  
        result = pressButtonAndWait(COLLECTBUTTON_PNG_PATH,sleep = 2.5)
    time.sleep(10)
    result = findButtonImageAndPress(INPUTFIELD_PNG_PATH)
    if result == 401:
        exitWindow()
        return 401
    insertPasswordToField()
    findButtonImageAndPress(APPROVEBUTTON_PNG_PATH)
        
    # 10 second collecting
    time.sleep(10)

def generateFullPngPath(count):
    return FULLSAMPLE_PNG_PATH+str(count)+".png"

def checkOnExceedCount(count):
    return count+1 if count < 3 else 1
    
def getPositionOfFullTitle(countFullTitle):
    FULL_PNG_PATH = generateFullPngPath(countFullTitle)
    print("Try to find FULL title",FULL_PNG_PATH)
    position = imagesearch(FULL_PNG_PATH)
    return position


def shedule(func, nth_sec):
    wait = 7200
    Timer(wait, func).start()
    Timer(wait + 1, lambda: shedule(func, nth_sec)).start()

def run():
    isFirstLoadGame = True
    shedule(reloadSite, 10)
    while gameLoaded:
        countFullTitle = 1
        fullTitlePosition = getPositionOfFullTitle(countFullTitle)
        fullTitlePositionX,fullTitlePositionY = getXYpositionFromTuple(fullTitlePosition)
        
        while fullTitlePositionX == -1 or fullTitlePositionY == -1:
            fullTitlePosition = getPositionOfFullTitle(countFullTitle)
            fullTitlePositionX,fullTitlePositionY = getXYpositionFromTuple(fullTitlePosition)
            countFullTitle = checkOnExceedCount(countFullTitle)
            
        centerFullTitle = (fullTitlePositionX+40,fullTitlePositionY+100)
        result = collectHoneyFromHive(centerFullTitle,isFirstLoadGame)
        if result != 401:
            isFirstLoadGame = False

'''
homeCenterPosition = findHomeOnScreen()
countHivesInRow = [2,2,1]
hivesPositions = checkAllHives(countHivesInRow)

run()
'''


gameLoaded = True
run()
