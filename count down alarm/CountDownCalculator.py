# Go To Better Alarm File , This one is old and not updated and has many bugs
# Link to Better Alarm File(https://github.com/ofcoursenp/Python-projects-Completed/blob/main/count%20down%20alarm/BetterAlarm.py)
import time
import pyautogui as pg
from playsound import playsound

# Do pip3 install pyautogui and pip3 install playsound in the terminal or windows powershell
# before running this file or else it wont work
# Count Down Alarm , It has iphone ringtone 

print("DO u want to enter time in seconds or minute")
Whatdouwant = input("Enter here > ")

if Whatdouwant.lower() == "seconds":
    acctuallsecond = pg.prompt("Enter the time u want to start the count down in seconds : ")
    acctuallsecond = int(acctuallsecond)
    for i in range(1,acctuallsecond+1):
        print(i)
        time.sleep(1)
        i -=1
    playsound("iphon.mp3")
        
if Whatdouwant.lower() == "minute" or Whatdouwant.lower() == "minutes":
    print("Seprate the minutes by :")
    print("Example : 8:10 > Here : is the diffrence of 8 minutes and 10 seconds")
    minutes = pg.prompt("Enter the time u want to start the count down in minutes : ")
    minutes_split = minutes.split(":")
    min = int(minutes_split[0])
    secondsofmin = min*60
    second_index = minutes_split[1]
    acctuallsecond = int(secondsofmin) + int(second_index)
    for i in range(1,acctuallsecond+1):
        print(i)
        time.sleep(1)
        i -=1
    playsound("iphon.mp3")
