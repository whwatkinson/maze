from solver.mk1.simple_brain import SimpleBrain, SimpleOrgans


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
                    'last_known_position': so.sight_clean,
                    'memory': {
                        'steps': 2
                    }
                }
            }
        ]

        for case in test_cases:

            sb = SimpleBrain(brain=case['brain'])

            assert type(sb) is SimpleBrain

    def test_brain_step_count(self):
        test_cases = [
            {
                'steps': 0,
                'movement': 1,
                'total_steps': 1
            }
        ]
        sb = SimpleBrain()
        for case in test_cases:

            sb.update_step_count()

            assert sb.get_step_count() == case['total_steps']
