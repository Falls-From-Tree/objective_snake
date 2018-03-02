import Gems

""" Framework/Actions for UI.py

    These low level helper funcitons enable UI.py to remain clean. Most methods
should remain modular and be mixed and matched in UI.py to form a game.
"""


def confirm_input():  # helper for int_decision, confirms player's choice
    while True:
        print('confirm? (y/n)')
        option = input('> ')
        if option is 'y':
            return True
        elif option is 'n':
            return False


def int_decision(text=None, min=None, max=None):  # modular method for integer
    if text is not None:                          # decisions, returns int
        print(text)
    while True:
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


def pp_decision(player, costs, balance, text=None):
    decision = int_decision(text, 0, len(costs) - 1)
    while True:
        if costs[decision] > balance:
            print('///not enough pp///')
            decision = int_decision(min=0, max=len(costs) - 1)
        else:
            player.mod_PP(-costs[decision])
            return decision


def title():  # display title art
    print('\ngempire\n\n')


# I made the costs go from 16-1 instead of 15-0. When ever I thik I know a better way to do somthing that is writen in the doc, I do it but than gradually come to relaize why I had it writen in the doc the first way and then change it back. It was from 16-1 cause off-colros would theroeticly be 0.
def choose_gem(player):  # initilize a gem's base stats
    print('\nPlayer {}, you have {} Proficiency Points to spend\n'.format(
          player.get_serial(),
          player.get_PP()
          ))
    choices = """\nchoose your gemstone:
                 \n0) Morganite - the Philosopher - 16pp
                 \n1) Sapphire - the Advocate - 15pp
                 \n2) Lapis Lazuli - the Planner - 14pp
                 \n3) Agate - the Superintendent - 13pp
                 \n4) Aquamarine - the Inquisitor - 12pp
                 \n5) Jasper - the Intendent - 11pp
                 \n6) Topaze - the Specialist - 10pp
                 \n7) Zircon - the Attorney - 9pp
                 \n8) Peridot - the Technician - 8pp
                 \n9) Amethyst - the Trooper - 7pp
                 \n10) Carnelian - the Stormtrooper - 6pp
                 \n11) Nephrite - the Aviator - 5pp
                 \n12) Rutile - the Enforcer - 4pp
                 \n13) Ruby - the Guardian - 3pp
                 \n14) Pearl - the Servant - 2pp
                 \n15) Bismuth - the Builder - 1pp"""

    gem_num = int_decision(choices, 0, 15)

    if gem_num is 0:
        player.__init__mor__()
    elif gem_num is 1:
        player.__init__sap__()
    elif gem_num is 2:
        player.__init__lap__()
    elif gem_num is 3:
        player.__init__aga__()
    elif gem_num is 4:
        player.__init__aqu__()
    elif gem_num is 5:
        player.__init__jas__()
    elif gem_num is 6:
        player.__init__top__()
    elif gem_num is 7:
        player.__init__zir__()
    elif gem_num is 8:
        player.__init__per__()
    elif gem_num is 9:
        player.__init__ame__()
    elif gem_num is 10:
        player.__init__car__()
    elif gem_num is 11:
        player.__init__lap__()
    elif gem_num is 12:
        player.__init__rut__()
    elif gem_num is 13:
        player.__init__rub__()
    elif gem_num is 14:
        player.__init__per__()
    elif gem_num is 15:
        player.__init__bis__()


def choose_era(player):  # modify base stats for era
    print('\nPlayer {}, you have {} Proficiency Points to spend\n'.format(
          player.get_serial(), player.get_PP()
          ))
    choices = """\nchoose your era:
                 \n0) Era One - 16pp
                 \n1) Era Two - 8pp'
                 \n2) Era Three - 0pp"""

    era_choice = pp_decision(player, {0: 16, 1: 8, 2: 0},
                             player.get_PP(), choices)

    if era_choice is 0:
        player.__init__era__one__()
    elif era_choice is 1:
        player.__init__era__two__()
    else:
        player.__init__era__three__()


def upgrade_weapons(player):  # player can buy weapons with this function
    if player.get_era() is 1:
        pass
    elif player.set_era() is 2:
        pass


def choose_diamond(player):  # modify base stats for diamond
    choices = """\nchoose your diamond:
                 \n0) Blue Diamond
                 \n1) Yellow Diamond"""

    diamond_num = int_decision(choices, 0, 1)

    if diamond_num is 0:
        player.mod_diamond('Blue')
    else:
        player.mod_diamond('Yellow')


# I commented this out just to simplfy my experiments
"""
def upgrade_abilities(player):  # player can buy abilities with this funciton
    done = False
    while player.__attributes['PP'] > 0 and not done:
        print('\nPlayer {}, you have {} '
              'Proficiency Points to spend\n'.format(
               player.__attributes['serial'], player.__attributes['PP'])
              )
        print('\nupgrade an ability?(n to exit)')
        for a in player.__attributes['avalible_abilities']:


            if player.set_ability_level(a) < 4:
                if player.set_ability_level(a) is 0:
                    print('\n{} is not'.format(a.replace('_', ' ')),
                          'unlocked - 1pp')
                else:
                    print('\n{} is level'.format(a.replace('_', ' ')),
                          '{} - 1pp'.format(player.add_ability_level(a)))

        while True:
            decision = input('> ').replace(' ', '_')
            if decision is not 'n':
                if (player.is_ability(decision) and
                   player.set_ability_level(decision) < 4):
                    player.add_PP(-1)
                    player.add_ability_level(decision, 1)
                    break
                else:
                    print('///invalid///')
            else:
                done = True
                break
"""


def choose_serial(player):  # player sets new_serial
    pass


def init_players():  # initilize all player characters
    players = [Gems.BaseGem() for i in
               range(int_decision('How many players?', 1))]

    for i in range(len(players)):  # loops through all players
        choose_gem(players[i])  # initilizes a gem's base stats
        choose_era(players[i])  # modifies base stats for era
        upgrade_weapons(players[i])  # player chooses starting weapons
        choose_diamond(players[i])  # modifies base stats for diamond
#        upgrade_abilities(players[i])  # player chooses starting abilities
        choose_serial(players[i])  # player chooses serial
        # ... other choices

    return players
