from Core.entity import Entity


class Tile(Entity):
    def __init__(self, rect, number, color):
        super().__init__()
        self.rect = rect
        self.number = number
        self.color = color
        self.is_active = False
