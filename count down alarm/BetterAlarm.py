from time import sleep
from playsound import playsound

time_in_min = list(input("Enter time in min and split with ':', : ").split(":"))
sec = int(time_in_min[1])
min = int(time_in_min[0])


while sec > 60:
  if sec >= 60:
    sec -=  60
    min +=1

  if sec < 60:
    break

secmin = min*60

time_in_sec = secmin+sec


while (time_in_sec):
    print(f"{min}:{sec}")
    time_in_sec -=1
    if sec == 0 and min > 0:
        sec +=60
        min -=1
    if sec > 0:
        sec -=1
    if sec == 0 and min == 0:
        break

    sleep(1)
    
playsound("iphon.mp3")

