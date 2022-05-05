import numpy as np
import cv2
from PIL import ImageGrab, Image
import pytesseract
import time
from pynput.keyboard import Key, Controller

filename = 'race.png'

pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR/tesseract.exe"


time.sleep(2)

# distance from left, distance from top
# 150% zoom, scroll to bottom, 24inch monitor
img = ImageGrab.grab(bbox=(300,550,1550,900))

img.save(filename)

text = cv2.imread(filename)
text = pytesseract.image_to_string(text)

# parsing
newText = ''
lastLetter = ''
for letterIndex in range(0, len(text) - 1):
	letter = text[letterIndex]

	# cases
	if (letter == ',' or letter == '.') and (lastLetter == ',' or lastLetter == "."):
		# this ones weird, but it often mistaked underscores for two punctuations so i just got rid of them
		newText = newText[:-1]
		newText += ' '
		continue
	if letter == '_':
		letter = " "
	if letter == " " and lastLetter == " ":
		continue
	if letter == "\n":
		letter == " "
	if letter == '¢' or letter == "<":
		letter = "\n"

	lastLetter = letter
	newText += letter

# keypresses
keyboard = Controller()
for i in range(50):
	for letterIndex in range(0, len(newText)):
		letter = newText[letterIndex]
		if letter == '\n':
			keyboard.press(Key.enter)
			keyboard.release(Key.enter)
		else:
			keyboard.press(letter)
			keyboard.release(letter)

print(newText)