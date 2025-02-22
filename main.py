import pygame
from game import Game


def init(self):
    pass


def process_events(self):
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                self.is_running = False


def update(self):
    pass


def render(self):
    self.screen.fill("purple")


game = Game(200, 200, init, process_events, update, render)


def main():
    game.run()


if __name__ == '__main__':
    main()