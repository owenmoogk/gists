import keyboard
import time

# string value to be repeated
text = 'dank memer'
timeDelay = 1

while True:
    if keyboard.is_pressed('f8'):  # if key 'q' is pressed 
        while True:
            for i in text:
                keyboard.press_and_release(i)
            keyboard.press_and_release('enter')
            if keyboard.is_pressed('f9'):
                break
            time.sleep(timeDelay)