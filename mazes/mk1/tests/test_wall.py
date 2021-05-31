from mazes.mk1 import SimpleWall

from mazes.mk1.tests.test_maze import TestMaze

class TestWall:

    test_case = [
        {
            'create_params':
                {
                    'height': 25,
                    'width': 25,
                    'number_of_walls': 25
                },
            'v': True,
            'length': 5,
            'x': 1,
            'y': 3
        }
    ]

    def test_get_wall_coords(self):

        for case in self.test_case:
            v = case['v']
            length = case['length']
            x = case['x']
            y = case['y']

            w = SimpleWall(**case['create_params'])

            wall_coords = w.get_wall_coords(v=v, length=length, x=x, y=y)

            assert len(wall_coords) == case['length']

