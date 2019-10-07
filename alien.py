import pygame
from pygame.sprite import Sprite

alien1_a = pygame.image.load("images/alien1_a.png")
alien1_b = pygame.image.load("images/alien1_b.png")
alien2_a = pygame.image.load("images/alien2_a.png")
alien2_b = pygame.image.load("images/alien2_b.png")
alien3_a = pygame.image.load("images/alien3_a.png")
alien3_b = pygame.image.load("images/alien3_b.png")

alien_a = [alien1_a, alien2_a, alien3_a]
alien_b = [alien1_b, alien2_b, alien3_b]

ufo_a = pygame.image.load("images/ufo_a.png")
ufo_b = pygame.image.load("images/ufo_b.png")
ufo_c = pygame.image.load("images/ufo_c.png")


class Alien(Sprite):

    def __init__(self, ai_settings, screen, sounds, alien_type, alt_frame):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.sounds = sounds
        self.type = alien_type
        self.image = alien_a[self.type]
        if alt_frame:
            self.rotate()
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

        self.score = self.get_score()

    def get_score(self):
        if self.type == 0:
            return 400
        elif self.type == 1:
            return 200
        else:
            return 100

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def rotate(self):
        if self.image is alien_b[self.type]:
            self.image = alien_a[self.type]
        else:
            self.image = alien_b[self.type]

    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def hit(self):
        self.sounds.shoot_play()
        self.kill()

    def save_spawn(self):
        self.start_x = self.rect.x
        self.start_y = self.rect.y

    def respawn(self):
        self.rect.x = self.start_x
        self.rect.y = self.start_y
