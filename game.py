import pygame


class Game:
    def __init__(self, size_x, size_y, init, process_events, update, render):
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.screen = pygame.display.set_mode((size_x, size_y))
        self.init = init
        self.update = update
        self.render = render
        self.process_events = process_events

    def run(self):
        self.init(self)
        while self.is_running:
            self.process_events(self)
            self.update(self)
            self.render(self)
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()
