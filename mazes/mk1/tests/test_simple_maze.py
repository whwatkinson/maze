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

            height = case['height']
            width = case['width']

            void = {0, height-1}

            for idx, row in enumerate(maze):

                # Test side of maze
                if idx not in void:
                    assert row[0] == row[width-1] == s.markers['side']

                # Test top of the maze
                if idx == 0:
                    # Test start position
                    if row == x_s and idx == y_s:
                        assert row[y_s] == s.markers['start']
                    # todo check rest DHH fix

                # Test the bottom of the maze
                if idx == height - 1:
                    # Test finish position
                    if row == x_f and idx == y_f:
                        assert row[y_s] == s.markers['finish']
                    # todo check rest DHH fix
