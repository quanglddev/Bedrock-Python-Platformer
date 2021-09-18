import uuid

from Tools.ClearTool import clear

from Tools.Firebase import Firebase as fs

from backend.User import User

from backend.Game import Game

from time import sleep

from random import shuffle

import pygame 

pygame.init() 
display_surface = pygame.display.set_mode((400, 400)) 
pygame.display.set_caption('Image')
image = pygame.image.load(r'./Villager.png') 

connection = fs()
db = connection.getFirebaseDB()

# ! Change this
me = User("md169", "Melody Davis")

def homepage():
    clear()
    print('======================================================')
    print("======== Welcome to online boardgame platform ========")
    print("========           You gonna love it          ========")
    print('======================================================')
    print("To create a game, type: 'create [game_name] [number_of_player]'")
    print("To join a game, type 'join'")

def on_snapshot(doc_snapshot, changes, read_time):
    clear()
    for doc in doc_snapshot:
        try: 
            print(doc.to_dict()['role'])
            print(doc.to_dict()['des'])
            print(doc.to_dict()['alignment'])
            while True:
                display_surface.blit(image, (0, 0)) 
        except:
            pass

# ! Begin the program
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

    # TODO: Setup cards and listeners
    allCards = new_game.initializeCards()
    # print(len(allCards))
    shuffle(allCards)

    playing_cards = []
    for i in range(number_of_player):
        playing_cards.append(allCards[i])

    # print(len(playing_cards))
    # ! 0-index admin
    print("Your are a: ", playing_cards[0].name)
    print("Description: ", playing_cards[0].des)
    print("Alignment: ", playing_cards[0].alignment)

    for i in range(1, len(playing_cards)):
        data = {
            u'role': playing_cards[i].name,
            u'des': playing_cards[i].des,
            u'alignment': playing_cards[i].alignment,
        }
        db.collection('users').document(player_ids[i]).set(data)
elif user_input == "join":
    # ! join
    doc_ref = db.collection(u'users').document(me.userID)
    doc_ref.set({
        u'role': u'waiting...',
        u'des': u'waiting...',
        u'alignment': u'waiting...',
    })
    # Watch the document
    doc_watch = doc_ref.on_snapshot(on_snapshot)
    doc_watch.unsubscribe()


