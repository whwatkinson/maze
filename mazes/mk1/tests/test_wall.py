from typing import List, Tuple

from mazes.mk1 import SimpleWall


class TestWall:

    test_case = [
        {
            'height': 25,
            'width': 25,
            'number_of_walls': 25
        }
    ]

    def test_get_wall_coords(self):

        for case in self.test_case:
            w = SimpleWall(**case)

            wall_meta = w.walls_meta

            for wall in wall_meta:

                assert type(wall['v']) is bool
                assert type(wall['length']) is int
                assert type(wall['x']) is int
                assert type(wall['y']) is int
                assert type(wall['wall_coords']) is list

            assert len(wall_meta) == case['number_of_walls']

