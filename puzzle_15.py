import pygame
from game import Game


class Puzzle15(Game):
    def init(self):
        self.background = 'white'
        self.colors = ['red', 'green', 'blue']

    def process_events(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.is_running = False

    def update(self):
        pass

    def render(self):
        self.screen.fill(self.background)
        x_s = self.size_x / 4
        y_s = self.size_y / 4
        counter = 0
        for i in range(4):
            for j in range(4):
                counter += 1
                if counter > len(self.colors) - 1:
                    counter = 0
                pygame.draw.rect(self.screen, self.colors[counter], pygame.Rect(x_s * i, y_s * j, x_s, y_s))
