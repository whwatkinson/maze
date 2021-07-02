from collections import namedtuple

Sight = namedtuple('Sight', [
    'up',
    'down',
    'left',
    'right',
    'z_minus',
    'z_plus'
])


class SimpleOrgans:
    sight_clean = Sight(
        up=None,
        down=None,
        left=None,
        right=None,
        z_minus=None,
        z_plus=None
    )
