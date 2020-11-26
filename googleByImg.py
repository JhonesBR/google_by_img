'''##########################################################################################################'''
'''System Variables'''

MAX_WORDS = 14
PYTESSERACT_PATH = r'C:\Program Files\Tesseract-OCR\tesseract'

'''
    If you want to change the language of recognition change it at
    line X 
    por for Portuguese Language
    eng for English Language
'''

OPERATION = 1
'''
    1 for scan and search at Google
    2 for scan and print
'''



'''##########################################################################################################'''


# Default python Library imports
import os
import webbrowser

# Pillow library
try:
    from PIL import Image, ImageOps
except ImportError:
    os.system('python -m pip install pillow')
    from PIL import Image, ImageOps

# Pyautogui library
try:
    import pyautogui
except ImportError:
    os.system('python -m pip install pyautogui')
    import pyautogui

# Numpy library
try:
    import numpy
except ImportError:
    os.system('python -m pip install numpy')
    import numpy

# Keyboard library
try:
    from pynput.keyboard import Key, KeyCode, Listener
except ImportError:
    os.system('python -m pip install pynput')
    from pynput.keyboard import Key, KeyCode, Listener

# Cv2 library
try:
    import cv2
except ImportError:
    os.system('python -m pip install opencv-python')

import pytesseract


pytesseract.pytesseract.tesseract_cmd = PYTESSERACT_PATH

startCord, endCord = (), ()


# Function to get the first coordinates (Top Left)
def getStartZone():
    global startCord
    global endCord
    startCord = pyautogui.position()


# Function to get the second coordinates (Botton Right) and execute 
def getEndZone():
    global startCord
    global endCord
    endCord = pyautogui.position()
    

# Verify Possibility, Take Screenshot and Execute
def VPTSaE():
    global startCord
    global endCord
    global MAX_WORDS
    global OPERATION

    start, end = startCord, endCord

    # Verify existency of both coordinates
    if start != () and end != ():
        # Get Screenshot of area
        width = end[0] - start[0]
        height = end[1] - start[1]
        img = pyautogui.screenshot(region=(start[0], start[1], width, height))
        
        # Improve the image for better readability
        img = improveImage(img)

        # Analyze text of image using tesseract
        text = pytesseract.image_to_string(img, lang="por")

        # Get stop index using the MAX_WORDS defined on top of the program
        stopIndex = getStopIndex(text)

        # Cut text where the stop index point
        if stopIndex != 0:
            text = text[:stopIndex]

        if OPERATION == 1:
            # Search at google for results
            url = "https://www.google.com.tr/search?q={}".format(text)
            webbrowser.open(url)    
        if OPERATION == 0:
            # Just print the result
            print(text)

        # Redefine coordinates to empty
        startCord, endCord = (), ()


# Function to get the stop index based on MAX_WORD
def getStopIndex(text):
    spaces, empty = [], 1
    for i in range(0, len(text)):
        if text[i] == ' ':
            spaces.append(i)
        else:
            empty = 0

    if empty == 0:
        if len(spaces) < MAX_WORDS:
            stopindex = spaces[-1]
        else:
            stopIndex = spaces[MAX_WORDS-1]

    else: return 0
    return stopIndex


# Function to improve the readability of the image for tesseract
def improveImage(img):
    grey = ImageOps.grayscale(img)
    return grey


# Shortcuts linked to specific functions
shortcutList = {
    frozenset([Key.shift, KeyCode(vk=65)]): getStartZone,  # shift + a (Get start coordinates)
    frozenset([Key.shift, KeyCode(vk=66)]): getEndZone,    # shift + b (Get end coordinates)
    frozenset([Key.shift, KeyCode(vk=67)]): VPTSaE,        # shift + c (Try to take screenshot and execute)
}

# List of keys pressed to be compared
pressed_vks = set()

# Get VK for the key pressed
def get_vk(key):
    return key.vk if hasattr(key, 'vk') else key.value.vk

# Check if the keys pressed match to the shortcuts defined
def checkShortcutPress(combination):
    return all([get_vk(key) in pressed_vks for key in combination])

# Executed on any key press
def on_press(key):
    vk = get_vk(key)
    pressed_vks.add(vk)
    for combination in shortcutList:
        if checkShortcutPress(combination):
            shortcutList[combination]()

# Executed on any key release
def on_release(key):
    vk = get_vk(key)
    pressed_vks.remove(vk)


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()