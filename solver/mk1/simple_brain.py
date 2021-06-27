from solver.mk1.simple_organs import SimpleOrgans

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

    def update_step_count(self) -> bool:
        """Updates the step count"""

        # Get bain dict
        steps = self.brain['memory']

        # GOALS
        if steps['steps'] > 10000:
            print("STEP GOAL REACHED")

        # Update steps
        steps['steps'] += 1

        return True

    def get_step_count(self):
        """Returns the current step count"""
        return self.brain['memory']['steps']
