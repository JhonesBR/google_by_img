'''##########################################################################################################'''
'''System Variables'''

MAX_WORDS = 14
PYTESSERACT_PATH = r'C:\Program Files\Tesseract-OCR\tesseract'

'''
    If you want to change the language of recognition change it at
    line 108 
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
    print("Top-left:", "X="+str(startCord[0])+", Y="+str(startCord[1]))


# Function to get the second coordinates (Botton Right) and execute 
def getEndZone():
    global startCord
    global endCord
    endCord = pyautogui.position()
    print("Botton-right:", "X="+str(endCord[0])+", Y="+str(endCord[1]))
    

# Verify Possibility, Take Screenshot and Execute
def VPTSaE():
    global startCord
    global endCord
    global MAX_WORDS
    global OPERATION
    global pressed_vks

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

        # Cut the text based on MAX_WORDS defined on top of the program
        text = getXWords(text, MAX_WORDS)

        if OPERATION == 1:
            # Search at google for results
            url = "https://www.google.com.tr/search?q={}".format(text)
            webbrowser.open(url)   
            # Shows confirmation message
            print('Searching for "'+ text +'"\n')
        if OPERATION == 2:
            # Just print the result
            print(text)

        # Redefine coordinates to empty
        startCord, endCord = (), ()
    else:
        # "Error" message
        print("Coordinates non defined")
    
    # Remove pressed keys to fix buffer issue
    toRemove = []
    for vk in pressed_vks:
        toRemove.append(vk)
    for vk in toRemove:
        pressed_vks.remove(vk)


# Function to cut text based on MAX_WORD
def getXWords(text, MAX_WORDS):
    s = text.split()
    if len(s) <= MAX_WORDS:
        return " ".join(s)
    else:
        return " ".join(s[:MAX_WORDS])


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
    if vk in pressed_vks:
        pressed_vks.remove(vk)


# Shows message and start the listener for keys
print("Program in operation\n")
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()