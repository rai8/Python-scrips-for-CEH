#install the pyautoui library module
#install the following first
#sudo apt-get install python3-tk python3-dev
#sudo apt-get install scrot


import pyautogui

my_screenshot= pyautogui.screenshot()
my_screenshot.save(r'/home/hytonne/Pictures/screenshot2.png')