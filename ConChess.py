print('''
  ____             ____ _                   
 / ___|___  _ __  / ___| |__   ___  ___ ___ 
| |   / _ \\| '_ \\| |   | '_ \\ / _ \\/ __/ __|
| |__| (_) | | | | |___| | | |  __/\\__ \\__ \\
 \\____\\___/|_| |_|\\____|_| |_|\\___||___/___/

            Welcome to ConChess
''')


# NEED TO MAKE FUNCTION THAT MAKES THE WHOLE BOARD WITH WHITE AND BLACK SPACES, AND THE PIECES OF COURSE
# DO NOT MAKE MANUALLY
class chess(object):
    def __init__(self):
        board = [
            ['C','K','B','W','Q','B','K','C'],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '','' , '', ''],
            ['', '', '', '', '', '', '', ''],
            ['c','k','b','w','q','b','k','c']]
        for i in range(len(board)) :  
            for j in range(len(board[i])) :  
                print(board[i][j], end=" ")
            print()

if __name__ == "__main__":
    chess = chess()