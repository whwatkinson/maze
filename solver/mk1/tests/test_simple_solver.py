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
