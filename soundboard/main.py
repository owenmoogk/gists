import winsound
import ctypes  # For interacting with Windows libraries
import win32con  # For Windows constants


# Define the hotkey combination
MOD_KEY = win32con.MOD_CONTROL | win32con.MOD_ALT  # Control + Alt
HOT_KEY = win32con.VK_I  # 'I' key

# Define the MP3 file path (replace with your actual file path)
mp3_file = r"C:\path\to\your\music.mp3"  # Raw string for including backslashes

# Function to play the MP3 file
def play_music():
    winsound.PlaySound(mp3_file, winsound.SND_FILENAME)

# Function to get and set the system volume
def get_volume():
    return ctypes.windll.user32.GetSystemVolume(0)  # Get current volume

def set_volume(volume):
    ctypes.windll.user32.SetSystemVolume(0, volume)  # Set volume (0 for default device)

# Function to register the hotkey
def register_hotkey():
    user32 = ctypes.windll.user32
    wintypes = ctypes.wintypes

    # Structure for hotkey registration
    class HOTKEY_MODIFIERS(ctypes.Structure):
        _fields_ = [("vk", wintypes.WORD),
                    ("mod", wintypes.WORD)]

    # Register the hotkey
    hotkey = HOTKEY_MODIFIERS(vk=HOT_KEY, mod=MOD_KEY)
    user32.RegisterHotKey(None, 0, 0, ctypes.pointer(hotkey))

    # Define the callback function for the hotkey
    def hotkey_callback(param):
        # Mute the volume
        current_volume = get_volume()
        set_volume(65535)  # Maximum volume value

        # Play the music
        play_music()

        # Restore the volume
        set_volume(current_volume)

    # Set the callback function for the hotkey
    user32.SetWinEventHook(win32con.EVENT_SYSTEM_KEYDOWN, hotkey_callback, None, 0, 0)

# Run the functions on startup (assuming script is run at startup)
register_hotkey()
message = "Hotkey registered. Press Win+Alt+I to play music and mute/unmute volume."
print(message)

# Keep the script running to listen for the hotkey
while True:
    pass
