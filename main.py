from python_imagesearch.imagesearch import imagesearch
from PIL import Image
import pyautogui
import pyperclip
import time

#ERROR 401 Cant Find image


HOME_PNG_PATH = "Png Files/home1.png"
COLLECTBUTTON_PNG_PATH = "Png Files/Collect Button.png"
PAWBUTTON_PNG_PATH = "Png Files/Paw Button.png"
EXITBUTTON_PNG_PATH = "Png Files/Exit Button.png"
PLAYBUTTON_PNG_PATH = "Png Files/Farm.png"
APPROVEBUTTON_PNG_PATH = "Png Files/Approve Button.png"
INPUTFIELD_PNG_PATH = "Png Files/Password.png"
FULLSAMPLE_PNG_PATH = "Png Files/Full_"
ERROR_PNG_PATH = "Png Files/Error.png"
ERRORBUTTON_PNG_PATH = "Png Files/Error button.png"


PASSWORD = ["Bb1249ArTiS","Ma118BGy293","Pn178ORTA817","KAPtar0701RAT","Xx768Bgy223","PtR128LKA991","L178Mm2XYB","Wx179Oo0jMXeUY64k"]

dragForBestVisionOffsetX = 720
dragForBestVisionOffsetY = 100

hexagonOffsetX = 200
hexagonOffsetY = 150

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
    reloadSiteHotKey = "F5"
    time.sleep(1)
    pyautogui.press(reloadSiteHotKey)
    time.sleep(5)
    result = findButtonImageAndPress(PLAYBUTTON_PNG_PATH)
    while result == 401:
        result = findButtonImageAndPress(PLAYBUTTON_PNG_PATH)
    time.sleep(5)

def exitWindow():
    findButtonImageAndPress(EXITBUTTON_PNG_PATH)
    resetMousePosition()

def insertPasswordToField(currentIndexFarm):
    pyperclip.copy(PASSWORD[currentIndexFarm])
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
    
    time.sleep(3)
    result = findButtonImageAndPress(INPUTFIELD_PNG_PATH)
    if result == 401:
        exitWindow()
        return 401
    insertPasswordToField(currentIndexFarm)
    time.sleep(1)
    findButtonImageAndPress(APPROVEBUTTON_PNG_PATH)
        
    # 7 second collecting
    time.sleep(7)

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

def dragMouseForBestVisionHives():
    result = findButtonImageAndPress(HOME_PNG_PATH)
    while result == 401:
        result = findButtonImageAndPress(HOME_PNG_PATH)
    pyautogui.moveTo(result)
    pyautogui.drag(-dragForBestVisionOffsetX, -dragForBestVisionOffsetY, 0.3,button='left')

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
        reloadSite()
        if currentIndexFarm == 1 or currentIndexFarm == 2 or currentIndexFarm == 3:
            dragMouseForBestVisionHives()
    return

def run():
    while gameLoaded:
        serverConnectionError = findButtonImageAndPress(ERRORBUTTON_PNG_PATH)
        findFullTitleOnFarm(20)

isHorizontalOrientationWindows = False
accountCount = len(PASSWORD)
browsersPositions = searchAndAddBrowsersPositions(accountCount)
maxCountFarm = accountCount
currentIndexFarm = 0
gameLoaded = True

run()

