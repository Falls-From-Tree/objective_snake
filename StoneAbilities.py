# I think this is a better way to handle abilites, though maybe not the best. I think obejcts are the way to go along with gems, arms, and hardlight weapons, and hardlight weapon abilites

class StoneAbility():
    def __init__(self):
        self.rank = 0

    def shapeshifting(self, rank_up=False):
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
            return 'Shapeshifting - rank:{}'.format(self.rank)

    def bubbling(self, rank_up=False):
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
            return 'Bubbling - rank:{}'.format(self.rank)

    def shocking(self, rank_up=False):
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
            return 'Shocking - rank:{}'.format(self.rank)

    def advanced_form_regeneration(self, rank_up=False):
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
            return 'Advanced Form Regeneration - rank:{}'.format(self.rank)

    def intent_telethesia(self, rank_up=False):
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
            return 'Intent Telethesia - rank:{}'.format(self.rank)
