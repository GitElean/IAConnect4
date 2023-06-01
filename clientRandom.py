#Elean Rivas 19062
#Connect4 Client


from socketIO_client import SocketIO
import random

tournamentID = "142857"
socketIO = SocketIO("127.0.0.1", 4000)


def connect():
    print("Conected")
    socketIO.emit('signin', {
        'user_name': "EleanRandom",
        'tournament_id': tournamentID,
        'user_role': 'player'
})

def signin():
    print("Has ingresado correctamente!")

def ready(data):
    gameID = data['game_id']
    playerTurnID = data['player_turn_id']
    board = data['board']
    move = random.randint(0, 6)

    socketIO.emit('play', {
        'tournament_id': tournamentID,
        'player_turn_id': playerTurnID,
        'game_id': gameID,
        'movement': move
    })


def finish(data):
    gameID = data['game_id']
    playerTurnID = data['player_turn_id']
    winnerTurnID = data['winner_turn_id']
    board = data['board']

    socketIO.emit('player_ready', {
        'tournament_id': tournamentID,
        'player_turn_id': playerTurnID,
        'game_id': gameID
    })


socketIO.on('connect', connect)
socketIO.on('ok_signin', signin)
socketIO.on('ready', ready)
socketIO.on('finish', finish)

socketIO.wait()