#Elean Rivas 19062
#Connect4 moveIA
#Clase que se encarga de realizar los movimientos en el tablero

class connect4Move:
    

    def __init__(self, move):
        self.move = move
        self.board = []

    def getMove(self):
        #
        return self.move
    
    #verifica si el movimiento es valido(No se sale del tablero)
    def validMove(self, board, move):
        if board[0][move] == 0:
            return True
        else:
            return False

    #elige el movimiento a realizar    
    def makeMove(self, board, move, player):
        return board[0][move] == player
    

    #optimiza el movimiento a realizar
    def minMax(self, board, move, player):

        #debe incluir look-ahead
        #debe incluir heuristica
        #debe incluir alpha-beta pruning
        return 0
    
