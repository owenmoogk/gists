import keyboard
import time

stop = 0

toType = 'Pls sell skunk'
timeDelay = 1 #seconds
startButton = 'b'
stopButton = 's'

while True:  # making a loop
    if keyboard.is_pressed('b'):  # if key 'q' is pressed 
        while stop == 0:
            for i in toType:
                keyboard.press_and_release(i)
                keyboard.press_and_release('enter')
                if keyboard.is_pressed('s'):
                    stop = 1
            time.sleep(timeDelay)
    stop = 0