from solver.mk1.simple_organs import SimpleOrgans


class TestSimpleOrgans:

    def test_new_sight(self):

        so = SimpleOrgans()

        # Useless but necessary
        for attribute in so.sight_clean:

            assert attribute is None
