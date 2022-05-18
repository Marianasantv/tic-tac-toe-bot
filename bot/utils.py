"""
[Module] Tic-tac-toe bot utilities.
"""

from random import randint
import requests
from urllib.parse import unquote


API_URL = "http://127.0.0.1:8000"


def is_registry_open():
    """
    Checks if registry is available via API.
    """
    try:
        url = "{}/registry".format(API_URL)
        res = requests.get(url)

        if res.text == "true":
            return True
        elif res.text == "false":
            return False

    except:
        return False


def register_user(name):
    """
    Registers user in API game.
    """
    url = "{}/register_player/{}".format(API_URL, name)
    res = requests.post(url)
    player_id = res.text[1]
    return player_id


def is_my_turn(player_id): 
    """
    Checks if it is our turn via API.
    """
    url = "{}/turn/{}".format(API_URL, player_id)
    res = requests.get(url)
    
    if res.text == "true":
        return True
    elif res.text == "false":
        return False


def read_board():
    """
    Gets game board via API.
    """
    url = "{}/board".format(API_URL)
    res = requests.get(url)
    board_str = res.text
    board = [
        [board_str[1], board_str[2], board_str[3]], 
        [board_str[4], board_str[5], board_str[6]], 
        [board_str[7], board_str[8], board_str[9]]
    ]

    return board


