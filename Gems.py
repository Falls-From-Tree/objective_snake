import StoneAbilities as SA

""" The BaseGem class is the framework for all gems and fusions.

    Base Gem holds all the stats of a gem or fusion in a dict, this dict is
modified through helper funcitons, these functions also return the end value.
Eventually we might keep ability functions here as well. We are still
utilizing child classes.
"""

# we've stil got to add the advance tech attributes which should coralate to era 4, but we don't have to do that right now
class BaseGem():
    def __init__(self):
        SA.StoneAbility.__init__ranks__(self)
        self.__attributes = dict(
            serial=None,
            stone=None,
            era=0,
            hardlight_weapon=False,
            health=36,
            size=1,
            movement_speed=0,
            flight_movement_speed=0,
            arms=[],
            caste_rank=0,
            diamond=None,
            action_slots=2,
            PP=32,
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


# these are some basic checks that should happen frequently to players, special during combat, to keep their attributes accurate
    def attributes_check(self):
        self.mod_movement_speed(self.get_size()*8)
        if self.get_SPR() > 0:
            self.mod_homo(True)
        if self.get_SPR() > 6:
            self.mod_hetro(True)
        if self.get_CPR() > 0:
            self.mod_attacking(True)
        if self.get_SPR() > 6:
            self.mod_blocking(True)
        if self.get_CPR() > 13:
            self.mod_disarming(True)
        if self.get_onePR() > 0:
            self.mod_one_equipment(True)
        if self.get_onePR() > 6:
            self.mod_one_vehicle(True)
        if self.get_onePR() > 13:
            self.mod_one_crafting(True)
        if self.get_twoPR() > 0:
            self.mod_two_equipment(True)
        if self.get_twoPR() > 6:
            self.mod_two_vehicle(True)
        if self.get_twoPR() > 13:
            self.mod_two_crafting(True)
        if self.get_threePR() > 0:
            self.mod_two_equipment(True)
        if self.get_threePR() > 6:
            self.mod_two_vehicle(True)
        if self.get_threePR() > 13:
            self.mod_three_crafting(True)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~GEMS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# After playing around with it for a while I think an implemeentation like below would be best. I want everyting about the gems contained in here such that all we have to do is calll one fucntion to initalize any new players from framework. While messing around with it, I think what was bothering me with the previous method was that we were adding strings and coroposding valsue to a dictionary to list abilites, but I think abialites should be objects. With this method a gem is initalied with all her abiietes dvided by era, but here own era furthur dilineates which of her own abiliets she has access too. This system has the potenal to allow gems to gain older era abilaites if we ever implement a game mechinic that would allow for that.
    def __init__mor__(self):
        self.mod_PP(-15)
        self.mod_stone('Morganite')
        self.mod_caste_rank(16)
        self.mod_SPR(2)
        self.mod_threePR(1)
        self.mod_two_abilities(SA.StoneAbility.shocking(self))
        self.mod_three_abilities(SA.StoneAbility.intent_telethesia(self))

    def __init__sap__(self):
        self.mod_PP(-14)
        self.mod_stone('Sapphire')
        self.mod_caste_rank(15)
        self.mod_SPR(3)

    def __init__lap__(self):
        self.mod_PP(-13)
        self.mod_stone('Lapis Lazuli')
        self.mod_caste_rank(14)
        self.mod_SPR(1)
        self.mod_threePR(2)

    def __init__aga__(self):
        self.mod_PP(-12)
        self.mod_stone('Agate')
        self.mod_caste_rank(13)
        self.mod_SPR(2)
        self.mod_CPR(1)

    def __init__aqu__(self):
        self.mod_PP(-11)
        self.mod_stone('Aquamarine')
        self.mod_caste_rank(12)
        self.mod_SPR(1)
        self.mod_CPR(1)
        self.mod_threePR(1)

    def __init__jas__(self):
        self.mod_PP(-10)
        self.mod_stone('Jasper')
        self.mod_caste_rank(11)
        self.mod_CPR(1)
        self.mod_blocking(True)

    def __init__top__(self):
        self.mod_PP(-9)
        self.mod_stone('Topaze')
        self.mod_caste_rank(10)
        self.mod_SPR(1)
        self.mod_CPR(1)
        self.mod_threePR(1)

    def __init__zir__(self):
        self.mod_PP(-8)
        self.mod_stone('Zircon')
        self.mod_caste_rank(9)
        self.mod_SPR(2)
        self.mod_threePR(1)

    def __init__per__(self):
        self.mod_PP(-7)
        self.mod_stone('Peridot')
        self.mod_caste_rank(8)
        self.mod_threePR(1)
        self.mod_three_vehicle(True)

    def __init__ame__(self):
        self.mod_PP(-6)
        self.mod_stone('Amethyst')
        self.mod_caste_rank(7)
        self.mod_CPR(3)

    def __init__car__(self):
        self.mod_PP(-5)
        self.mod_stone('Carnelian')
        self.mod_caste_rank(6)
        self.mod_CPR(1)
        self.mod_blocking(True)

    def __init__nep__(self):
        self.mod_PP(-4)
        self.mod_stone('Nephrite')
        self.mod_caste_rank(5)
        self.mod_threePR(1)
        self.mod_three_vehicle(True)

    def __init__rut__(self):
        self.mod_PP(-3)
        self.mod_stone('Rutile')
        self.mod_caste_rank(4)
        self.mod_CPR(1)
        self.mod_disarming(True)

    def __init__rub__(self):
        self.mod_PP(-2)
        self.mod_stone('Ruby')
        self.mod_caste_rank(3)
        self.mod_SPR(1)
        self.mod_CPR(1)
        self.mod_threePR(1)

    def __init__pea__(self):
        self.mod_PP(-1)
        self.mod_stone('Pearl')
        self.mod_caste_rank(2)
        self.mod_SPR(2)
        self.mod_threePR(1)

    def __init__bis__(self):
        self.mod_stone('Bismuth')
        self.mod_caste_rank(1)
        self.mod_threePR(1)
        self.mod_three_crafting(True)

# ~~~~~~~~~~~~~~~~~~~~~~~~~ERAS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# I don't know if the "self.mod_avalible_abilities" stuff here actauly works, I looked it up and I think this is what it should be but it might not be

    def __init__era__one__(self):
        self.mod_PP(-16)
        self.mod_era(1)
        self.mod_SPR(2)
        self.mod_onePR(1)
        self.mod_twoPR(2)
        self.mod_avalible_abilities(
            self.get_one_abilities() +
            self.get_two_abilities() +
            self.get_three_abilities()
        )

    def __init__era__two__(self):
        self.mod_PP(-8)
        self.mod_era(2)
        self.mod_SPR(1)
        self.mod_twoPR(1)
        self.mod_avalible_abilities(
            self.get_two_abilities() +
            self.get_three_abilities()
        )

    def __init__era__three__(self):
        self.mod_era(3)
        self.mod_avalible_abilities(
            self.get_three_abilities()
        )

# ~~~~~~~~~~~~~~~~~~~~~~~~~GETS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# I borke ip the helper classes into gets and mods. The gets just retrun value and the mods modfiy them. I usded the language of mod over the set and add becuase I think mod is more uniform. We know that if we want to change an attirbute we can call a mod function. Perhaps all these get and mod helper functions should be in a new document by themselves.

    def get_serial(self):
        return self.__attributes['serial']

    def get_stone(self):
        return self.__attributes['stone']

    def get_era(self):
        return self.__attributes['era']

    def get_health(self):
        return self.__attributes['health']

    def get_size(self):
        return self.__attributes['size']

    def get_movement_speed(self):
        return self.__attributes['movement_speed']

    def get_flight_movement_speed(self):
        return self.__attributes['flight_movement_speed']

    def get_arms(self):
        return self.__attributes['arms']

    def get_caste_rank(self):
        return self.__attributes['caste_rank']

    def get_diamond(self):
        return self.__attributes['diamond']

    def get_action_slots(self):
        return self.__attributes['action_slots']

    def get_PP(self):
        return self.__attributes['PP']

    def get_SPR(self):
        return self.__attributes['SPR']

    def get_homo(self):
        return self.__attributes['homo']

    def get_hetro(self):
        return self.__attributes['hetro']

    def get_CPR(self):
        return self.__attributes['CPR']

    def get_attacking(self):
        return self.__attributes['attacking']

    def get_blocking(self):
        return self.__attributes['blocking']

    def get_disarming(self):
        return self.__attributes['disarming']

    def get_onePR(self):
        return self.__attributes['onePR']

    def get_twoPR(self):
        return self.__attributes['twoPR']

    def get_threePR(self):
        return self.__attributes['threePR']

    def get_cert(self):
        return self.__attributes['certs']

    def get_one_equipment(self):
        return self.__attributes['one_equipment']

    def get_one_vehicle(self):
        return self.__attributes['one_vehicle']

    def get_one_crafting(self):
        return self.__attributes['one_crafting']

    def get_two_equipment(self):
        return self.__attributes['two_equipment']

    def get_two_vehicle(self):
        return self.__attributes['two_vehicle']

    def get_two_crafting(self):
        return self.__attributes['two_crafting']

    def get_three_equipment(self):
        return self.__attributes['three_equipment']

    def get_three_vehicle(self):
        return self.__attributes['three_vehicle']

    def get_three_crafting(self):
        return self.__attributes['three_crafting']

    def get_one_abilities(self):
        return self.__attributes['one_abilities']

    def get_two_abilities(self):
        return self.__attributes['two_abilities']

    def get_three_abilities(self):
        return self.__attributes['three_abilities']

    def get_avalible_abilities(self):
        return self.__attributes['avalible_abilities']

    def get_hardlight_weapon(self):
        return self.__attributes['hardlight_weapon']

# ~~~~~~~~~~~~~~~~~~~~~~~~~MODS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

    def mod_serial(self, serial_mod):
        self.__attributes['serial'] = serial_mod

    def mod_stone(self, stone_mod):
        self.__attributes['stone'] = stone_mod

    def mod_era(self, era_mod):
        self.__attributes['era'] += era_mod

    def mod_health(self, health_mod):
        self.__attributes['health'] += health_mod

    def mod_size(self, size_mod):
        self.__attributes['size'] = size_mod

    def mod_movement_speed(self, movement_speed_mod):
        self.__attributes['movement_speed'] += movement_speed_mod

    def mod_flight_movement_speed(self, flight_movement_speed_mod):
        self.__attributes['flight_movement_speed'] += flight_movement_speed_mod

    def mod_arms(self, arms_mod):
        self.__attributes['arms'] += arms_mod

    def mod_caste_rank(self, caste_rank_mod):
        self.__attributes['caste_rank'] += caste_rank_mod

    def mod_diamond(self, diamond_mod):
        self.__attributes['diamond'] = diamond_mod

    def mod_action_slots(self, action_slots_mod):
        self.__attributes['action_slots'] += action_slots_mod

    def mod_PP(self, PP_mod):
        self.__attributes['PP'] += PP_mod

    def mod_SPR(self, SPR_mod):
        self.__attributes['SPR'] += SPR_mod

    def mod_homo(self, homo_mod):
        self.__attributes['homo'] = homo_mod

    def mod_hetro(self, hetro_mod):
        self.__attributes['hetro'] = hetro_mod

    def mod_CPR(self, CPR_mod):
        self.__attributes['CPR'] += CPR_mod

    def mod_attacking(self, attacking_mod):
        self.__attributes['attacking'] = attacking_mod

    def mod_blocking(self, blocking_mod):
        self.__attributes['blocking'] = blocking_mod

    def mod_disarming(self, disarming_mod):
        self.__attributes['disarming'] = disarming_mod

    def mod_onePR(self, onePR_mod):
        self.__attributes['onePR'] += onePR_mod

    def mod_twoPR(self, twoPR_mod):
        self.__attributes['twoPR'] += twoPR_mod

    def mod_threePR(self, threePR_mod):
        self.__attributes['threePR'] += threePR_mod

    def mod_cert(self, cert_mod, add=True):
        if add:
            self.__attributes['certs'].append(
                cert_mod
            )
        else:
            self.__attributes['certs'].remove(
                cert_mod
            )

    def mod_one_equipment(self, one_equipment_mod):
        self.__attributes['one_equipment_mod'] = one_equipment_mod

    def mod_one_vehicle(self, one_vehicle_mod):
        self.__attributes['one_vehicle'] = one_vehicle_mod

    def mod_one_crafting(self, one_crafting_mod):
        self.__attributes['one_crafting'] = one_crafting_mod

    def mod_two_equipment(self, two_equipment_mod):
        self.__attributes['two_equipment_mod'] = two_equipment_mod

    def mod_two_vehicle(self, two_vehicle_mod):
        self.__attributes['two_vehicle'] = two_vehicle_mod

    def mod_two_crafting(self, two_crafting_mod):
        self.__attributes['two_crafting'] = two_crafting_mod

    def mod_three_equipment(self, three_equipment_mod):
        self.__attributes['three_equipment_mod'] = three_equipment_mod

    def mod_three_vehicle(self, three_vehicle_mod):
        self.__attributes['three_vehicle'] = three_vehicle_mod

    def mod_three_crafting(self, three_crafting_mod):
        self.__attributes['three_crafting'] = three_crafting_mod

    def mod_one_abilities(self, one_abilities_mod, add=True):
        if add:
            self.__attributes['one_abilities'].append(
                one_abilities_mod
            )
        else:
            self.__attributes['one_abilities'].remove(
                one_abilities_mod
            )

    def mod_two_abilities(self, two_abilities_mod, add=True):
        if add:
            self.__attributes['two_abilities'].append(
                two_abilities_mod
            )
        else:
            self.__attributes['two_abilities'].remove(
                two_abilities_mod
            )

    def mod_three_abilities(self, three_abilities_mod, add=True):
        if add:
            self.__attributes['three_abilities'].append(
                three_abilities_mod
            )
        else:
            self.__attributes['three_abilities'].remove(
                three_abilities_mod
            )

    def mod_avalible_abilities(self, avalible_abilities_mod, add=True):
        if add:
            self.__attributes['avalible_abilities'].append(
                avalible_abilities_mod
            )
        else:
            self.__attributes['avalible_abilities'].remove(
                avalible_abilities_mod
            )

    def mod_hardlight_weapon(self, hardlight_weapon_mod):
        self.__attributes['hardlight_weapon'] = hardlight_weapon_mod


# I commendtd these out to simplfy my experiemtns and I don't know if they are compatable with the set up I am proposing. At least in terms of the uniformaty going on with the gets and mods, I don't think these should be in here.
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
