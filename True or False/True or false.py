from ast import While
from decimal import DivisionByZero
from operator import truediv
from re import A


print("Please leave gap after every new int \nFor eg 22 + 22 = 44 \nDont leave space for same integers just leave gap for new process")
print("Use opeator as python operator \nopeartors = ['/' , '%'  , '**' , '+' , '-' , '*'] \nIf u want square answer do number ** number = answer \nIf u want to do Remainder do number % number = answer")



a = input("Enter ur Input : ")

# opeartors = ['/' , '%'  , "**" , "+" , "-" , "*"]

try:
    splitword = a.split(" ")
except IndexError:
    print("Please enter correct value")


logs = open("F:\python projects\True or False\Logs.txt" , "a") #in that F:\ (instead enter ur log file location and dont forget to add .txt at last)
logs.write(str(splitword))

# print(splitword)

# print(int(splitword[0]))
# print(int(splitword[2]))
# print(int(splitword[-1]))
try:
    if splitword[1] == "*": #Multiplication
        first = int(splitword[0])
        second = int(splitword[2])
        last = int(splitword[-1])
        if first * second == last:
            print("True")
            logs.write("Multiplication found , Answer was True\n")
        else:
            print("False")
            logs.write("Multiplication found , Answer was False\n")
except ValueError:
    logs.write("Sorry not a correct value\n")
    print("Please Enter a correct Airthmetic Operation , Also use gap after each instance of integer(number)")
except DivisionByZero:
    print("Cant divide by zero")
except IndexError:
    logs.write("Please enter correct value")
    print("Sorry pls enter correct value")

try:
    if splitword[1] == "+": #Addition
        first = int(splitword[0])
        second = int(splitword[2])
        last = int(splitword[-1])
        if first + second == last:
            print("True")
            logs.write("Addition found , Answer was True\n")
        else:
            print("False")
            logs.write("Additon found , Answer was False\n")
except ValueError:
    logs.write("Sorry not a correct value\n")
    print("Please Enter a correct Airthmetic Operation , Also use gap after each instance of integer(number)")
except DivisionByZero:
    print("Cant divide by zero")
except IndexError:
    logs.write("Please enter correct value")
    print("Sorry pls enter correct value")

try:
    if splitword[1] == "-": #Substraction
        first = int(splitword[0])
        second = int(splitword[2])
        last = int(splitword[-1])
        if first - second == last:
            print("True")
            logs.write("Substraction found , Answer was True\n")
        else:
            print("False")
            logs.write("Square found , Answer was False\n")
except ValueError:
    logs.write("Sorry not a correct value")
    print("Please Enter a correct Airthmetic Operation , Also use gap after each instance of integer(number)\n")
except DivisionByZero:
    print("Cant divide by zero")
except IndexError:
    logs.write("Please enter correct value")
    print("Sorry pls enter correct value")

try:
    if splitword[1] == "/": #Division
        first = int(splitword[0])
        second = int(splitword[2])
        last = int(splitword[-1])
        if first / second == last:
            logs.write("Divison found , Answer was True\n")
            print("True")
        else:
            print("False")
            logs.write("Divison found , Answer was False\n")
except ValueError:
    logs.write("Sorry not a correct value\n")
    print("Please Enter a correct Airthmetic Operation , Also use gap after each instance of integer(number)")
except ZeroDivisionError:
    logs.write("Sorry Cant divide by Zero")
    print("Cant divide by zero\n")
except IndexError:
    logs.write("Please enter correct value")
    print("Sorry pls enter correct value")

try:
    if splitword[1] == "%": #Remainder
        first = int(splitword[0])
        second = int(splitword[2])
        last = int(splitword[-1])
        if first % second == last:
            print("True")
            logs.write("Remainder found , Answer was True\n")
        else:
            print("False")
            logs.write("Remainder found , Answer was False\n")
except ValueError:
    logs.write("Sorry not a correct value\n")
    print("Please Enter a correct Airthmetic Operation , Also use gap after each instance of integer(number)")
except DivisionByZero:
    print("Cant divide by zero")
except IndexError:
    logs.write("Please enter correct value")
    print("Sorry pls enter correct value")

try:
    if splitword[1] == "**": #Square
        first = int(splitword[0])
        second = int(splitword[2])
        last = int(splitword[-1])
        if first ** second == last:
            logs.write("Square found , Answer was True\n")
            print("True")
        else:
            print("False")
            logs.write("Square found , Answer was False\n")
except ValueError:
    logs.write("Sorry not a correct valuen\n")
    print("Please Enter a correct Airthmetic Operation , Also use gap after each instance of integer(number)")
except DivisionByZero:
    print("Cant divide by zero")
except IndexError:
    logs.write("Please enter correct value")
    print("Sorry pls enter correct value")

logs.close()





