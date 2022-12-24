import pyautogui as pg
import time

time.sleep(10)

txt = open("D:/Shivam/Python/animals.txt")
a = "Ashish is"
for i in txt:
    pg.write(a+i)
    pg.press("Enter") 