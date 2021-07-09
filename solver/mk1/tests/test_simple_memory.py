from collections import namedtuple


from solver.mk1.simple_memory import SimpleMemory


class TestSimpleMemory:

    def test_new_brain(self):

        test_memory = SimpleMemory()

        assert test_memory.steps == 0

    def test_inherited_memory(self):

        TestCase = namedtuple('TestCase', ['steps', 'exp_steps'])

        test_cases = [
            TestCase(1, 1),
            TestCase(77, 77)
        ]

        for case in test_cases:

            test_memory = SimpleMemory(steps=case.steps)

            assert test_memory.steps == case.exp_steps
