import serial
import pyautogui
import subprocess as s

arduinoSerialData = serial.Serial('/dev/ttyACM0', 9600)	#Replace ttyACM1 with your corresponding port

#Control Functions
def seekBack():
	pyautogui.hotkey('shift', 'left')

def seekForward():
	pyautogui.hotkey('shift', 'right')

def play():
	pyautogui.press('space')

def mute():
	pyautogui.press('m')

def captions():
	pyautogui.press('c')

def fullScreen():
	pyautogui.press('f')

def volumeDec():
	s.Popen(['amixer', 'set', 'Master', '10%-'])

def volumeInc():
	volOutput = s.check_output(['amixer', 'set', 'Master', '10%+'])
	volOutput = str(volOutput)
	if ("off" in volOutput):
		s.Popen(['amixer', '-D', 'pulse', 'set', 'Master', 'toggle'])
		volOutput = s.check_output(['amixer', 'set', 'Master', '40%+'])

#Judgement Area :P
while(True):
	if(arduinoSerialData.inWaiting()>0):
		myData = arduinoSerialData.readline()
		plainstring1 = myData.decode("utf-8", "ignore")
		#print(plainstring1)							Remove this Comment to see your IR codes
		if("33456255" in plainstring1):
			print("Play/Pause")
			play()

		if("33439935" in plainstring1):
			print("SeekBack")
			seekBack()

		if("33472575" in plainstring1):
			print("SeekForward")
			seekForward()

		if("33446055" in plainstring1):
			print("FullScreen_Toggle")
			fullScreen()

		if("33460335" in plainstring1):
			print("Captions_Toggle")
			captions()
		
		if("33454215" in plainstring1):
			print("Mute_Toggle")
			mute()

		if("33464415" in plainstring1):
			print("volume 10% --")
			volumeDec()

		if("33448095" in plainstring1):
			print("volume 10% ++")
			volumeInc()