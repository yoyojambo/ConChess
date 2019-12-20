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
        self.board = [
            ['c','k','b','w','q','b','k','c'],
            ['p','p','p','p','p','p','p','p'],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '','' , '', ''],
            ['P','P','P','P','P','P','P','P'],
            ['C','K','B','W','Q','B','K','C']]
        self.turn = True
        
    def draw(self):
        for i in range(len(self.board)) :  
            for j in range(len(self.board[i])) :  
                print(self.board[i][j], end=" ")
                if self.board[i][j] == '':
                    print(' ', end='')
            print()

    def takeinput(self):
        if self.turn:
            self.move = input("White movement: ")
        else:
            self.move = input("Black movement: ")
        
        if self.move == "exit":
            quit()

        if ord(self.move[0]) > 104 or ord(self.move[0]) < 97:
            print("That is not admitted, try again")
            self.takeinput()
        if ord(self.move[3]) > 104 or ord(self.move[3]) < 97:
            print("That is not admitted, try again")
            self.takeinput()

        if (self.move[0].lower() in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']) and (self.move[3].lower() in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
            self.origin = [8 - int(self.move[1]) , ord(self.move[0].lower()) - 97]
            self.destiny = [8 - int(self.move[4]) , ord(self.move[3].lower()) - 97]

    def movepiece(self, o, d):
        if self.board[d[0]][d[1]].isupper != self.board[o[0]][o[1]].isupper:
            if self.pieceallowedmove(self.board[d[0]][d[1]], self.board[o[0]][o[1]]):
                self.board[d[0]][d[1]] = self.board[o[0]][o[1]]
                self.board[o[0]][o[1]] = ''
                self.turn = not self.turn
            else:
                print("That is not an allowed move for that piece.")
            
        else:
            print("You can't eat you own piece.")
            self.takeinput()
        

if __name__ == "__main__":
    chess = chess()
    while True:
        chess.draw()
        chess.takeinput()
        chess.movepiece(chess.origin, chess.destiny)
    
    