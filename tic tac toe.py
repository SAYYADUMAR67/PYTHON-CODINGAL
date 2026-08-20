theboard = {'7': '','8': '', '9': '',
           '4': '','5': '', '6': '',
            '3': '','2': '', '1': '',
}
boardkeys = []
for key in theboard:
    boardkeys.append(key)
def printboard (board):
    print(board[7] + '|' + '|' board[8] + board[9])
    print('-+-+-')
    print(board[4] + '|' + '|' board[5] + board[6])
    print('-+-+-')
    print(board[3] + '|' + '|' board[2] + board[1])
def game():
    turn = 'x'
    count = 0
    for i in range (10):
        printboard(theboard)
        print ("its your turn,"+ turn + "move to which place?")
        move = input()
        if theboard [move] == ' ':
            theboard[move] = turn
            count +=1