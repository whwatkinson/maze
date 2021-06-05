
new_sight = {
    'up': None,
    'down': None,
    'left': None,
    'right': None,
    'z_minus': None,
    'z_plus': None
}


class SimpleBrain:

    def __init__(self, brain: dict = None):

        if not brain:
            self.brain = self.get_brain(brain)

    def get_brain(self, brain):

        if type(brain) is self:
            return brain

        else:
            # What consitutes a brain anway? Currently thinking a known state
            new_brain = {
                'sight': new_sight,
                'last_known_position': new_sight,
                'memory': {
                    'steps': 0
                }
            }
        return new_brain
