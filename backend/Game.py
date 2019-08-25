from backend.Card import Card

class Game:
    # ! Default is werewolf game
    def __init__(self, id, name="werewolf", player_ids=[]):
        self.id = id
        self.name = name
        self.cards = []  # ! An array of card classes
        self.player_ids = player_ids

    def initializeCards(self):
        if self.name == "werewolf":
            return self.getWerewolfCards()
        return []

    def getWerewolfCards(self):
        Werewolf = Card('./assets/Werewolf.png', 'Werewolf',
                        'Each night the Werewolf can vote on a player to kill and talk with the other Werewolves.', 'evil', ['kill'])

        Villager = Card('./assets/Villager.png', 'Villager',
                        'You are a regular villager without any special abilities.', 'good', [''])
        # Alpha_Werewolf = Card('./assets/Alpha_Werewolf.png', 'Alpha Werewolf', 'When the Alpha Werewolf votes on a player to kill during the night, his vote counts twice.', 'unknown', ['kill'])
        Seer = Card('./assets/Seer.png', 'Seer',
                    'Each night, the Seer can see the role of one player.', 'good', ['look'])
        Junior_Werewolf = Card('./assets/Junior_Werewolf.png', 'Junior Werewolf', 'Each night the Werewolf can vote on a player to kill and talk with the other Werewolves. They can also select one player to die with them in any phase ofthe game.', 'evil', ['kill'])
        Lone_Werewolf = Card('./assets/Lone_Werewolf.png', 'Lone Werewolf',
                            'Each night the Werewolf can vote on a player to kill and talk with the other Werewolves but you only win if you are the last werewolf alive.', 'evil', ['kill'])
        Nightmare_Werewolf = Card('./assets/Nightmare_Werewolf.png', 'Nightmare Werewolf', 'Each night the Werewolf can vote on a player to kill and talk with the other Werewolves. Twice during the game, the Nightmare Werewolf can choose a player so that they cannot use their abiliy for a night. ', 'evil', ['kill'])
        Werewolf_Berserk = Card('./assets/Werewolf_Berserk.png', 'Werewolf Berserk', 'Each night the Werewolf can vote on a player to kill and talk with the other Werewolves. Once per game the Werewolf Berserk can announce a Werewolves frenzy during the day. If during the night their target is protected, all protectors of the victim will die.', 'evil', ['kill'])
        Wolf_Seer = Card('./assets/Wolf_Seer.png', 'Wolf Seer', 'Each night can see the role of one player. They can talk with the other Werewolves and provide any information they found. However, the Wolf Seer cannot vote on a player to kill unless they resign their ability to see roles. If they are the last Werewolf alive they instantly resign their seeing ability.', 'evil', ['kill'])
        Wolf_Shaman = Card('./assets/Wolf_Shaman.png', 'Wolf Shaman', 'Each night the Wolf Shaman can vote on a player to kill and talk with the other Werewolves. During the day, the Shaman can put an Enchantment on another player. This will make that player appear as a Shaman Werewolf to the Seer, Aura Seer or Detective.', 'evil', ['kill'])
        Doctor = Card('./assets/Doctor.png', 'Doctor',
                    'Each night the Doctor can select one player to heal. If this player is attacked by the Werewolves, they do not die in that night.', 'good', ['heal'])
        Bodyguard = Card('./assets/Bodyguard.png', 'Bodyguard', 'Each night the Bodyguard can select one player to protect. They also automatically protect themselves. If the Bodyguard or the player they are protecting gets attacked, they will survive. However, if they are attacked again the bodyguard will die.', 'good', ['protect'])
        Tough_Guy = Card('./assets/Tough_Guy.png', 'Tough Guy', ' You can choose one player to protect every night. If you or that player is attacked, neither dies and instead you and the attacker will both see each one role. Because of your injuries, you will die at the end of the following day.', 'good', ['protect'])
        Gunner = Card('./assets/Gunner.png', 'Gunner', 'You have two bullets which you can use to kill somebody. The shots are very loud so that your role will be revealed after the first shot', 'unknown', ['kill'])
        Jailer = Card('./assets/Jailer.png', 'Jailer', 'Select a target each day to put in jail during the next night. At night you can talk privately with your target. Your target cannot act or be attacked, but if you find him suspicious, you can kill him. if you do not have bullets you can still imprison players to protect against attacks', 'unknown', ['protect'])
        Red_Lady = Card('./assets/Red_Lady.png', 'Red Lady', 'At night you can visit another player. If you are attacked that night, you will not be killed. However, if you visit a player that is evil or is attacked, you will die.', 'good', [''])
        Priest = Card('./assets/Priest.png', 'Priest',
                    'You can throw holy water on another player. If that player is a werewolf, he dies. If he is not a werewolf, you die. You can only use it once.', 'good', ['exorcist'])
        Marksman = Card('./assets/Marksman.png', 'Marksman', 'At night you can mark a player as your target. After the next day, you can kill or change your target. If you try to kill a villager, your shot will be backfire and kill you. You have two arrows.', 'unknown', ['hunt'])
        Aura_Seer = Card('./assets/Aura_Seer.png', 'Aura Seer', 'Each night you can select a player to uncover his alignment', 'good', [''])
        Spirit_Seer = Card('./assets/Spirit_Seer.png', 'Spirit Seer',
                        'Each night you can select two players. At the beginning of the next day you will be informed if either of those two players has killed last night.', 'good', ['inform'])
        Seer_Apprentice = Card('./assets/Seer_Apprentice.png', 'Seer Apprentice', 'You are a normal villager until the seer dies, at which point you become the new seer.', 'good', ['look'])
        Detective = Card('./assets/Detective.png', 'Detective',
                        'Each night you can select two players to uncover if they are in the same team.', 'good', ['reveal'])
        Medium = Card('./assets/Medium.png', 'Medium',
                    'During the night you can talk anonymously with the dead. Once during the game you can revive a dead player.', 'unknown', ['revive'])
        Mayor = Card('./assets/Mayor.png', 'Mayor',
                    'Once during the game you can reveal your role which will make your vote count double during the rest of the game.', 'good', ['vote'])
        Witch = Card('./assets/Witch.png', 'Witch', 'You have two potions: One will kill and the other will protect a player.', 'unknown', ['kill'])
        Avenger = Card('./assets/Avenger.png', 'Avenger', 'The Avenger can select a player to kill with them when they die.', 'good', ['kill'])
        Beast_Hunter = Card('./assets/Beast_Hunter.png', 'Beast Hunter', 'At night you can place a trap on a player which will become active the following night. This player cannot be killed at night. If the player is attacked by werewolves, the nearest werewolf to the left will die.', 'unknown', [''])
        Pacifist = Card('./assets/Pacifist.png', 'Pacifist',
                        'Once per game you can reveal the role of a player to everybody and prevent anybody from voting that day.', 'good', ['peace'])
        Grumpy_Grandma = Card('./assets/Grumpy_Grandma.png', 'Grumpy Grandma', 'At night you can select a player who cannot talk during the next day.', 'good', ['silence'])
        Cupid = Card('./assets/Cupid.png', 'Cupid', 'During the first night you can select two players to be a love couple.', 'good', ['match'])
        Cursed = Card('./assets/Cursed.png', 'Cursed',
                    'You are a villager until the werewolves try to kill you, at which point you become a werewolf.', 'good', ['change'])
# = Card('./assets/.png', '', '', 'good', [''])

        allCards = [Werewolf, Villager, Beast_Hunter, Tough_Guy, Doctor, Bodyguard, Detective, Spirit_Seer, Aura_Seer, Marksman, Werewolf_Berserk, Pacifist, Avenger, Red_Lady, Priest, Jailer, Grumpy_Grandma, Witch, Mayor, Medium, Gunner, Wolf_Shaman, Cupid, Wolf_Seer, Nightmare_Werewolf, Cursed, Lone_Werewolf, Junior_Werewolf, Seer, Seer_Apprentice]

        return allCards
