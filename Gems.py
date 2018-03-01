""" The BaseGem class is the framework for all gems and fusions.

    Base Gem holds all the stats of a gem or fusion in a dict, this dict is
modified through helper funcitons, these functions also return the end value.
Eventually we might keep ability functions here as well. We are still
utilizing child classes.
"""
import StoneAbilities as SA


class BaseGem():
    def __init__gem__(self):
        SA.StoneAbility.__init__ranks__(self)
        self.__attributes = dict(
            serial='test',
            stone=None,
            era=None,
            hardlight_weapon=False,
            health=36,
            size=1,
            movement_speed=8,
            flight_movement_speed=0,
            arms=[],
            caste_rank=None,
            diamond=None,
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
            one_equipment=False,
            one_vehicle=False,
            one_crafting=False,
            twoPR=0,
            two_equipment=False,
            two_vehicle=False,
            two_crafting=False,
            threePR=0,
            three_equipment=False,
            three_vehicle=False,
            three_crafting=False,
            one_abilities=[SA.StoneAbility.shapeshifting(self)],
            two_abilities=[SA.StoneAbility.bubbling(self)],
            three_abilites=[SA.StoneAbility.advanced_form_regeneration(self)],
            avalible_abilities=[],
            certs=[],
        )
        self.attributes_check()

    def attributes_check(self):
        self.__attributes['movement_speed'] = self.__attributes['size'] * 8
        if self.__attributes['SPR'] > 0:
            self.__attributes['homo'] = True
        if self.__attributes['SPR'] > 6:
            self.__attributes['hetro'] = True
        if self.__attributes['CPR'] > 0:
            self.__attributes['attacking'] = True
        if self.__attributes['CPR'] > 6:
            self.__attributes['blocking'] = True
        if self.__attributes['CPR'] > 13:
            self.__attributes['disarming'] = True
        if self.__attributes['onePR'] > 0:
            self.__attributes['one_equipment'] = True
        if self.__attributes['onePR'] > 6:
            self.__attributes['one_vehicle'] = True
        if self.__attributes['onePR'] > 13:
            self.__attributes['one_crafting'] = True
        if self.__attributes['twoPR'] > 0:
            self.__attributes['two_equipment'] = True
        if self.__attributes['twoPR'] > 6:
            self.__atributes['two_vehicle'] = True
        if self.__attributes['twoPR'] > 13:
            self.__attributes['two_crafting'] = True
        if self.__attributes['threePR'] > 0:
            self.__attributes['three_equipment'] = True
        if self.__attributes['threePR'] > 6:
            self.__attributes['three_vehicle'] = True
        if self.__attributes['threePR'] > 13:
            self.__attributes['three_crafting'] = True

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~GEMS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

    def __init__mor__(self):
        self.__attributes['PP'] -= 15
        self.__attributes['stone'] = 'Morganite'
        self.__attributes['SPR'] = +2
        self.__attributes['threePR'] += 1
        self.__attributes['two_abilities'].append(
            SA.StoneAbility.shocking(self)
        )
        self.__attributes['three_abilites'].append(
            SA.StoneAbility.intent_telethesia(self)
        )

    def __init__sap__(self):
        self.__attributes['PP'] -= 14
        self.__attributes['stone'] += 'Sapphire'
        self.__attributes['SPR'] += 3

    def __init__lap__(self):
        self.__attributes['PP'] -= 13
        self.__attributes['stone'] = 'Lapis Lazuli'
        self.__attributes['SPR'] += 1
        self.__attributes['threePR'] += 2

    def __init__aga__(self):
        self.__attributes['PP'] -= 12
        self.__attributes['stone'] = 'Agate'
        self.__attributes['SPR'] += 2
        self.__attributes['CPR'] += 1

    def __init__aqu__(self):
        self.__attributes['PP'] -= 11
        self.__attributes['stone'] = 'Aquamarine'
        self.__attributes['SPR'] += 1
        self.__attributes['CPR'] += 1
        self.__attributes['threePR'] += 1

    def __init__jas__(self):
        self.__attributes['PP'] -= 10
        self.__attributes['stone'] = 'Jasper'
        self.__attributes['CPR'] += 1
        self.__attributes['blocking'] = True

    def __init__top__(self):
        self.__attributes['PP'] -= 9
        self.__attributes['stone'] = 'Topaze'
        self.__attributes['SPR'] += 1
        self.__attributes['CPR'] += 1
        self.__attributes['threePR'] += 1

    def __init__zir__(self):
        self.__attributes['PP'] -= 8
        self.__attributes['stone'] = 'Zircon'
        self.__attributes['SPR'] += 2
        self.__attributes['threePR'] += 1

    def __init__per__(self):
        self.__attributes['PP'] -= 7
        self.__attributes['stone'] = 'Peridot'
        self.__attributes['threePR'] += 1
        self.__attributes['three_vehicle'] = True

    def __init__ame__(self):
        self.__attributes['PP'] -= 6
        self.__attributes['stone'] = 'Amethyst'
        self.__attributes['CPR'] += 3

    def __init__car__(self):
        self.__attributes['PP'] -= 5
        self.__attributes['stone'] = 'Carnelian'
        self.__attributes['CPR'] += 1
        self.__attributes['blocking'] = True

    def __init__nep__(self):
        self.__attributes['PP'] -= 4
        self.__attributes['stone'] = 'Nephrite'
        self.__attributes['threePR'] += 1
        self.__attributes['three_vehicle'] = True

    def __init__rut__(self):
        self.__attributes['PP'] -= 3
        self.__attributes['stone'] = 'Rutile'
        self.__attributes['CPR'] += 1
        self.__attributes['blocking'] = True

    def __init__rub__(self):
        self.__attributes['PP'] -= 2
        self.__attributes['stone'] = 'Ruby'
        self.__attributes['SPR'] += 1
        self.__attributes['CPR'] += 1
        self.__attributes['threePR'] += 1

    def __init__pea__(self):
        self.__attributes['PP'] -= 1
        self.__attributes['stone'] = 'Pearl'
        self.__attributes['SPR'] += 2
        self.__attributes['threePR'] += 1

    def __init__bis__(self):
        self.__attributes['stone'] = 'Bismuth'
        self.__attributes['threePR'] += 1
        self.__attributes['three_crafting'] = True

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ERAS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

    def __init__era__one(self):
        self.__attributes['PP'] -= 16
        self.__attributes['era'] = 1
        self.__attributes['SPR'] += 2
        self.__attributes['onePR'] += 1
        self.__attributes['twoPR'] += 2
        self.__attributes['avalible_abilities'].append(
            self.__attributes['one_abilities'],
            self.__attributes['two_abilities'],
            self.__attributes['three_abilites']
        )

    def __init__era__two(self):
        self.__attributes['PP'] -= 8
        self.__attributes['era'] = 2
        self.__attributes['SPR'] += 1
        self.__attributes['twoPR'] += 1
        self.__attributes['avalible_abilities'].append(
            self.__attributes['two_abilities'],
            self.__attributes['three_abilites']
        )

    def __init__era__three(self):
        self.__attributes['era'] = 0
        self.__attributes['avalible_abilities'].append(
            self.__attributes['three_abilites']
        )

