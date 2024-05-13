from tkinter import *
from tkinter.ttk import *

from util.serverlist_ import *

import tkinter as tk
import ctypes
import tkinter.messagebox as mb
import os
import tkinter.filedialog as fd
import time
import subprocess
import sys
import psutil
import win32process

# hwnd = ctypes.windll.kernel32.GetConsoleWindow()      
# if hwnd != 0:      
#     ctypes.windll.user32.ShowWindow(hwnd, 0)      
#     ctypes.windll.kernel32.CloseHandle(hwnd)
#     _, pid = win32process.GetWindowThreadProcessId(hwnd)
#     os.system('taskkill /PID ' + str(pid) + ' /f')

procs = [p for p in psutil.process_iter() if 'python.exe' in p.name() and __file__ in p.cmdline()]
if len(procs) > 1:
    print('blockhost: [WARNING] BlockHost is already running...')
    ctypes.windll.user32.MessageBoxW(0, "BlockHost is already running !", "BlockHost", 0x30)
    sys.exit(1)
else:
	print("blockhost: Process created")

checkServerList()

def main():
	ui = Tk()
	ui.title("BlockHost")
	ui.geometry("800x500")
	ui.resizable(False, False)
	ui.iconbitmap("src/logo.ico")


	ui.config(bg="#333333")
	ui.mainloop()

if __name__ == '__main__':
	main()