from solver.mk1 import SimpleBrain, SimpleOrgans


so = SimpleOrgans()

class TestSimpleBrain:


    def test_get_new_brain(self):

        test_cases = [
            {
                'brain': {
                    'sight': {
                        'up': 'S',
                        'down': 'W',
                        'left': ' ',
                        'right': '|',
                        'z_minus': None,
                        'z_plus': None
                    },
                    'last_known_position': so.sight_clean
                    'memory': {
                        'steps': 2
                    }
                }
            }
        ]

        for case in test_cases:

            sb = SimpleBrain(brain=case['brain'])

            assert type(sb) is SimpleBrain
