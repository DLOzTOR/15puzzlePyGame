import pygame
import pygame.font
from Core.game import Game
from Entities import *
from Core.input import Input
import Core.physics as physics
import random


class Puzzle15(Game):
    def __init__(self, size_x, size_y):
        super().__init__(size_x, size_y)
        self.is_win = False
        self.font = pygame.font.Font(None, 24)
        self.win_font = pygame.font.Font(None, 48)
        self.background = 'wheat'
        self.colors = ['crimson', 'green2', 'royalblue1']
        self.field = []
        x_s = self.size_x // 4
        y_s = self.size_y // 4
        t = []
        self.set_tiles(t, x_s, y_s)
        self.shuffle(t, x_s, y_s)

    def set_tiles(self, t, x_s, y_s):
        color_counter = 0
        number_counter = 0
        for i in range(4):
            for j in range(4):
                if i == 3 and j == 3:
                    continue
                color_counter += 1
                number_counter += 1
                if color_counter > len(self.colors) - 1:
                    color_counter = 0
                t.append(Tile(pygame.Rect(x_s * j, y_s * i, x_s, y_s), number_counter, self.colors[color_counter]))
        t.append(None)

    def shuffle(self, t, x_s, y_s):
        random.shuffle(t)
        tv = 0
        for i in t:
            if tv % 4 == 0:
                self.field.append([])
            if i is not None:
                i.rect.y = tv//4 * y_s
                i.rect.x = tv % 4 * x_s
            self.field[tv//4].append(i)
            tv += 1

    def is_completed(self):
        counter = 0
        for i in self.field:
            for j in i:
                if j is None and counter != 15:
                    return False
                elif j is not None and j.number != counter + 1:
                    return False
                counter += 1
        return True

    def restart(self):
        t = []
        for i in self.field:
            for j in i:
                t.append(j)
        self.field = []
        self.shuffle(t, self.size_x // 4, self.size_y // 4)
        self.is_win = False

    def process_events(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.is_running = False
                case pygame.MOUSEBUTTONDOWN:
                    if not self.is_win and event.dict['button'] == 1:
                        Input.mouse_down_position = event.dict['pos']
                case pygame.MOUSEBUTTONUP:
                    if not self.is_win and event.dict['button'] == 1:
                        Input.is_mouse_click = True
                case pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.restart()

    def update(self):
        if Input.is_mouse_click:
            x = 0
            y = 0
            for row in self.field:
                x = 0
                for tile in row:
                    if tile is not None and physics.aabb_to_point(tile.rect.x, tile.rect.y, tile.rect.w, tile.rect.h, *Input.mouse_down_position):
                        pos = -1
                        for i in range(4):
                            for j in range(4):
                                if self.field[i][j] is None:
                                    pos = [i,j]
                                    break
                        if abs(pos[0] - y) + abs(pos[1] - x) == 1:
                            self.field[y][x].rect.x = pos[1] * self.field[y][x].rect.w
                            self.field[y][x].rect.y = pos[0] * self.field[y][x].rect.h
                            self.field[y][x], self.field[pos[0]][pos[1]] = self.field[pos[0]][pos[1]], self.field[y][x]
                            # self.print_field()
                            if self.is_completed():
                                self.is_win = True
                        break
                    x += 1
                y += 1

            Input.is_mouse_click = False

    def draw_tiles(self):
        for row in self.field:
            for tile in row:
                if tile is None:
                    continue
                pygame.draw.rect(self.screen, tile.color, tile.rect, border_radius=10)
                pygame.draw.rect(self.screen, self.background, tile.rect, width=2, border_radius=10)
                number_text = self.font.render(f'{tile.number}', True, 'black')
                self.screen.blit(number_text, (tile.rect.x + tile.rect.w // 2 - number_text.get_width() // 2,
                                               tile.rect.y + tile.rect.h // 2 - number_text.get_height() // 2))

    def draw_win_screen(self):
        pygame.draw.rect(self.screen, 'gold', pygame.Rect(self.size_x // 4, self.size_y // 3, self.size_x // 2, self.size_y // 3), border_radius=10)
        number_text = self.win_font.render(f'You win!', True, 'black')
        self.screen.blit(number_text, (self.size_x // 2 - number_text.get_width() // 2, self.size_y // 2 - number_text.get_height()))
        number_text = self.font.render(f'Press R to restart!', True, 'black')
        self.screen.blit(number_text, (self.size_x // 2 - number_text.get_width() // 2, self.size_y // 2 + number_text.get_height()))

    def render(self):
        self.screen.fill(self.background)
        self.draw_tiles()
        if self.is_win:
            self.draw_win_screen()

    def print_field(self):
        for i in self.field:
            for j in i:
                print(' 0' if j is None else j.number if j.number >= 10 else f' {j.number}', end=' ')
            print()