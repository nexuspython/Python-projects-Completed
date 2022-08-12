import random

words = ["elephant" , "house" , "microsoft"]


wannaplay = int(input("do u wanna play press 1 to play \nif u dont wanna play press 0 : "))
print("If u wanna quit in middle of game enter quit to stop the game")

while True:
    comp_word_slect = random.choice(words)
    if comp_word_slect.lower() == "elephant":
        print("Is big \na animal of land\n enter here if u think u guessed it")
        is_correct = input("Enter the guessed word : ")
        if is_correct.lower() == "elephant":
            print("Nice u got it")
        if is_correct.lower() == "quit":
            quit()
        else:print("Sorry its wrong")
    if comp_word_slect.lower() == "house":
        print("gives shelter \nIts where u live\n enter here if u think u guessed it")
        is_correct = input("Enter the guessed word : ")
        if is_correct.lower() == "house":
            print("Nice u got it")
        if is_correct.lower() == "quit":
            quit()
        else:print("Sorry its wrong")
    if comp_word_slect.lower() == "microsoft":
        print("Is a company \nmade Windows operating system \n enter here if u think u guessed it")
        is_correct = input("Enter the guessed word : ")
        if is_correct.lower() == "microsoft":
            print("Nice u got it")
        if is_correct.lower() == "quit":
            quit()
        else:print("Sorry its wrong")
    if wannaplay == 0:
        quit()





