import pygame

class Dino:
    def __init__(self, dr_game):
        """initialize the dino and set its starting position"""
        self.screen = dr_game.screen
        self.screen_rect = dr_game.screen.get_rect()

        #load dino image and its rect
        self.images = [
            pygame.image.load('images/yoshi1.png'),
            pygame.image.load('images/yoshi2.png')
            ]
        self.current_image = 0
        self.image = self.images[self.current_image]
        self.rect = self.image.get_rect()

        #set position for dino when game starts
        self.rect.center = self.screen_rect.center

        #run animation timer
        self.animation_time = 0.1
        self.time_elapsed = 0

    def update(self, dt):
        self.time_elapsed += dt

        if self.time_elapsed >= self.animation_time:
            self.time_elapsed = 0
            self.current_image = (self.current_image + 1) % len(self.images)
            self.image = self.images[self.current_image]

    def blitme(self):
        #draw dino at current position
        self.screen.blit(self.image, self.rect)


class Heart:
    def __init__(self, dr_game, x, y):
        """initialize the heart and set its starting position"""
        self.screen = dr_game.screen
        self.screen_rect = dr_game.screen.get_rect()

        #load heart image and its rect
        self.image = pygame.image.load('images/heart.png')
        self.rect = self.image.get_rect()

        #set position for heart when game starts
        self.rect.x = x
        self.rect.y = y

    def blitme(self):
        #draw heart at current position
        self.screen.blit(self.image, self.rect)