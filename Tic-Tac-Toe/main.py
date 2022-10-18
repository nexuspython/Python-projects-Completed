
board = [" "," "," ",
        " "," "," ",
        " "," "," ",]

def printboard(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print(f"---------")
    print("END BOARD")

filled = 0
turn = 0
win = False
printboard(board)
while not win:
    try:
        if filled == 9:
            print("Its a draw")
            break
        if turn == 0:
            choice = int(input("its 0 turn , Enter the number u want to keep the point : "))
        if turn == 1:
            choice = int(input("its X turn , Enter the number u want to keep the point : "))
    except ValueError:
        print("Please enter valid int ")
# Checking if the number is already repleated or not?
    try:
        if turn == 0: 
            if board[choice-1] == "X" or board[choice-1] == "0":
                print("That spot is alrady filled , chose another spot : ")
            else:
                board[choice-1] = "0"
                filled +=1
                turn = 1
                printboard(board)           
        elif turn == 1:
            if board[choice-1] == "X" or board[choice-1] == "0":
                print("That spot is alrady filled , chose another spot : ")
            else:
                board[choice-1] = "X"
                filled +=1
                turn = 0
                printboard(board)
    except ValueError:
        print("Please choose number between 1-9")
    except NameError:
        print("Please choose number between 1-9")
    except IndexError:
        print("Please choose number between 1-9")       
    
    # Checking if player wins or not
    if board[0] == "X" and board[1] == "X" and board[2] == "X":
        print("X wins")
        break
    elif board[0] == "0" and board[1] == "0" and board[2] == "0":
        print("0 wins")
        break
    elif board[3] == "X" and board[4] == "X" and board[5] == "X":
        print("X wins")
        break
    elif board[3] == "0" and board[4] == "0" and board[5] == "0":
        print("0 wins")
        break
    elif board[6] == "X" and board[7] == "X" and board[8] == "X":
        print("X wins")
        break
    elif board[6] == "0" and board[7] == "0" and board[8] == "0":
        print("0 wins")
        break
    elif board[0] == "0" and board[4] == "0" and board[8] == "0":
        print("0 wins")
        break
    elif board[0] == "X" and board[4] == "X" and board[8] == "X":
        print("X wins")
        break
    elif board[2] == "0" and board[4] == "0" and board[6] == "0":
        print("0 wins")
        break
    elif board[2] == "X" and board[4] == "X" and board[6] == "X":
        print("X wins")
        break
    elif board[0] == "0" and board[3] == "0" and board[6] == "0":
        print("0 wins")
        break
    elif board[0] == "X" and board[3] == "X" and board[6] == "X":
        print("X wins")
        break
    elif board[1] == "0" and board[4] == "0" and board[7] == "0":
        print("0 wins")
        break
    elif board[1] == "X" and board[4] == "X" and board[7] == "X":
        print("X wins")
        break
    elif board[2] == "0" and board[5] == "0" and board[8] == "0":
        print("0 wins")
        break
    elif board[2] == "X" and board[5] == "X" and board[8] == "X":
        print("X wins")
        break

    
 






