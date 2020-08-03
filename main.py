#Welcome to the Telegram Lumberjack GameBot
#Meant to be run on a 1980x1080 display with Lumberjack as a split screen on the right with 100% zoom settings
#Run the prog after hitting the play button


#Logic: click button twice after checking branch is above head
#How: pyautogui checks for the pixel parameters above head and if fits the branch, it will click the opposing button

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

pyautogui.FAILSAFE=True

#tree color along y axis RGB (161,116,56)
#sky color above head RGB (211,247,255)
#Coordinates above head left (1362,523)
#coordinates above head right (1509 523)
#left button coord (1340,875)
#right button coord (1540,889)

#branch1
left_man_x,left_man_y=1362,523
right_man_x,right_man_y=1509,523
#branch2
right_man_x2,right_man_y2=1518,399
left_man_x2,left_man_y2=1372,399
#buttons
rightclick_x,rightclick_y=1540,889
leftclick_x,leftclick_y=1340,875
#for troubleshooting
count=0

#variable to change for how fast the prog will run
timesleep=0.2

if __name__=="__main__":
	#win32 approach of clicking is faster than pyautogui
	def click(x,y):
		win32api.SetCursorPos((x,y))
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
		time.sleep(0.02)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

	while keyboard.is_pressed("q")==False:
		'''
		pseudo code:
			if branch above, press 2 times opp direction
			if 2 branches detected in same location, press x4
		'''

		pic=pyautogui.screenshot()
		#if branch1 on right present and branch2 on right present, click left button 4x (this increases the speed hence optimiser)
		if pic.getpixel((right_man_x,right_man_y))[2]==56 and pic.getpixel((right_man_x2,right_man_y2))[2]==56:
			click(leftclick_x,leftclick_y)
			count+=1
			click(leftclick_x,leftclick_y)
			count+=1
			click(leftclick_x,leftclick_y)
			count+=1
			click(leftclick_x,leftclick_y)
			count+=1
			print("optimiser right "+str(count))
			time.sleep(timesleep)
		#if branch1 on left and branch2 on left present, click right button 4x
		elif pic.getpixel((left_man_x,left_man_y))[2]==56 and pic.getpixel((left_man_x2,left_man_y2))[2]==56:
			click(rightclick_x,rightclick_y)
			count+=1
			click(rightclick_x,rightclick_y)
			count+=1
			click(rightclick_x,rightclick_y)
			count+=1
			click(rightclick_x,rightclick_y)
			count+=1
			print("optimiser left "+str(count))
			time.sleep(timesleep)

		#if branch1 on left present, click right button 2x
		elif pic.getpixel((left_man_x,left_man_y))[2]==56:
			click(rightclick_x,rightclick_y)
			count+=1
			click(rightclick_x,rightclick_y)
			count+=1
			print("moved left cuz branch ontop of rightman + count " + str(count))
			time.sleep(timesleep)

		#if branch1 on right present, click left button 2x
		elif pic.getpixel((right_man_x,right_man_y))[2]==56:
			click(leftclick_x,leftclick_y)
			count+=1
			click(leftclick_x,leftclick_y)
			count+=1
			print("left cuz left top is clear"+str(count))
			time.sleep(timesleep)
		#if branch1 on right absent, click right button 1x (typically to start the prog as there are no branches nearby at the start)
		elif pic.getpixel((right_man_x,right_man_y))[2]==255:
			click(rightclick_x,rightclick_y)
			count+=1
			print("last command")
			time.sleep(timesleep)