def decide_move(board, player_id):
    """
    Decides next move to make.
    """
    # Calcular quien es el enemy
    enemy = "X"
    if player_id == "X":
        enemy = "O"

    # PASO 1 - BLOQUEAR
    # verificar si el enemy va a ganar -> bloquear
    if board[0][0] == enemy and board[0][1] == enemy and board[0][2] == "-":
        return [0, 2]
    if board[0][0] == enemy and board[1][0] == enemy and board[2][0] == "-":
        return [2, 0]
    if board[1][0] == enemy and board[1][1] == enemy and board[1][2] == "-":
        return [1, 2]
    if board[2][0] == enemy and board[2][1] == enemy and board[2][2] == "-":
        return [2, 2]
    if board[0][1] == enemy and board[1][1] == enemy and board[2][1] == "-":
        return [2, 1] 
    if board[0][2] == enemy and board[1][2] == enemy and board[2][2] == "-":         
        return [2, 2] 
    if board[0][0] == enemy and board[1][1] == enemy and board[2][2] == "-":         
        return [2, 2]
    if board[0][0] == enemy and board[2][2] == enemy and board[1][1] == "-":         
        return [1, 1]
    if board[1][1] == enemy and board[2][2] == enemy and board[0][0] == "-":         
        return [0, 0]
    if board[2][0] == enemy and board[1][1] == enemy and board[0][2] == "-":         
        return [0, 2]
    if board[2][0] == enemy and board[0][2] == enemy and board[1][1] == "-":         
        return [1, 1]
    if board[1][1] == enemy and board[0][2] == enemy and board[2][0] == "-":         
        return [2, 0]
    if board[1][0] == enemy and board[2][0] == enemy and board[0][0] == "-":         
        return [0, 0]
    if board[0][0] == enemy and board[2][0] == enemy and board[1][0] == "-":         
        return [1, 0]
    if board[1][1] == enemy and board[2][1] == enemy and board[0][1] == "-":         
        return [0, 1]
    if board[0][1] == enemy and board[2][1] == enemy and board[1][1] == "-":         
        return [1, 1]
    if board[0][2] == enemy and board[1][2] == enemy and board[2][2] == "-":         
        return [2, 2]
    if board[2][2] == enemy and board[1][2] == enemy and board[0][2] == "-":         
        return [0, 2]
    if board[0][2] == enemy and board[2][2] == enemy and board[1][2] == "-":         
        return [1, 2]
    if board[0][1] == enemy and board[0][2] == enemy and board[0][0] == "-":         
        return [0, 0]
    if board[0][0] == enemy and board[0][2] == enemy and board[0][1] == "-":         
        return [0, 1]
    if board[1][2] == enemy and board[1][0] == enemy and board[1][1] == "-":         
        return [1, 1]
    if board[1][1] == enemy and board[1][2] == enemy and board[1][0] == "-":         
        return [1, 0]
    if board[2][2] == enemy and board[2][1] == enemy and board[2][0] == "-":         
        return [2, 0]
    if board[2][0] == enemy and board[2][2] == enemy and board[2][1] == "-":         
        return [2, 1]
    
    
    # si llega a este punto - puedo hacer cualquier movimiento
    
    # PASO 2 - GANAR?
    # verificar si yo voy a ganar, entonces retornar el unico que me falta
    if board[0][0] == player_id and board[0][1] == player_id and board[0][2] == "-":
        return [0, 2]
    if board[0][0] == player_id and board[1][0] == player_id and board[2][0] == "-":
        return [2, 0]
    if board[0][1] == player_id and board[0][2] == player_id and board[0][0] == "-":
        return [0, 0]
    if board[0][0] == player_id and board[0][2] == player_id and board[0][1] == "-":
        return [0, 1]
    if board[1][0] == player_id and board[1][1] == player_id and board[1][2] == "-":
        return [1,2]
    if board[1][2] == player_id and board[1][1] == player_id and board[1][0] == "-":
        return [1, 0]
    if board[1][0] == player_id and board[1][2] == player_id and board[1][1] == "-":
        return [1, 1]
    if board[2][2] == player_id and board[2][1] == player_id and board[2][0] == "-":
        return [2, 0]
    if board[2][0] == player_id and board[2][2] == player_id and board[2][1] == "-":
        return [2, 1]
    if board[2][0] == player_id and board[2][1] == player_id and board[2][2] == "-":
        return [2, 2]
    if board[2][0] == player_id and board[0][0] == player_id and board[1][0] == "-":
        return [1, 0]
    if board[1][0] == player_id and board[2][0] == player_id and board[0][0] == "-":
        return [0, 0]
    if board[0][1] == player_id and board[1][1] == player_id and board[2][1] == "-":
        return [2, 1]
    if board[2][1] == player_id and board[0][1] == player_id and board[1][1] == "-":
        return [1, 1]
    if board[2][1] == player_id and board[1][1] == player_id and board[0][1] == "-":
        return [0, 1]
    if board[0][2] == player_id and board[1][2] == player_id and board[2][2] == "-":
        return [2, 2]
    if board[2][2] == player_id and board[0][2] == player_id and board[1][2] == "-":
        return [1, 2]
    if board[2][2] == player_id and board[1][2] == player_id and board[0][2] == "-":
        return [0, 2]
    if board[0][2] == player_id and board[1][1] == player_id and board[2][0] == "-":
        return [2, 0]
    if board[2][0] == player_id and board[0][2] == player_id and board[1][1] == "-":
        return [1, 1]
    if board[2][0] == player_id and board[1][1] == player_id and board[0][2] == "-":
        return [0, 2]
    if board[2][2] == player_id and board[1][1] == player_id and board[0][0] == "-":
        return [0, 0]
    if board[0][0] == player_id and board[2][2] == player_id and board[1][1] == "-":
        return [1, 1]    
    if board[0][0] == player_id and board[1][1] == player_id and board[2][2] == "-":
        return [2, 2]
    

    # PASO 3 - ESQUINA
    # ver si las esquinas estan vacias
    if board[2][0] == "-":
        return[2,0]
    if board[0][2] == "-":
        return[0,2]
    if board[0][0] == "-":
        return[0,0]
    if board[2][2] == "-":
        return[2,2]
    
    # otras estrategias ara comenzar 
    if board[2][0] == player_id and board[1][1] == enemy and board[0][2] == "-":         
        return [0, 2]
    if board[2][0] == player_id and board[1][0] == enemy and board[2][2] == "-":         
        return [2, 2]
    if board[2][0] == player_id and board[2][1] == enemy and board[2][2] == "-":         
        return [2, 2]
    if board[2][0] == player_id and board[0][0] == enemy and board[2][2] == "-":         
        return [2, 2]
    if board[2][0] == player_id and board[1][2] == enemy and board[2][2] == "-":         
        return [2, 2]
    if board[2][0] == player_id and board[0][1] == enemy and board[2][2] == "-":         
        return [2, 2]
    
    
    # Ultimo recurso, que sea random
    row = randint(0, 2)
    column = randint(0, 2)
    return [row, column]


def validate_move(board, move):
    """
    Checks if the desired next move hits an empty position.
    """
    row, col = move[0], move[1]

    if board[row][col] == "-":
        return True

    return False


def send_move(player_id, move):
    """
    Sends move to API.
    """
    row, col = move[0], move[1]
    url = "{}/move/{}/{}/{}".format(API_URL, player_id, row, col)
    res = requests.post(url)
    return None


def does_game_continue():
    """
    Checks if the current match continues via API.
    """
    url = "{}/continue".format(API_URL)
    res = requests.get(url)

    if res.text == "true":
        return True
    elif res.text == "false":
        return False


def print_board(board):
    '''
    Prints the baord in console to watch the game.
    '''
    print("\nCurrent board: \n")
    print(board[0][0], "|", board[0][1], "|", board[0][2])
    print("----------")
    print(board[1][0], "|", board[1][1], "|", board[1][2])
    print("----------")
    print(board[2][0], "|", board[2][1], "|", board[2][2], "\n")


