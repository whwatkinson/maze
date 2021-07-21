from collections import namedtuple
from random import randint


from walls.mk1 import SimpleWall


class TestSimpleWall:

    test_case = [
        {
            'height': 5,
            'width': 5,
            'number_of_walls': 2,
            'max_wall_length': 1
        },
        {
            'height': 7,
            'width': 66,
            'number_of_walls': 25,
            'max_wall_length': 12
        },
        {
            'height': 45,
            'width': 23,
            'number_of_walls': 77
        },
        {
            'height': 99,
            'width': 99,
            'number_of_walls': 0,
            'max_wall_length': 12
        }
    ]

    def test_get_wall_coords(self):

        for case in self.test_case:
            w = SimpleWall(**case)

            wall_meta = w.walls_meta

            assert len(wall_meta) == case['number_of_walls']

    def test_get_wall_meta_return(self):

        for case in self.test_case:
            w = SimpleWall(**case)

            wall_meta = w.walls_meta

            for wall in wall_meta:

                assert type(wall.vertical) is bool
                assert type(wall.wall_length) is int
                assert type(wall.x) is int
                assert type(wall.y) is int
                assert type(wall.wall_coords) is list

    def test_wall_length(self):
        pass

    def test_narnia(self):

        TestCase = namedtuple('TestCase', ['x', 'y', 'expected_result'])

        test_cases = [
            TestCase(1, 7, True),
            TestCase(5, 7, False)
        ]

        # Known False results
        for case in test_cases:

            # Random coords on random walls
            sw = SimpleWall(10, 10, 10, 5)

            test = sw.narnia(case.x, case.y)
            assert test is case.expected_result
