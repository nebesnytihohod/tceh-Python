class Player(object):
    """docstring for Player"""

    def __init__(self, name):
        self.name = name


class Ship(object):
    """docstring for Ship"""

    def __init__(self, size, coord, direction):
        self.size = size
        self.coord = coord
        self.direction = direction


class GameField(object):
    """docstring for GameField"""

    def __init__(self, ):
        self.field = [[0,0,0], [], [], [], [], [], [], [], [], []]


class Hit(object):
    def __init__(self):
        pass

    coordHit
    resultHit

game = GameField()
game.field[0] = 1