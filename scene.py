import pygame

class RollingBackground:
    def __init__(self, dr_game):
        """initialize the background and set its starting position"""
        self.screen = dr_game.screen
        self.screen_rect = dr_game.screen.get_rect()

        #load background image and its rect
        self.image = pygame.image.load('images/background.png')
        self.rect = self.image.get_rect()

        self.rect1 = self.image.get_rect()
        self.rect2 = self.image.get_rect()

        #set position for background when game starts
        self.rect1.x = 0
        self.rect1.y = 150

        self.rect2.x = self.rect1.width
        self.rect2.y = 150

    def update(self):
        self.rect1.x -= 2
        self.rect2.x -= 2
        if self.rect1.right <= 0:
            self.rect1.x = self.rect2.right
        if self.rect2.right <= 0:
            self.rect2.x = self.rect1.right

    def blitme(self):
        #draw background at current position
        self.screen.blit(self.image, self.rect1)
        self.screen.blit(self.image, self.rect2)



class Obstacle1:
    def __init__(self, dr_game):
        """initialize the obstacle and set its starting position"""
        self.screen = dr_game.screen
        self.screen_rect = dr_game.screen.get_rect()

        #load obstacle image and its rect
        self.image = pygame.image.load('images/obstacle1.png')
        self.rect = self.image.get_rect()

        #set position for obstacle when game starts
        self.rect.x = 900
        self.rect.y = 275

    def update(self):
        self.rect.x -= 2

        if self.rect.right <= 0:
            self.rect.x = 1200


    def blitme(self):
        #draw obstacle at current position
        self.screen.blit(self.image, self.rect)