import pygame


class Game:
    def __init__(self, size_x, size_y):
        pygame.init()
        self.size_x = size_x
        self.size_y = size_y
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.screen = pygame.display.set_mode((size_x, size_y))

    def start(self):
        pass

    def process_events(self):
        pass

    def update(self):
        pass

    def render(self):
        pass

    def run(self):
        while self.is_running:
            self.process_events()
            self.update()
            self.render()
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()
