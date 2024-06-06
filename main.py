import pygame
import sys
from utils import Settings
from dino import Dino, Heart
from scene import RollingBackground, Obstacle1
import numpy as np


class DinoRun:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.mixer.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        self.bg_color = self.settings.bg_color
        pygame.display.set_caption('Dino Run')

        music = pygame.mixer.music.load('audio/skibidi-toilet.mp3')
        pygame.mixer.music.play(-1)

        self.jump_sound = pygame.mixer.Sound('audio/perfect-fart.mp3')

        self.dino = Dino(self)
        self.hearts = [Heart(self, 1050, 550), Heart(self, 1090, 550), Heart(self, 1130, 550)]
        self.rolling_background = RollingBackground(self)
        self.obstacles = []

        self.generate_obstacles(num_obstacles = 5, start_x = 900, min_distance = 1000, max_distance = 1300)

    def generate_obstacles(self, num_obstacles, start_x, min_distance, max_distance):
        #generate random x positions for obstacles
        distances = np.cumsum(np.random.randint(min_distance, max_distance, size=num_obstacles - 1))
        x_positions = np.cumsum(np.concatenate(([start_x], distances)))

        for x in x_positions:
            obstacle = Obstacle1(self)
            obstacle.rect.x = x
            self.obstacles.append(obstacle)

    def run_game(self):
        target_fps = 240
        while True:
            dt = self.clock.tick(target_fps) / 1000 #amount of seconds between each loop
            self._check_events()
            self._update_screen()
            self.rolling_background.update()
            self.dino.update(dt)

            for obstacle in self.obstacles:
                obstacle.update()

            self.clock.tick(target_fps)

    def _check_events(self):
        """respond to key presses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    #dino jumps
                    self.dino.rect.y -= 65
                    pygame.mixer.Sound.play(self.jump_sound)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    #dino lands
                    self.dino.rect.y += 65

    def _update_screen(self):
        """update images on the screen and flip to the new screen"""
        self.screen.fill(self.bg_color)
        self.rolling_background.blitme()
        self.dino.blitme()
        for obstacle in self.obstacles:
            obstacle.blitme()
        for heart in self.hearts:
            heart.blitme()
        pygame.display.flip()



if __name__ == "__main__":
    dr = DinoRun()
    dr.run_game()