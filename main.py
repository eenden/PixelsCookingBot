import pyperclip
import pyautogui
import random
from time import sleep

def cook():
	x = random.randint(1120, 1210)
	y = random.randint(750, 770)
	pyautogui.click(x, y)
	pause = random.randint(122, 127)
	# pause = random.randint(362, 365)
	sleep(pause)
	x = random.randint(1125, 1208)
	y = random.randint(753, 771)
	pyautogui.click(x, y)
	pause = random.randint(5, 15)
	sleep(pause)



def main():
	# print(pyautogui.position())
	# return
	for i in range(22):
		cook()


if __name__ == '__main__':
	sleep(10)
	main()