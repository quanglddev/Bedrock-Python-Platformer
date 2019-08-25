from Tools.ClearTool import clear
from Tools.Firebase import Firebase as fs

from backend.User import User

from backend.Game import Game

connection = fs()
db = connection.getFirebaseDB()

# ! Change this
me = User("qdl24", "Quang Luong")

def homepage():
    clear()
    print('======================================================')
    print("======== Welcome to online boardgame platform ========")
    print("========           You gonna love it          ========")
    print('======================================================')
    print("To create a game, type: 'create [game_id] [game_name] [number_of_player]'")
    print("To join a game, type: 'join [game_id]'")

# ! Begin the program
while True:
    homepage()
    user_input = input("Please enter your wish: ")
    splitted_user_input = user_input.split()
    if len(splitted_user_input) == 4 and 'create' in user_input:
        # ! Create a new game
        game_id = splitted_user_input[1]
        game_name = splitted_user_input[2]
        number_of_player = int(splitted_user_input[3])

        player_ids = [me.userID]
        for i in range(1, number_of_player):
            newPlayer = input("Enter a player's id here: ")
            player_ids.append(newPlayer)

        new_game = Game(game_id, 'werewolf', player_ids)
    elif len(splitted_user_input) == 2 and 'join' in user_input:
        # ! Join a new game
        game_id = splitted_user_input[1]
    elif user_input == "exit":
        break
    else:
        continue
    # ! Setup cards and listeners

    # ! Later
    # connection.activateChat(game_id) 