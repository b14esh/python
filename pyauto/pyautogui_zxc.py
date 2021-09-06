# Pyautogui - модуль для работы с gui, нажимает клавиши
#typewrite() - это симуляция нажатия клавиш. Библиотека знает только клавиши на английском языке
#К примеру , чтобы напечатать "Привет" нужно передать "Ghbdtn"
#https://medium.com/nuances-of-programming/%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D1%81-python-a4c9f210a064
# https://pyautogui.readthedocs.io/en/latest/mouse.html
# https://pyautogui.readthedocs.io/en/latest/keyboard.html


# пример печатания текста
import pyautogui, time
time.sleep(5)
f = open(f"zxc.txt", 'r' , encoding="utf-8")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")





