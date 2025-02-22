import pygame
import pygame.font
from Core.game import Game
from Entities import *
from Core.input import Input
import Core.physics as physics


class Puzzle15(Game):
    def __init__(self, size_x, size_y):
        super().__init__(size_x, size_y)
        self.font = pygame.font.Font(None, 36)
        self.background = 'wheat'
        self.colors = ['crimson', 'green2', 'royalblue1']
        self.field = []
        x_s = self.size_x / 4
        y_s = self.size_y / 4
        color_counter = 0
        number_counter = 0
        for i in range(4):
            self.field.append([])
            for j in range(4):
                if i == 3 and j == 3:
                    continue
                color_counter += 1
                number_counter += 1
                if color_counter > len(self.colors) - 1:
                    color_counter = 0
                self.field[i].append(Tile(pygame.Rect(x_s * j, y_s * i, x_s, y_s), number_counter, self.colors[color_counter]))

    def process_events(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.is_running = False
                case pygame.MOUSEBUTTONDOWN:
                    if event.dict['button'] == 1:
                        Input.mouse_down_position = event.dict['pos']
                case pygame.MOUSEBUTTONUP:
                    if event.dict['button'] == 1:
                        Input.is_mouse_click = True

    def update(self):
        if Input.is_mouse_click:
            for row in self.field:
                for tile in row:
                    if physics.aabb_to_point(tile.rect.x, tile.rect.y, tile.rect.w, tile.rect.h, *Input.mouse_down_position):
                        tile.is_active = True
                    else:
                        tile.is_active = False
            Input.is_mouse_click = False

    def render(self):
        self.screen.fill(self.background)
        for row in self.field:
            for tile in row:
                pygame.draw.rect(self.screen, tile.color, tile.rect, border_radius=10)
                pygame.draw.rect(self.screen,self.background, tile.rect, width=2, border_radius=10)
                number_text = self.font.render(str(tile.number), True, 'black' if not tile.is_active else 'gold')
                self.screen.blit(number_text, (tile.rect.x + tile.rect.w // 2 - number_text.get_width() // 2, tile.rect.y + tile.rect.h // 2 - number_text.get_height() // 2))
