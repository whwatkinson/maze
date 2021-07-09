from collections import namedtuple


from solver.mk1.simple_brain import SimpleBrain, SimpleOrgans
from solver.mk1.simple_solver import SimpleSolver
from solver.mk1.simple_memory import SimpleMemory
from solver.mk1 import Sight

so = SimpleOrgans()
sm = SimpleMemory()


class TestSimpleBrain:

    def test_new_brain(self):

        test_brain = SimpleBrain()

        for attribute in test_brain.sight:
            assert attribute is None

        for attribute in test_brain.last_known_position:
            assert attribute is None

    def test_inherited_brain(self):

        TestCase = namedtuple('TestCase', [
            "sight", "last_known_position", "memory"
        ])

        test_cases = [
            TestCase(
                sight=Sight(
                    up='S',
                    down='W',
                    left=' ',
                    right='|',
                    z_minus=None,
                    z_plus=None
                ),
                last_known_position=Sight(
                    up=' ',
                    down='W',
                    left=' ',
                    right='|',
                    z_minus=None,
                    z_plus=None
                ),
                memory=SimpleMemory(steps=55))
        ]

        for case in test_cases:

            test_brain = SimpleBrain(**case._asdict())
            ss = SimpleSolver(brain=test_brain)
            assert type(ss.brain) is SimpleBrain
            assert ss.brain.memory.steps == case.memory.steps

            for expected, test in zip(case.sight, ss.brain.sight):
                assert expected == test

            for expected, test in zip(case.last_known_position, ss.brain.last_known_position):
                assert expected == test
