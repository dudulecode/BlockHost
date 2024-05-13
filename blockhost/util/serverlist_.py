from tkinter import *

import ctypes
import os

# Check Server List

def checkServerList():
    with open('util/server_list.txt') as file_in:
        for line in file_in:
            if os.path.getsize('util/server_list.txt') == 0:
                ctypes.windll.user32.MessageBoxW(0, "empty", "BlockHost", 0x30)
                print("blockhost: Server list is empty")
                return False
            else:
                return True