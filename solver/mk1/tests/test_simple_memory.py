from solver.mk1.simple_memory import SimpleMemory


class TestSimpleMemory:

    def test_new_brain(self):

        test_memory = SimpleMemory()

        assert test_memory.steps == 0
