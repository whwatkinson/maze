from solver.mk1.simple_brain import SimpleBrain, SimpleOrgans
from solver.mk1.simple_solver import SimpleSolver
from solver.mk1 import Sight

so = SimpleOrgans()


class TestSimpleBrain:

    def test_get_new_brain(self):

        test_cases = [
            {
                'sight': Sight(
                    up='S',
                    down='W',
                    left=' ',
                    right='|',
                    z_minus=None,
                    z_plus=None
                ),
                'last_known_position': so.sight_clean,
                'memory': {
                    'steps': 2
                    }
                }

        ]

        for case in test_cases:

            test_brain = SimpleBrain(**case)

            ss = SimpleSolver(brain=test_brain)
            assert type(ss.brain) is SimpleBrain
