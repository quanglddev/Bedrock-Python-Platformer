from backend.Card import Card

class Game:
    # ! Default is werewolf game
    def __init__(self, id, name="werewolf", player_ids=[]):
        self.id = id
        self.name = name
        self.cards = [] # ! An array of card classes
        self.player_ids = player_ids

    def initializeCards(self):
        if self.name == "werewolf":
            card1 = Card('123', 'wolf', 'hello', ['kill']) 
            card2 = Card('456', 'villager', 'hello', []) 
            return [card1, card2]
        return []