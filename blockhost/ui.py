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
import pyglet
import shutil

# Instance Checker
hwnd = ctypes.windll.kernel32.GetConsoleWindow()      
if hwnd != 0:      
    ctypes.windll.user32.ShowWindow(hwnd, 0)      
    ctypes.windll.kernel32.CloseHandle(hwnd)
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    os.system('taskkill /PID ' + str(pid) + ' /f')

procs = [p for p in psutil.process_iter() if 'python.exe' in p.name() and __file__ in p.cmdline()]
if len(procs) > 1:
	# If BlockHost is already running, the another instance will be closed
    print('blockhost: [WARNING] BlockHost is already running...')
    ctypes.windll.user32.MessageBoxW(0, "BlockHost is already running !", "BlockHost", 0x30)
    sys.exit(1)
else:
	print("blockhost: Process created")

# Adding Fonts
pyglet.font.add_file('src/fonts/Gotham-Bold.otf')

def main():
	ui = Tk()
	ui.title("BlockHost")
	ui.geometry("800x500")
	ui.resizable(False, False)
	ui.iconbitmap("src/logo.ico")

	ui.config(bg="#333333")
	
	if checkServerList():
		with open('util/server_list.txt') as file_in:
			for line in file_in:
				dir = os.listdir(line)
				if 'start.cmd' or 'start.bat' in dir:
					def startServer():
						print("blockhost: [WARNING] File copying in server folder...")
						shutil.copy2("template/basic_server.bat", line)
						print("blockhost: File copied in server folder")
						os.system(f'start cmd /K" cd {line} & basic_server.bat"')
						print("blockhost: New session created")
						print("blockhost: Server started")

					Label(ui, text=f"{line}", bg="#333333", font=("Gotham-Bold", 15), fg="white").pack()
					Button(ui, text="Start server", command=startServer).pack()

	ui.mainloop()

if __name__ == '__main__':
	main()