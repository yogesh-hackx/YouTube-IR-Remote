import serial
import pyautogui

arduinoSerialData = serial.Serial('/dev/ttyACM1', 9600)	#Replace ttyACM1 with your corresponding port

while(1 == 1):
	if(arduinoSerialData.inWaiting()>0):
		myData = arduinoSerialData.readline()
		plainstring1 = myData.decode("utf-8", "ignore")
		print(plainstring1)
		if("33456255" in plainstring1):
			print("Play/Pause")
			pyautogui.keyDown('space')
			pyautogui.keyUp('space')

		if("33439935" in plainstring1):
			print("SeekBack")
			pyautogui.hotkey('shift', 'left')

		if("33472575" in plainstring1):
			print("SeekForward")
			pyautogui.hotkey('shift', 'right')

		if("33446055" in plainstring1):
			print("FullScreen_Toggle")
			pyautogui.press('f')

		if("33460335" in plainstring1):
			print("Captions_Toggle")
			pyautogui.press('c')

		if("33454215" in plainstring1):
			print("Mute_Toggle")
			pyautogui.press('m')