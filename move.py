#Elean Rivas 19062
#Connect4 moveIA
#Clase que se encarga de realizar los movimientos en el tablero

class connect4Move:
    

    def __init__(self, move):
        self.infinito = 100000000000
        self.move = move
        self.board = []
        self.depth = 5
    
    #verifica si el movimiento es valido(No se sale del tablero)
    def validMove(self, board, move):
        for row in range(5, -1, -1):
            if board[row][move] == 0:
                return True
        return False

    #elige el movimiento a realizar    
    def makeMove(self, board,):
        #retorna el movimiento a realizar
        #llama a make move
        #valida el movimiento
        return 0 #el retorno debe ser solamente un número entre 0-6
    

    #optimiza el movimiento a realizar 
    def minMax(self, board, move, player):

        #debe incluir look-ahead
        #debe incluir heuristica
        #debe incluir alpha-beta pruning
        return 0

    #Revisa la adyacencia de fichas   
    def getAdjacentTiles(self, board, row, col, player=None):
        adjacent_tiles = []
        
        if player is None:
            player = self.move
        
        # Vertical
        if row + 1 < 6 and board[row + 1][col] == player:
            adjacent_tiles.append((row + 1, col))
        
        # horizontal
        if col + 1 < 7 and board[row][col + 1] == player:
            adjacent_tiles.append((row, col + 1))
        
        # diagonal (top-left to bottom-right)
        if row + 1 < 6 and col + 1 < 7 and board[row + 1][col + 1] == player:
            adjacent_tiles.append((row + 1, col + 1))
        
        # diagonal (top-right to bottom-left)
        if row + 1 < 6 and col - 1 >= 0 and board[row + 1][col - 1] == player:
            adjacent_tiles.append((row + 1, col - 1))
        
        return adjacent_tiles
    
    #aplicamos la heuristica
    def evaluate(self, board):
        heuristic_value = 3
        defensive_value = 1.5
        strategic_value = [1, 3, 5, 7, 5, 3, 1]
        
        total_value = heuristic_value
        
        for row in range(6):
            for col in range(7):
                if board[row][col] == self.move:
                    # Fichas propias adyacentes
                    adjacencies = self.getAdjacentTiles(board, row, col)
                    total_value += 3 * len(adjacencies)
                    
                    # Fichas rivales para determinar el valor defensivo
                    opponent_adjacencies = self.getAdjacentTiles(board, row, col, self.getOpponentMove())
                    total_value += defensive_value * len(opponent_adjacencies)
                    
                    # Valor estrategico posicional
                    total_value += strategic_value[col]
        
        return total_value