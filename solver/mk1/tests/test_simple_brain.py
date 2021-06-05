from solver.mk1.simple_brain import SimpleBrain


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
                    'last_known_position': {
                        'up': None,
                        'down': None,
                        'left': None,
                        'right': None,
                        'z_minus': None,
                        'z_plus': None
                    },
                    'memory': {
                        'steps': 2
                    }
                }
            }
        ]

        for case in test_cases:

            sb = SimpleBrain(brain=case['brain'])

            assert type(sb) is SimpleBrain
