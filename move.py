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
        valid_moves = [move for move in range(7) if self.validMove(board, move)]
    
        if not valid_moves:
            raise ValueError("No valid moves available.")
        
        for move in valid_moves:
            if self.validMove(board, move):
                best_move = move
            break
    
        best_move = self.minMax(board, self.depth, True, -self.infinito, self.infinito)[0]
        
        if best_move not in valid_moves:
            raise ValueError("The selected move is not valid.")
        
        return best_move
    

    #optimiza el movimiento a realizar 
    def minMax(self, board, depth, maximizingPlayer, alpha, beta):
        valid_moves = [move for move in range(7) if self.validMove(board, move)]
        #profundidad
        if depth == 0 or len(valid_moves) == 0:
            return None, self.evaluate(board)
        #maximizamos nuetros tiro
        if maximizingPlayer:
            max_eval = -self.infinito
            best_move = None
            
            for move in valid_moves:
                new_board = self.makeMoveInBoard(board, move, 1)
                evaluation = self.minMax(new_board, depth - 1, False, alpha, beta)[1]
                
                if evaluation > max_eval:
                    max_eval = evaluation
                    best_move = move
                #poda
                alpha = max(alpha, evaluation)
                if beta <= alpha:
                    break
            
            return best_move
        
        else:
            #minimizacion del tiro rival
            min_eval = self.infinito
            best_move = None
            
            for move in valid_moves:
                new_board = self.makeMoveInBoard(board, move, 2)
                evaluation = self.minMax(new_board, depth - 1, True, alpha, beta)[1]
                
                if evaluation < min_eval:
                    min_eval = evaluation
                    best_move = move
                #poda
                beta = min(beta, evaluation)
                if beta <= alpha:
                    break
            
            return best_move

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
    
    #se obtiene el valor del rival para poder obtener el valor defensivo y el min
    def getOpponentMove(self):
        return 1 if self.move == 2 else 2
    