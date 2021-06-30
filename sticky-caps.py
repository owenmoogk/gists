import keyboard
from pynput import keyboard as k
import pyautogui

hotkey = "alt + i"
active = False # if the sticky caps is active
held = False # if the hotkey is currently held
case = True # just alternates for caps and not
isCapsOn = False # even if this isnt actually accurate, it returns the caps state to the state it was before hitting the keybind

def activate():

	def onPress(key):
		global active, held, case, isCapsOn

		if keyboard.is_pressed(hotkey) and (not held):
			active = not active
			held = True

			# return the caps state to the og state
			if isCapsOn:
				pyautogui.press('capslock')
				isCapsOn = False
		else:
			held = False

			if (len(str(key)) == 3) and active:
				case = not case
				pyautogui.press('capslock')
				isCapsOn = not isCapsOn
		
		
	def onRelease(key):
		pass

	with k.Listener(on_press=onPress, on_release=onRelease) as listener:
		listener.join()

activate()