import Gems


""" Framework/Actions for UI.py

    These low level helper funcitons enable UI.py to remain clean. Most methods
should remain modular and be mixed and matched in UI.py to form a game.
"""


def confirm_input():  # helper for int_decision, confirms player's choice
    while(True):
        print('confirm? (y/n)')
        option = input('> ')
        if option == 'y':
            return True
        elif option == 'n':
            return False


def int_decision(text=None, min=None, max=None):  # modular method for integer
    if text is not None:                          # decisions, returns int
        print(text)
    while(True):
        try:
            decision = int(input('> '))
            if ((min is None or decision >= min) &
               (max is None or decision <= max)):
                if confirm_input():
                    return decision
            else:
                print('///invalid///')
        except ValueError:
            print('///invalid///')


def title():  # display title art
    print('\ngempire\n\n')


def choose_gem(player):  # initilize a gem's base stats
    choices = """\nchoose your gemstone:
                 \n0) Morganite - the Philosopher - 15pp
                 \n1) Sapphire - the Advocate - 14pp
                 \n2) Lapis Lazuli - the Planner - 13pp
                 \n3) Agate - the Superintendent - 12pp
                 \n4) Aquamarine - the Inquisitor - 11pp
                 \n5) Jasper - the Intendent - 10pp
                 \n6) Topaze - the Specialist - 9pp
                 \n7) Zircon - the Attorney - 8pp
                 \n8) Peridot - the Technician - 7pp
                 \n9) Amethyst - the Trooper - 6pp
                 \n10) Carnelian - the Stormtrooper - 5pp
                 \n11) Nephrite - the Aviator - 4pp
                 \n12) Rutile - the Enforcer - 3pp
                 \n13) Ruby - the Guardian - 2pp
                 \n14) Pearl - the Servant - 1pp
                 \n15) Bismuth - the Builder - 0pp"""

    gem_num = int_decision(choices, min=0, max=15)

    player.add_PP(gem_num - 15)
    if gem_num == 0:
        player.set_stone('Morganite')
        player.add_SPR(2)
        player.add_threePR(1)
    elif gem_num == 1:
        player.set_stone('Sapphire')
        player.add_SPR(3)
    elif gem_num == 2:
        player.set_stone('Lapis Lazuli')
        player.add_SPR(1)
        player.add_threePR(2)
    elif gem_num == 3:
        player.set_stone('Agate')
        player.add_SPR(2)
        player.add_CPR(2)
    elif gem_num == 4:
        player.set_stone('Aquamarine')
        player.add_SPR(1)
        player.add_CPR(1)
        player.add_threePR(1)
    elif gem_num == 5:
        player.set_stone('Jasper')
        player.add_CPR(1)
        player.set_blocking(2)
    elif gem_num == 6:
        player.set_stone('Topaze')
        player.add_SPR(1)
        player.add_CPR(1)
        player.add_threePR(1)
    elif gem_num == 7:
        pass
    elif gem_num == 8:
        pass
    elif gem_num == 9:
        pass
    elif gem_num == 10:
        pass
    elif gem_num == 11:
        pass
    elif gem_num == 12:
        pass
    elif gem_num == 13:
        pass
    elif gem_num == 14:
        pass
    elif gem_num == 15:
        pass


def choose_era(player):  # modify base stats for era
    choices = """\nchoose your era:
                 \n0) Era One
                 \n1) Era Two'
                 \n2) Era Three"""

    era_num = int_decision(choices, min=0, max=2)

    if era_num == 0:
        pass
    elif era_num == 1:
        pass
    elif era_num == 2:
        pass


def choose_diamond(player):  # modify base stats for diamond
    choices = """\nchoose your diamond:
                 \n0) Blue Diamond
                 \n1) Yellow Diamond"""

    diamond_num = int_decision(choices, min=0, max=1)

    if diamond_num == 0:
        pass
    else:
        pass


def init_players():  # initilize all player characters
    players = [Gems.BaseGem() for i in
               range(int_decision('How many players?', min=1))]

    for i in range(len(players)):  # loops through all players
        print('\nPlayer {}, you have {} Proficiency Points to spend\n'.format(
              i, players[i].add_PP())
              )

        choose_gem(players[i])  # initilizes a gem's base stats
        choose_era(players[i])  # modifies base stats for era
        choose_diamond(players[i])  # modifies base stats for diamond
        # choose_abilities(players, i)  # player chooses starting abilities
        # choose_weapons(players, i)  # player chooses starting weapons
        # choose_serial(players, i)  # player chooses serial
        # ... other choices

    return players
