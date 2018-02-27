import BaseGem


def confirm_input():
    while(True):
        print('confirm? (y/n)')
        option = input('>')
        if option == 'y':
            return True
        elif option == 'n':
            return False


def int_decision(text=None, min=None, max=None):
    while(True):
        if text is not None:
            print(text)
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


def title():  # eventually will produce some sort of art
    print('\ngempire\n\n')


def gem_init(players, player):  # sets up a single gem
    choose_gem(players, player)
    # chooe_era
    # choose_diamond


def choose_gem(players, player):
    print('choose your gemstone:\n',
          '\n0) Morganite - the Philosopher - 15pp',
          '\n1) Sapphire - the Advocate - 14pp',
          '\n2) Lapis Lazuli - the Planner - 13pp',
          '\n3) Agate - the Superintendent - 12pp',
          '\n4) Aquamarine - the Inquisitor - 11pp',
          '\n5) Jasper - the Intendent - 10pp',
          '\n6) Topaze - the Specialist - 9pp',
          '\n7) Zircon - the Attorney - 8pp',
          '\n8) Peridot - the Technician - 7pp',
          '\n9) Amethyst - the Trooper - 6pp',
          '\n10) Carnelian - the Stormtrooper - 5pp',
          '\n11) Nephrite - the Aviator - 4pp',
          '\n12) Rutile - the Enforcer - 3pp',
          '\n13) Ruby - the Guardian - 2pp',
          '\n14) Pearl - the Servant - 1pp',
          '\n15) Bismuth - the Builder - 0pp'
          )

    gem_num = int_decision(min=0, max=15)
    players[player].add_PP(gem_num - 15)

    if gem_num == 0:
        players[player].set_stone('Morganite')
        players[player].add_SPR(2)
        players[player].add_threePR(1)
    elif gem_num == 1:
        players[player].set_stone('Sapphire')
        players[player].add_SPR(3)
    elif gem_num == 2:
        players[player].set_stone('Lapis Lazuli')
        players[player].add_SPR(1)
        players[player].add_threePR(2)
    elif gem_num == 3:
        players[player].set_stone('Agate')
        players[player].add_SPR(2)
        players[player].add_CPR(2)
    elif gem_num == 4:
        players[player].set_stone('Aquamarine')
        players[player].add_SPR(1)
        players[player].add_CPR(1)
        players[player].add_threePR(1)
    elif gem_num == 5:
        players[player].set_stone('Jasper')
        players[player].add_CPR(1)
        players[player].set_blocking(2)
    elif gem_num == 6:
        players[player].set_stone('Topaze')
        players[player].add_SPR(1)
        players[player].add_CPR(1)
        players[player].add_threePR(1)

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


def init_players(num_players):
    players = [BaseGem() for i in range(
               int_decision('How many players?', min=1))]

    for i in range(num_players):  # loops through all players
        print('Player {}, you have {} Proficiency Points to spend\n'.format(
              i, players[i].attributes['PP'])
              )

        gem_init(players, i)  # initilizes a player's gems

    return players
