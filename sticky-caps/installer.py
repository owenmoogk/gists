import shutil
import tkinter as tk
import sys
import subprocess

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'keyboard'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'pynput'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'pyautogui'])

original = 'sticky-caps.py'
target = 'C:\\Users\\owenm\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\sticky-caps.pyw'

shutil.copyfile(original, target)

root = tk.Tk()
root.geometry('500x200')
root.title('Sticky Caps Installer')
frame = tk.Frame(root)
frame.pack()

text = tk.Text(frame, height=10, width=50)
text.pack()
text.insert(tk.END, 'Sticky caps is installed! Toggle with \"ALT + I\".')

root.mainloop()