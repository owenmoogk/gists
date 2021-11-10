import pyautogui
import keyboard

while True:
	pyautogui.click(600,600)
	if keyboard.is_pressed('q'):
		break