import keyboard
from pynput import keyboard as k
import pyautogui

hotkey = "alt + i"
active = False # if the sticky caps is active
held = False # if the hotkey is currently held
case = True # just alternates for caps and not

def activate():

	def onPress(key):
		global active, held, case
		
		if (len(str(key)) == 3) and active:
			case = not case
			pyautogui.press('capslock')

		if keyboard.is_pressed(hotkey) and (not held):
			active = not active
			held = True
		else:
			held = False
		
	def onRelease(key):
		pass

	with k.Listener(on_press=onPress, on_release=onRelease) as listener:
		listener.join()

activate()