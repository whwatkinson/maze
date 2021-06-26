from typing import List, Dict
from random import randint

from pytest import raises

from mazes.mk1 import SimpleMaze


class TestSimpleMaze:

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

    @staticmethod
    def get_test_cases(number: int) -> List[Dict[str, int]]:

        test_cases = [
            {
                'height': randint(0, 250),
                'width': randint(0, 250),
                'number_of_walls': randint(0, 250)
            }
            for _ in range(number)]

        return test_cases

    def test_start(self):

        for case in self.test_cases:

            s = SimpleMaze(**case)
            markers = s.markers
            maze = s.simple_maze
            height = case['height']
            width = case['width']

            valid_pos_start = maze[0][1:width-1]
            valid_pos_finish = maze[height-1][1:width-1]

            assert markers['start'] in valid_pos_start
            assert markers['finish'] in valid_pos_finish

    def test_height_width(self):

        with raises(ValueError) as exec_info:
            SimpleMaze(2, 2)
        assert exec_info.type is ValueError

        for case in self.test_cases:
            s = SimpleMaze(**case)
            maze = s.simple_maze

            # Test height of maze
            assert len(maze) == case['height']

            # Test width of maze
            for row in maze:
                assert len(row) == case['width']

    def test_markers(self):

        for case in self.test_cases:

            s = SimpleMaze(**case)
            maze = s.simple_maze

            x_s, y_s = s.coords_start
            x_f, y_f = s.coords_start

            height = case['height'] - 1
            width = case['width'] - 1

            void = {0, height}

            for idx, row in enumerate(maze):

                # Test side of maze
                if idx not in void:
                    assert row[0] == row[width] == s.markers['side']

                # Test top of the maze
                if idx == 0:
                    for top in range(width):
                        # Test start position
                        if top == y_s:
                            assert row[top] == s.markers['start']
                        else:
                            # Test the other positions

                            assert row[top] == s.markers['top']

                # Test the bottom of the maze
                if idx == height:

                    for bottom in range(width):
                        # Test finish position
                        if bottom == y_f:

                            assert row[bottom] == s.markers['finish']
                            # Test the other positions
                        else:

                            assert row[bottom] == s.markers['bottom']
