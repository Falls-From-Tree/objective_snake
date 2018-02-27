class BaseGem():
    def __init__(self):
        self.attributes = dict(
            serial=None,
            stone=None,
            era=None,
            health=36,
            size=1,
            movement_speed=8,
            arms=2,
            caste_rank=None,
            action_slots=2,
            PP=31,
            SPR=0,
            homo=False,
            hetro=False,
            CPR=0,
            attacking=False,
            blocking=False,
            disarming=False,
            onePR=0,
            twoPR=0,
            threePR=0,
            certs=[]
        )


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


def title():
    print('\ngempire\n\n')


def choose_gem():
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

    return int_decision(min=0, max=15)


def gem_init(players, player, gem_num):
    if gem_num == 0:
        players[player].attributes['stone'] = 'Morganite'
        players[player].attributes['PP'] -= 15
        players[player].attributes['SPR'] += 2
        players[player].attributes['threePR'] += 1
    elif gem_num == 1:
        players[player].attributes['stone'] = 'Sapphire'
        players[player].attributes['PP'] -= 14
        players[player].attributes['SPR'] += 3
    elif gem_num == 2:
        players[player].attributes['stone'] = 'Lapis Lazuli'
        players[player].attributes['PP'] -= 13
        players[player].attributes['SPR'] += 1
        players[player].attributes['threePR'] += 2
    elif gem_num == 3:
        players[player].attributes['stone'] = 'Agate'
        players[player].attributes['PP'] -= 12
        players[player].attributes['SPR'] += 2
        players[player].attributes['CPR'] += 2
    elif gem_num == 4:
        players[player].attributes['stone'] = 'Aquamarine'
        players[player].attributes['PP'] -= 11
        players[player].attributes['SPR'] += 1
        players[player].attributes['CPR'] += 1
        players[player].attributes['threePR'] += 1
    elif gem_num == 5:
        players[player].attributes['stone'] = 'Jasper'
        players[player].attributes['PP'] -= 10
        players[player].attributes['CPR'] += 1
        players[player].attributes['blocking'] += 2
    elif gem_num == 6:
        players[player].attributes['stone'] = 'Topaze'
        players[player].attributes['PP'] -= 9
        players[player].attributes['SPR'] += 1
        players[player].attributes['CPR'] += 1
        players[player].attributes['threePR'] += 1

    elif option == 7:
        pass
    elif option == 8:
        pass
    elif option == 9:
        pass
    elif option == 10:
        pass
    elif option == 11:
        pass
    elif option == 12:
        pass
    elif option == 13:
        pass
    elif option == 14:
        pass
    elif option == 15:
        pass
    else:
        print("\n///please pick a valid number///\n")


def init_players(num_players):
    players = [BaseGem()] * num_players

    for i in range(num_players):
        print('Player {}, you have {} Proficiency Points to spend\n'.format(
              i, players[i].attributes['PP'])
              )

        gem_init(players, i, choose_gem())  # COMBINE CHOOSE AND INIT

    return players


def dec_players():
    num_players = int_decision('How many players?', min=1)
    return init_players(num_players)
