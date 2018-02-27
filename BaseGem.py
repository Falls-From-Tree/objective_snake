class BaseGem():
    def __init__(self):
        self.__attributes = dict(
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

    def set_serial(self, new_serial):
        self.__attributes['serial'] = new_serial

    def set_stone(self, new_stone):
        self.__attributes['stone'] = new_stone

    def set_era(self, new_era):
        self.__attributes['era'] = new_era

    def add_health(self, health_mod):
        self.__attributes['health'] += health_mod

    # size should probably always be powers of 2
    # this also modifies movement_speed
    def set_size(self, new_size):
        self.__attributes['size'] = new_size
        self.__attributes['movementspeed'] = new_size * 8

    def add_flight_movement_speed(self, flight_movement_speed_mod):
        self.__attributes['flight_movement_speed'] += flight_movement_speed_mod

    def add_arms(self, arms_mod):
        self.__attributes['arms'] += arms_mod

    def add_caste_rank(self, caste_rank_mod):
        self.__attributes['caste_rank'] += caste_rank_mod

    def add_action_slots(self, action_slots_mod):
        self.__attributes['action_slots'] += action_slots_mod

    def add_PP(self, PP_mod):
        self.__attributes['PP'] += PP_mod

    def add_SPR(self, SPR_mod):
        self.__attributes['SPR'] += SPR_mod

    def set_homo(self, new_homo):
        self.__attributes['homo'] = new_homo

    def set_hetro(self, new_hetro):
        self.__attributes['hetro'] = new_hetro

    def add_CPR(self, CPR_mod):
        self.__attributes['CPR'] += CPR_mod

    def set_attacking(self, new_attacking):
        self.__attributes['attacking'] = new_attacking

    def set_blocking(self, new_blocking):
        self.__attributes['blocking'] = new_blocking

    def set_disarming(self, new_disarming):
        self.__attributes['disarming'] = new_disarming

    def add_onePR(self, onePR_mod):
        self.__attributes['onePR'] += onePR_mod

    def add_twoPR(self, twoPR_mod):
        self.__attributes['twoPR'] += twoPR_mod

    def add_threePR(self, threePR_mod):
        self.__attributes['threePR'] += threePR_mod

    def add_cert(self, new_cert):
        self.__attributes['certs'].append(new_cert)
