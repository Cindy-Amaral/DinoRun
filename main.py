import pygame
import sys
from utils import Settings, GameStats
from dino import Dino, Heart
from scene import RollingBackground, Obstacle1
import numpy as np
from time import sleep


class DinoRun:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.mixer.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        self.bg_color = self.settings.bg_color
        pygame.display.set_caption('Dino Run')
        self.stats = GameStats(self)

        music = pygame.mixer.music.load('audio/game-music-loop-3-144252.mp3')
        pygame.mixer.music.play(-1)

        self.jump_sound = pygame.mixer.Sound('audio/cartoon-jump-6462.mp3')
        self.end_sound = pygame.mixer.Sound('audio/spongebob-fail.mp3')

        self.dino = Dino(self)
        self.hearts = [Heart(self, 1050, 550), Heart(self, 1090, 550), Heart(self, 1130, 550)]
        self.rolling_background = RollingBackground(self)
        #self.obstacles = []
        self.obstacles = pygame.sprite.Group()

        self.generate_obstacles(num_obstacles = 5, start_x = 900, min_distance = 1000, max_distance = 1300)
        self.collision_detected = False
    def generate_obstacles(self, num_obstacles, start_x, min_distance, max_distance):
        #generate random x positions for obstacles
        distances = np.cumsum(np.random.randint(min_distance, max_distance, size=num_obstacles - 1))
        x_positions = np.cumsum(np.concatenate(([start_x], distances)))

        for x in x_positions:
            obstacle = Obstacle1(self)
            obstacle.rect.x = x
            self.obstacles.add(obstacle)

    def run_game(self):
        target_fps = 240
        while True:
            dt = self.clock.tick(target_fps) / 1000 #amount of seconds between each loop
            self._check_events()
            self.rolling_background.update()
            self.dino.update(dt)

            for obstacle in self.obstacles:
                obstacle.update()

            #look for collisions
            #if pygame.sprite.spritecollideany(self.dino, self.obstacles):
                #self._dino_hit()
            if self._check_collision():
                self._dino_hit()

            self.clock.tick(target_fps)
            self._update_screen()

    def _check_events(self):
        """respond to key presses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    #dino jumps
                    self.dino.rect.y -= 80
                    pygame.mixer.Sound.play(self.jump_sound)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    #dino lands
                    self.dino.rect.y += 80

    def _update_screen(self):
        """update images on the screen and flip to the new screen"""
        self.screen.fill(self.bg_color)
        self.rolling_background.blitme()
        self.dino.blitme()
        self.obstacles.draw(self.screen)
        # for obstacle in self.obstacles:
        #     obstacle.blitme()
        for heart in self.hearts:
            heart.blitme()
        pygame.display.flip()

    def _dino_hit(self):
        self.stats.hearts_left -= 1
        if self.stats.hearts_left >= 1:
            self.hearts[self.stats.hearts_left].rect.y = 700
            self._update_screen()
            sleep(0.5)
        else:
            self.hearts[self.stats.hearts_left].rect.y = 700
            self._update_screen()
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(self.end_sound)
            sleep(3)

    def _check_collision(self):
        """Check for collisions between the dino and obstacles"""
        dino_hitbox = self.dino.rect
        for obstacle in self.obstacles:
            if dino_hitbox.colliderect(obstacle.hitbox):
                if not self.collision_detected:
                    self.collision_detected = True
                    return True
            else:
                self.collision_detected = False
        return False




if __name__ == "__main__":
    dr = DinoRun()
    dr.run_game()