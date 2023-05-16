#Elean Rivas 19062
#Connect4 Client

import socketio
import random
import math


#Settings
host = 'localhost'
port = '4000'

HOST = host
PORT = port
userName = input("Ingrese su nombre de usuario:\n")
tournamentID = in´put("Ingrese el ID del torneo:\n")


#Cliente de Socket.io
sio = socketio.Cliente()
address = 'http://' + HOST + ":" + + PORT
sio.connect(address)


#Conexión
@sio.on('connect')
def connect():
    ## Client has connected
    print("Conectado: " + userName)

    ## Signin signal
    sio.emit('signin', {
        'user_name' : userName,
        'tournament_id' : tournamentID,
        'user_role' : 'player'
    })

@sio.on('ready')
def ready(data):
    gameID = data['game_id']
    playerTurnID = data['player_turn_id']
    board = data['board']
    c4_move = random.randint(1, 4)
    tournamentID = data['tournament_id']

    print("ID del juego: " + gameID)
    print("ID del jugador: " + playerTurnID)
    print("Movimiento: " + str(c4_move))
    print("Tablero: " + board)

    sio.emit('play', {
        'tournament_id': tournamentID,
        'player_turn_id': playerTurnID,
        'game_id': gameID,
        'movement': c4_move,
    })