# ~~~~~~~~~~~~~~~~~~~~~~~~~ABILITIES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

    def get_serial(self):
        return self.__attributes['serial']

    def get_PP(self):
        return self.__attributes['PP']

"""
class StoneAbility():
    def shapeshifting(self, rank_up=False):
        self.rank += 0
        if rank_up is True and self.rank < 4:
            self.rank += 1
            if self.rank > 0:
                pass
            if self.rank > 1:
                pass
            if self.rank > 2:
                pass
            if self.rank > 3:
                pass
        else:
            return 'Shapeshifting - rank:{}'.formate(self.rank)

    def bubbling(self, rank_up=False):
        self.rank += 0
        if rank_up is True and self.rank < 4:
            self.rank += 1
            if self.rank > 0:
                pass
            if self.rank > 1:
                pass
            if self.rank > 2:
                pass
            if self.rank > 3:
                pass
        else:
            return 'Bubbling - rank:{}'.formate(self.rank)

    def shocking(self, rank_up=False):
        self.rank += 0
        if rank_up is True and self.rank < 4:
            self.rank += 1
            if self.rank > 0:
                pass
            if self.rank > 1:
                pass
            if self.rank > 2:
                pass
            if self.rank > 3:
                pass
        else:
            return 'Shocking - rank:{}'.formate(self.rank)

    def advanced_form_regeneration(self, rank_up=False):
        self.rank += 0
        if rank_up is True and self.rank < 4:
            self.rank += 1
            if self.rank > 0:
                pass
            if self.rank > 1:
                pass
            if self.rank > 2:
                pass
            if self.rank > 3:
                pass
        else:
            return 'Advanced Form Regeneration - rank:{}'.formate(self.rank)

    def intent_telethesia(self, rank_up=False):
        self.rank += 0
        if rank_up is True and self.rank < 4:
            self.rank += 1
            if self.rank > 0:
                pass
            if self.rank > 1:
                pass
            if self.rank > 2:
                pass
            if self.rank > 3:
                pass
        else:
            return 'Intent Telethesia - rank:{}'.formate(self.rank)
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~NEED TO EXAMINE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

"""
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
"""
