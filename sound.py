import pygame

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()


class Sound:
    def __init__(self):
        self.ufo = pygame.mixer.Sound('sounds/ufo_highpitch.wav')
        self.ufo_loop = False
        self.ufo.set_volume(0.1)
        self.laser = pygame.mixer.Sound('sounds/invaderkilled.wav')
        self.laser.set_volume(0.1)
        self.shoot = pygame.mixer.Sound('sounds/shoot.wav')
        self.shoot.set_volume(0.1)
        self.explosion = pygame.mixer.Sound('sounds/explosion.wav')
        self.explosion.set_volume(0.1)

    def ufo_play(self):
        self.ufo.play(-1)
        self.ufo_loop = True

    def ufo_stop(self):
        self.ufo.stop()
        self.ufo_loop = False

    def laser_play(self):
        self.laser.play()

    def shoot_play(self):
        self.shoot.play()

    def explosion_play(self):
        self.explosion.play()
