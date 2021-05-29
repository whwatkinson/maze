from pytest import raises

from mazes.mk1 import SimpleMaze


class TestMaze:

    test_cases = [
        {
            'height': 5,
            'width': 5

        },
        {

            'height': 44,
            'width': 4
        },
    ]

    def test_start(self):

        for case in self.test_cases:

            s = SimpleMaze(**case)
            maze = s.maze
            width = case['width']
            valid_pos = maze[0][1:width-1]

            start = 's'

            assert start in valid_pos

    def test_finish(self):

        for case in self.test_cases:

            s = SimpleMaze(**case)
            maze = s.maze
            width = case['width']
            height = case['height']
            valid_pos = maze[height-1][1:width-1]

            finish = 'f'

            assert finish in valid_pos

    def test_height_width(self):

        with raises(ValueError):
            SimpleMaze(2, 2)

        for case in self.test_cases:
            s = SimpleMaze(**case)
            maze = s.maze

            assert len(maze) == case['height']

            for row in maze:
                assert len(row) == case['width']

    def test_side(self):

        for case in self.test_cases:

            s = SimpleMaze(**case)
            maze = s.maze

            height = case['height']
            width = case['width']

            void = {0, height-1}

            for idx, row in enumerate(maze):

                if idx not in void:

                    assert row[0] == row[width-1] == '|'
