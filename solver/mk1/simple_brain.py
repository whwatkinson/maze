from solver.mk1 import SimpleOrgans

so = SimpleOrgans()


class SimpleBrain:

    def __init__(self, brain: dict = None):

        if not brain:
            self.brain = self.get_brain(brain)

    def get_brain(self, brain):
        """What consitutes a brain anway? Currently thinking a known state"""

        if type(brain) is self:
            return brain

        else:
            new_brain = {
                'sight': so.sight_clean,
                'last_known_position': so.sight_clean,
                'memory': {
                    'steps': 0
                }
            }
        return new_brain
