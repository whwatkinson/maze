from solver.mk1.simple_organs import SimpleOrgans
from solver.mk1.simple_memory import SimpleMemory

so = SimpleOrgans()
sight_clean = so.sight_clean


class SimpleBrain:

    def __init__(
            self,
            sight: sight_clean = None,
            last_known_position: sight_clean = None,
            memory: SimpleMemory = None

    ):
        """
        What consitutes a brain anway? Currently thinking a known state
        :param sight:
        :param last_known_position:
        :param memory:
        :return :
        """

        self.sight = self.get_new_vision(sight)
        self.last_known_position = self.get_new_vision(last_known_position)
        self.memory = self.get_new_memory(memory)

    @staticmethod
    def get_new_vision(attribute):
        if not attribute:
            return sight_clean
        else:
            return attribute

    @staticmethod
    def get_new_memory(memory):
        if not memory:
            # Dicts are mutable afterall
            return SimpleMemory()
        else:
            return memory

    def __repr__(self):
        return f"|SIMPLE_BRAIN| steps_taken {self.memory.steps}"
