from mazes.mk1.simple_maze import SimpleMaze


class TestMaze:

    test_cases = [
        {'height': 5}
    ]

    def test_start(self):

        for case in self.test_cases:

            s = SimpleMaze(height=case['height'])
            maze = s.maze

            start = 's'

            assert maze[0][2] == start
