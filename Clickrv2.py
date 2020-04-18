import pyautogui
import keyboard as key  

startl = input ("Клавиша активации левой кнопки:")
startr = input ("Клавиша активации правой кнопки:")
stop = input ("Клавиша остановки:")



while True:
 if key.is_pressed( startl ):
  pyautogui.click(clicks=10000,interval=0.01)
 if key.is_pressed( stop ):
  break 

 if key.is_pressed( startr ):
  pyautogui.tripleClick(button = "right")
 if key.is_pressed( stop ):
  break