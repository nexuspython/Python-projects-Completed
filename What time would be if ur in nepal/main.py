import time
import Nepal

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
splittime = current_time.split(":")

timetoconvert = input('Enter time u want to convert to : ').lower()
if timetoconvert == "aus" or timetoconvert == "australia":
    identifier = "Time in Australia "
    nptouss = int(Nepal.ausInSec[0])

if timetoconvert == "uk" or timetoconvert == "united kingdom":
    identifier = "Time in UK "
    nptouss = int(Nepal.ukInSec[0])

if timetoconvert == "us" or timetoconvert == "united states":
    identifier = "Time in usa "
    nptouss = int(Nepal.usInSec[0])


hourtosec = int(splittime[0]) * 60 * 60
mintosec = int(splittime[1]) * 60
secofsec = int(splittime[2])
sec = secofsec + hourtosec + mintosec

if timetoconvert == "aus" or timetoconvert == "australia":
    timeOfUsToNp = sec + nptouss
else:
    timeOfUsToNp = sec - nptouss
minofustonp = 0
Hourfustonp = 0


while (timeOfUsToNp):
    if timeOfUsToNp > 60:
        timeOfUsToNp -= 60
        minofustonp += 1

    if minofustonp > 60:
        minofustonp -= 60
        Hourfustonp += 1

    if timeOfUsToNp < 60 and minofustonp < 60:
        break


print(f"{identifier} right now is : {Hourfustonp}:{minofustonp}:{timeOfUsToNp}")
