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
            assert type(ss.brain) is dict
            assert type(ss.path_taken) is list


    def test_brain_position(self):
        pass

    def test_brain_step_count(self):
        pass