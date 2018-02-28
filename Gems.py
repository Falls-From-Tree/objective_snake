""" The BaseGem class is the framework for all gems and fusions.

    Base Gem holds all the stats of a gem or fusion in a dict, this dict is
modified through helper funcitons, these functions also return the end value.
Eventually we might keep ability functions here as well. We are still
utilizing child classes.
"""


class BaseGem():
    def __init__(self, init_serial):
        self.__attributes = dict(
            serial=init_serial,
            stone=None,
            era=None,
            health=36,
            size=1,
            movement_speed=8,
            flight_movement_speed=0,
            arms=[],
            caste_rank=None,
            diamond='',
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
            certs=[],
            abilities={'bubbling': -2, 'shape_shifting': -1}
        )

#
#
# ~~~~~~~~~~~~~~~HELPER CLASSES FOR ACCESSING AND MODIFYING STATS~~~~~~~~~~~~~~

    def set_serial(self, new_serial=None):
        if new_serial is not None:
            self.__attributes['serial'] = new_serial
        return self.__attributes['serial']

    def set_stone(self, new_stone=None):
        if new_stone is not None:
            self.__attributes['stone'] = new_stone
        return self.__attributes['stone']

    def set_era(self, new_era=None):
        if new_era is not None:
            self.__attributes['era'] = new_era
        return self.__attributes['era']

    def add_health(self, health_mod=None):
        if health_mod is not None:
            self.__attributes['health'] += health_mod
        return self.__attributes['health']

    # size should probably always be powers of 2
    # this also modifies movement_speed
    def set_size(self, new_size=None):
        if new_size is not None:
            self.__attributes['size'] = new_size
            self.__attributes['movemen_speed'] = new_size * 8
        return self.__attributes['size']

    def get_movement_speed(self):
        return self.__attributes['movement_speed']

    def add_flight_movement_speed(self, f_movement_speed_mod=None):
        if f_movement_speed_mod is not None:
            self.__attributes['flight_movement_speed'] += f_movement_speed_mod
        return self.__attributes['flight_movement_speed']

    def get_arms(self):
        return self.__attributes['arms']

    def add_caste_rank(self, caste_rank_mod=None):
        if caste_rank_mod is not None:
            self.__attributes['caste_rank'] += caste_rank_mod
        return self.__attributes['caste_rank']

    def set_diamond(self, new_diamond=None):
        if new_diamond is not None:
            self.__attributes['diamond'] = new_diamond
        return self.__attributes['diamond']

    def add_action_slots(self, action_slots_mod=None):
        if action_slots_mod is not None:
            self.__attributes['action_slots'] += action_slots_mod
        return self.__attributes['action_slots']

    def add_PP(self, PP_mod=None):
        if PP_mod is not None:
            self.__attributes['PP'] += PP_mod
        return self.__attributes['PP']

    def add_SPR(self, SPR_mod=None):
        if SPR_mod is not None:
            self.__attributes['SPR'] += SPR_mod
        return self.__attributes['SPR']

    def set_homo(self, new_homo=None):
        if new_homo is not None:
            self.__attributes['homo'] = new_homo
        return self.__attributes['homo']

    def set_hetro(self, new_hetro=None):
        if new_hetro is not None:
            self.__attributes['hetro'] = new_hetro
        return self.__attributes['hetro']

    def add_CPR(self, CPR_mod=None):
        if CPR_mod is not None:
            self.__attributes['CPR'] += CPR_mod
        return self.__attributes['CPR']

    def set_attacking(self, new_attacking=None):
        if new_attacking is not None:
            self.__attributes['attacking'] = new_attacking
        return self.__attributes['attacking']

    def set_blocking(self, new_blocking=None):
        if new_blocking is not None:
            self.__attributes['blocking'] = new_blocking
        return self.__attributes['blocking']

    def set_disarming(self, new_disarming=None):
        if new_disarming is not None:
            self.__attributes['disarming'] = new_disarming
        return self.__attributes['disarming']

    def add_onePR(self, onePR_mod=None):
        if onePR_mod is not None:
            self.__attributes['onePR'] += onePR_mod
        return self.__attributes['onePR']

    def add_twoPR(self, twoPR_mod=None):
        if twoPR_mod is not None:
            self.__attributes['twoPR'] += twoPR_mod
        return self.__attributes['twoPR']

    def add_threePR(self, threePR_mod=None):
        if threePR_mod is not None:
            self.__attributes['threePR'] += threePR_mod
        return self.__attributes['threePR']

    def add_cert(self, new_cert=None):
        if new_cert is not None:
            self.__attributes['certs'].append(new_cert)
        return self.__attributes['certs']

    def ability_list(self):
        return list(self.__attributes['abilities'].keys())

    def is_ability(self, ability):
        return ability in self.__attributes['abilities']

    def set_ability_level(self, ability, new_level=None):
        if ability in self.__attributes['abilities']:
            if new_level is not None:
                self.__attributes['abilities'][ability] = new_level
            return self.__attributes['abilities'][ability]
        else:
            return -1

    def add_ability_level(self, ability, level_mod=None):
        if ability in self.__attributes['abilities']:
            if level_mod is not None:
                self.__attributes['abilities'][ability] += level_mod
            return self.__attributes['abilities'][ability]
        else:
            return -1

    def add_ability(self, ability, level):
        if ability not in self.__attributes['abilities']:
            self.__attributes['abilities'][ability] = level

    def rm_ability(self, ability):
        return self.__attributes['abilities'].pop(ability)

    def can_upgrade(self):
        if self.__attributes['PP'] > 0:
            for a in self.__attributes['abilities']:
                if self.__attributes['abilities'][a] < 4:
                    return True
        return False

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~END OF HELPER CLASSES~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ABILITIES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def print_abilities(self):
        for a in self.__attributes['abilities']:
            print(a)

    def print_unlocked_abilities(self):
        for a in self.__attributes['abilities']:
            if self.__attributes['abilities'][a] > -1:
                print(a)
