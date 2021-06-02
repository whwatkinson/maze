from typing import List, Tuple
from solver.mk1 import SimpleSolver, solver_names


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
