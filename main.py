import uuid

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
    print("To create a game, type: 'create [game_name] [number_of_player]'")
    print("To join a game, tell your friend your id")

# ! Begin the program
while True:
    homepage()
    user_input = input("Please enter your wish: ")
    splitted_user_input = user_input.split()
    if len(splitted_user_input) == 3 and 'create' in user_input:
        # ! Create a new game
        game_name = splitted_user_input[1]
        number_of_player = int(splitted_user_input[2])

        player_ids = [me.userID] # <-- array (list)
        for i in range(1, number_of_player):
            newPlayer = input("Enter a player's id here: ")
            player_ids.append(newPlayer)

        new_game = Game(str(uuid.uuid4()), 'werewolf', player_ids)
    elif len(splitted_user_input) == 2 and 'join' in user_input:
        # ! Join a new game
        game_id = splitted_user_input[1]
        # TODO 
    elif user_input == "exit":
        break
    else:
        continue
    # TODO: Setup cards and listeners

    # ! Later
    # connection.activateChat(game_id) 