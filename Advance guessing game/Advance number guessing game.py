import random as r

#-------------------------------------------------------------------------------------------------------------------------------
# all the necessary variables
user_tries = 0 # increments every time user inputs wrong number
is_working = True
is_guessing = True
#---------------------------------------------------------------------------------------------------------------------------------

#program runs from here:
print("Do you want to start this game?\n")
start = input("Enter Yes or No: ").lower()

if start == "yes" or start == "ok" or start == "sure":
    while is_working == True:
        print("Select appropriate upper limit")
        try:
            upper_limit = int(input("Enter upper limit here : "))
            if upper_limit > 0:
                is_working = False
        except ValueError:
            print("Please enter a correct value ")
    print("Select Level \n1: Easy level (shows if ur higher or lower the number)\n2: Hard level(Does not show u any hint)\nPress 1 for easy and 2 for hard")
    try:
        hard_or_easy = int(input("Enter ur difficulty , press 1 or 2 anything else will close the program : "))
    except ValueError:
        quit()
    computer_guess = r.randint(1,upper_limit)
    if hard_or_easy == 1 or hard_or_easy == 2:
        if hard_or_easy == 1:
            while is_guessing == True:
                try:
                    user_guess = int(input(f"Enter a number between 1 - {upper_limit} : "))
                except ValueError:
                    print("Please enter a correct value ")
                try:
                    if user_guess == computer_guess:
                        print("You Won")
                        print(f"It took u {user_guess} tries")
                        is_guessing = False
                    if user_guess > computer_guess:
                        user_tries +=1
                        print("Go a little bit low")
                    if user_guess < computer_guess:
                        user_tries +=1
                        print("Go a bit high")
                except:
                    print(" ")
        if hard_or_easy == 2:
            while is_guessing == True:
                try:
                    user_guess = int(input(f"Enter a number between 1 - {upper_limit} : "))
                except ValueError:
                    print("Please enter a correct value ")
                try:
                    if user_guess == computer_guess:
                        print("You Won")
                        print(f"It took u {user_guess} tries")
                        is_guessing = False
                    else:
                        user_tries +=1
                        print("Try again")
                except:
                    print(" ")
    else:
        quit()
else:
    print("Thank you for trying")
    quit()


