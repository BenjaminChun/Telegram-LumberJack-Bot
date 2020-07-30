from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

pyautogui.FAILSAFE=True

#tree color along y axis RGB (161,116,56)
#sky color above head RGB (211,247,255)
#Coordinates above head left 1362,523
#coordinates above head right 1509 523
#left button coord 1340,875
#right button coord 1540,889
timesleep=0.5

if __name__=="__main__":
	def click(x,y):
		win32api.SetCursorPos((x,y))
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
		time.sleep(0.01)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

	while keyboard.is_pressed("q")==False:
		pic=pyautogui.screenshot()
		if pic.getpixel((1509,523))[2]!=56 and pic.getpixel((1518,399))[2]!=56:
			click(1340,875)
			time.sleep(0.2)
			click(1340,875)
			print("command 4 executed")
			time.sleep(timesleep)
		elif pic.getpixel((1509,523))[2]==56:
			click(1340,875)
			print("command 1 executed")
			time.sleep(timesleep)
		elif pic.getpixel((1493,587))[2]==56:
			click(1340,875)
			print("command 3 executed")
			time.sleep(timesleep)

		else:	
			click(1540,889)
			print("command 2 executed")
			time.sleep(timesleep)
