theboard = {'7': '','8': '', '9': '',
            '4': '','5': '', '6': '',
            '3': '','2': '', '1': '',
}
boardkeys = []
for key in theboard:
    boardkeys.append(key)
def printBoard (board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[3] + '|' + board[2] + '|' + board[1])
def game():
    turn = 'x'
    count = 0
    for i in range (10):
        printBoard(theboard)
        print ("its your turn,"+ turn + "move to which place?")
        move = input()
        if theboard [move] == ' ':
            theboard[move] = turn
            count +=1
        else:
            print("that place is already filled.\nMove to which place?")
            continue

        if count >= 5:
            if theboard['7'] == theboard['8'] == theboard['9'] != ' ':
                printBoard(theboard)
                print("\nGAME OVER!.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theboard['4'] == theboard['5'] == theboard['6'] != ' ':
                printBoard(theboard)
                print("\nGAME OVER!.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theboard['3'] == theboard['2'] == theboard['1'] != ' ':
                printBoard(theboard)
                print("\nGAME OVER!.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theboard['1'] == theboard['4'] == theboard['7'] != ' ':
                printBoard(theboard)
                print("\nGAME OVER!.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theboard['2'] == theboard['5'] == theboard['8'] != ' ':
                printBoard(theboard)
                print("\nGAME OVER!.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theboard['3'] == theboard['6'] == theboard['9'] != ' ':
                printBoard(theboard)
                print("\nGAME OVER!.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theboard['7'] == theboard['5'] == theboard['3'] != ' ':
                printBoard(theboard)
                print("\nGAME OVER!.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theboard['1'] == theboard['5'] == theboard['9'] != ' ':
                printBoard(theboard)
                print("\nGAME OVER!.\n")
                print(" **** " +turn + " won. ****")
                break
            if count == 9:
                print("GAME OVER!")
                print("IT'S A TIE!")

            if turn == 'x':
                turn = 'O'
            else:
                turn = 'x' 

        restart = input ("DO YOU WANT TO PLAY AGAIN?!(Y/N)")
        if restart == "Y" or restart == "Y":
            for key in boardkeys:
                theboard[key] = " "

            game()

if __name__ == "__main__":
    game()