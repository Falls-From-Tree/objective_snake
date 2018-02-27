class BaseGem():
    def __init__(self):
        self.attributes = dict(
            serial=None,
            stone=None,
            era=None,
            health=36,
            size=1,
            movement_speed=None,
            flight_movement_speed=0,
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

    def mod_serial(self, new_serial):
        self.attributes['serial'] = new_serial

    def mod_stone(self, new_stone):
        self.attributes['stone'] = new_stone

    def mod_era(self, new_era):
        self.attributes['era'] = new_era

    def mod_health(self, health_mod):
        self.attributes['health'] += health_mod

    # size should probably always be powers of 2
    # this also modifies movement_speed
    def mod_size(self, new_size):
        self.attributes['size'] = new_size
        self.attributes['movementspeed'] = new_size*8

    def mod_flight_movement_speed(self, flight_movement_speed_mod):
        self.attributes['flight_movement_speed'] += flight_movement_speed_mod

    def mod_arms(self, arms_mod):
        self.attributes['arms'] += arms_mod

    def mod_caste_rank(self, caste_rank_mod):
        self.attributes['caste_rank'] += caste_rank_mod

    def mod_action_slots(self, action_slots_mod):
        self.attributes['action_slots'] += action_slots_mod

    def mod_PP(self, PP_mod):
        self.attributes['PP'] += PP_mod

    def mod_SPR(self, SPR_mod):
        self.attributes['SPR'] += SPR_mod

    def mod_homo(self, mod_homo):
        self.attributes['homo'] = mod_homo

    def mod_hetro(self, mod_hetro):
        self.attributes['hetro'] = mod_hetro

    def mod_CPR(self, CPR_mod):
        self.attributes['CPR'] += CPR_mod

    def mod_attacking(self, mod_attacking):
        self.attributes['attacking'] = mod_attacking

    def mod_blocking(self, mod_blocking):
        self.attributes['blocking'] = mod_blocking

    def mod_disarming(self, mod_disarming):
        self.attributes['disarming'] = mod_disarming

    def mod_onePR(self, onePR_mod):
        self.attributes['onePR'] += onePR_mod

    def mod_twoPR(self, twoPR_mod):
        self.attributes['twoPR'] += twoPR_mod

    def mod_threePR(self, threePR_mod):
        self.attributes['threePR'] += threePR_mod

    def mod_certs(self, new_cert):
        self.attributes['certs'].append(new_cert)


def title():
    print('\ngempire\n\n')
    return start()


def start():
    print('how many players?')
    global playerCount
    playerCount = intDecision(start, min=1)
    return makeGem()


def intDecision(loop, min=None, max=None):
    option = intInput(loop)
    if ((min is None or option >= min) & (max is None or option <= max)):
        if confirmInput():
            return option
        else:
            return loop()
    else:
        return invalid(loop)


def intInput(loop):
    try:
        option = int(input('>'))
        return option
    except ValueError:
        return invalid(loop)


def invalid(loop):
    print('///invalid///')
    return loop()


def confirmInput():
    print('confirm? (y/n)')
    option = input('>')
    if option == 'y':
        return True
    elif option == 'n':
        return False
    else:
        return invalid(confirmInput)


def makeGem():
    global playerList
    playerList = []
    for player in range(playerCount):
        newGem = BaseGem()
        playerList.append(newGem)
        chooseStone(newGem)


def chooseStone(gem):
    print('player {}, you have {} Proficiency Points to spend'.format(
        playerList.index(gem), gem.attributes['PP'])
         )
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
# don't know why but this breaks it, causes chooseStone to infinatly loop
#    gem_choice = intDecision(chooseStone(gem), min=0, max=15)
    """
    if gem_choice == 0:
        Gem(playerList[player]).mod_stone('Morganite')
        Gem(player).mod_PP(15)
        playerList[player].attributes['SPR'] += 2
        playerList[player].attributes['threePR'] += 1
    elif gem_choice == 1:
        playerList[player].attributes['stone'] = 'Sapphire'
        playerList[player].attributes['PP'] -= 14
        playerList[player].attributes['SPR'] += 3
    elif gem_choice == 2:
        playerList[player].attributes['stone'] = 'Lapis Lazuli'
        playerList[player].attributes['PP'] -= 13
        playerList[player].attributes['SPR'] += 1
        playerList[player].attributes['threePR'] += 2
    elif gem_choice == 3:
        playerList[player].attributes['stone'] = 'Agate'
        playerList[player].attributes['PP'] -= 12
        playerList[player].attributes['SPR'] += 2
        playerList[player].attributes['CPR'] += 2
    elif gem_choice == 4:
        playerList[player].attributes['stone'] = 'Aquamarine'
        playerList[player].attributes['PP'] -= 11
        playerList[player].attributes['SPR'] += 1
        playerList[player].attributes['CPR'] += 1
        playerList[player].attributes['threePR'] += 1
    elif gem_choice == 5:
        playerList[player].attributes['stone'] = 'Jasper'
        playerList[player].attributes['PP'] -= 10
        playerList[player].attributes['CPR'] += 1
        playerList[player].attributes['blocking'] += 2
    elif gem_choice == 6:
        playerList[player].attributes['stone'] = 'Topaze'
        playerList[player].attributes['PP'] -= 9
        playerList[player].attributes['SPR'] += 1
        playerList[player].attributes['CPR'] += 1
        playerList[player].attributes['threePR'] += 1

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
"""


title()
