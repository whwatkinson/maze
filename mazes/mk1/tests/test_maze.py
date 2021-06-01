from pytest import raises

from mazes.mk1 import SimpleMaze


class TestMaze:

    test_cases = [
        {
            'height': 5,
            'width': 5,
            'number_of_walls': 2
        },
        {
            'height': 44,
            'width': 4,
            'number_of_walls': 3
        },
        {
            'height': 3,
            'width': 3,
            'number_of_walls': 1
        },
        {
            'height': 99,
            'width': 99,
            'number_of_walls': 0
        },
        {
            'height': 500,
            'width': 250,
            'number_of_walls': 200
        }
    ]

    def test_start(self):

        for case in self.test_cases:

            s = SimpleMaze(**case)
            maze = s.blank_maze
            s.display_maze()
            height = case['height']
            width = case['width']

            valid_pos_start = maze[0][1:width-1]
            valid_pos_finish = maze[height-1][1:width-1]
            finish = 'f'
            start = 's'

            assert start in valid_pos_start
            assert finish in valid_pos_finish

    def test_height_width(self):

        with raises(ValueError) as exec_info:
            SimpleMaze(2, 2)
        assert exec_info.type is ValueError

        for case in self.test_cases:
            s = SimpleMaze(**case)
            maze = s.blank_maze

            assert len(maze) == case['height']

            for row in maze:
                assert len(row) == case['width']

    def test_side(self):

        for case in self.test_cases:

            s = SimpleMaze(**case)
            maze = s.blank_maze

            height = case['height']
            width = case['width']

            void = {0, height-1}

            for idx, row in enumerate(maze):

                if idx not in void:

                    assert row[0] == row[width-1] == '|'
