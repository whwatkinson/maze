


from mazes.mk1.simple_maze import SimpleMaze


class TestMaze:


    test_cases = [
        {
            'simple_maze':
                [
                    ['_', '_', 's', '_', '_'],
                    ['|', 'x', 'x', 'x', '|'],
                    ['|', 'x', 'x', 'x', '|'],
                    ['|', 'x', 'x', 'x', '|'],
                    ['‾', '‾', 'f', '‾', '‾']
        }
    ]


    def test_start(self):