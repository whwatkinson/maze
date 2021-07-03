from pytest import mark
from collections import namedtuple

from solver import SolverMeta
from solver.mk1 import SimpleSolver, Sight
from solver.mk1.tests.sample_mazes import maze0


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
            sm = SolverMeta()

            assert ss.name in sm.solver_names
            # assert type(ss.brain) is dict
            assert type(ss.path_taken) is list

    def test_brain_position(self):
        pass

    def test_brain_step_count(self):
        test_cases = [
            {
                'steps': 0,
                'movement': 2,
                'total_steps': 2
            }
        ]
        for case in test_cases:

            ss = SimpleSolver()

            for steps in range(case['total_steps'])

                ss.update_step_count()

                assert ss.get_step_count() == case['total_steps']



    @mark.xfail
    def test_update_position(self):

        test_cases = [
            {
                'old_position': Sight(
                    up='W',
                    down='W',
                    left=' ',
                    right='|',
                    z_minus=None,
                    z_plus=None
                ),
                'new_position': Sight(
                    up=' ',
                    down=' ',
                    left=' ',
                    right=' ',
                    z_minus=None,
                    z_plus=None
                )
            }
        ]

        for case in test_cases:
            ss = SimpleSolver()
            ss.brain.memory['sight'] = case['old_position']
            ss.update_location(**case['new_position']._asdict())

            # Check old sight is LKP
            assert (
                    ss.brain.last_known_position
                    == case['old_position']
            )

            # Check new sight in NP
            assert ss.get_current_postion() == case['new_position']

    def test_update_sight(self):

        TestCase = namedtuple('TestCase', ['maze', 'position', 'expected'])

        test_cases = [
            # Top Left
            TestCase(maze0, (0, 0), Sight(
                up='A',
                down='|',
                left='A',
                right='_',
                z_minus=None,
                z_plus=None
            )),
            # Middle
            TestCase(maze0, (12, 17), Sight(
                up='W',
                down=' ',
                left='W',
                right='W',
                z_minus=None,
                z_plus=None
            )),
            # Bottom right
            TestCase(maze0, (24, 24), Sight(
                up='|',
                down='A',
                left='‾',
                right='A',
                z_minus=None,
                z_plus=None
            ))

        ]

        for case in test_cases:
            ss = SimpleSolver()
            sight = ss.update_sight(case.maze, case.position)
            for test, expected in zip(case.expected, sight):
                assert test == expected
