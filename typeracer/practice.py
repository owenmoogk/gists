import numpy as np
import cv2
from PIL import ImageGrab, Image
import pytesseract
import time
from pynput.keyboard import Key, Controller

filename = 'practice.png'

def main():

	# 150%
	img = ImageGrab.grab(bbox=(400,550,1700,700))

	img.save(filename)

	text = cv2.imread(filename)
	text = pytesseract.image_to_string(text)

	# parsing
	newText = ''
	for letterIndex in range(0, len(text) - 1):
		letter = text[letterIndex]

		# cases
		if letter == ',' or letter == '.':
			newText += ' '
			continue
		if letter == '_':
			letter = " "

		newText += letter

	# keypresses
	keyboard = Controller()
	# for i in range(5):
	for letterIndex in range(0, len(newText)):
		letter = newText[letterIndex]
		if letter == '\n':
			keyboard.press(Key.enter)
			keyboard.release(Key.enter)
		else:
			keyboard.press(letter)
			keyboard.release(letter)

	print(newText)

while True:
	main()
	time.sleep(1)