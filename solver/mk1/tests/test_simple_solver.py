from solver import solver_names
from solver.mk1 import SimpleSolver


class TestSimpleSolver:

    test_cases = [
        {
            'brain': None,
            'path_taken': None
        }
    ]

    def test_get_solver(self):

        for case in self.test_cases:

            ss = SimpleSolver(**case)

            assert ss.name in solver_names
            # assert type(ss.brain) is dict
            assert type(ss.path_taken) is list

    def test_brain_position(self):
        pass

    def test_brain_step_count(self):
        test_cases = [
            {
                'steps': 0,
                'movement': 1,
                'total_steps': 1
            }
        ]
        ss = SimpleSolver()
        for case in test_cases:

            ss.update_step_count()

            assert ss.get_step_count() == case['total_steps']

    def test_update_position(self):

        test_cases = [
            {
                'old_position': {
                    'up': 'W',
                    'down': 'W',
                    'left': ' ',
                    'right': '|',
                    'z_minus': None,
                    'z_plus': None
                },
                'new_position': {
                    'up': ' ',
                    'down': ' ',
                    'left': ' ',
                    'right': ' ',
                    'z_minus': None,
                    'z_plus': None
                }
            }
        ]

        for case in test_cases:
            ss = SimpleSolver()
            ss.brain.brain['sight'] = case['old_position']
            ss.update_location(**case['new_position'])

            # Check old sight is LKP
            assert (
                    ss.brain.brain['last_known_position']
                    == case['old_position']
            )

            # Check new sight in NP
            assert ss.get_current_postion() == case['new_position']
