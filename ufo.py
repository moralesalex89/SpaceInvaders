import pygame

ufo_a = pygame.image.load('images/ufo_a.png')
ufo_b = pygame.image.load('images/ufo_b.png')
ufo_c = pygame.image.load('images/ufo_c.png')
ufo_d = pygame.image.load('images/ufo_d.png')
ufo_e = pygame.image.load('images/ufo_e.png')
ufo_f = pygame.image.load('images/ufo_f.png')
d_ufo_a = ''
d_ufo_b = ''
sound_a = ''
sound_b = ''
pygame.init()
ufo_sound = pygame.mixer.Sound('sounds/ufo_highpitch.wav')

ufo = [ufo_a, ufo_b, ufo_c, ufo_d, ufo_e, ufo_f]
d_ufo = [d_ufo_a, d_ufo_b]
sound = [sound_a, sound_b]


class UFO:
    def __init__(self, ai_settings, screen, sounds):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = ufo_a
        self.rect = self.image.get_rect()
        self.rect.right = 0
        self.rect.bottom = ai_settings.alien_start_pos_y - ai_settings.alien_space_factor
        self.state = 0
        self.score = 1000
        self.hit = False
        self.sounds = sounds

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def set_spawn(self, is_left):
        if self.sounds.ufo_loop is False:
            self.sounds.ufo_play()

        if is_left:
            self.rect.right = 0
            self.state = 1
        else:
            self.rect.left = self.ai_settings.screen_width
            self.state = 2

    def update(self):
        self.rotate()
        if self.state == 1 and self.rect.left < self.ai_settings.screen_width:
            self.rect.x += self.ai_settings.ufo_speed_factor
        elif self.state == 2 and self.rect.right > 0:
            self.rect.x -= self.ai_settings.ufo_speed_factor
        else:
            self.state = 0
            self.sounds.ufo_stop()

    def rotate(self):
        frame = ufo.index(self.image)
        frame += 1
        frame = frame % len(ufo)
        self.image = ufo[frame]
#        if frame / 2 == 0:
#            ufo_sound.play()

    def active(self):
        if self.state == 0:
            return False
        else:
            return True

    def destroy(self):
        self.state = 0
        self.hit = True
        self.rect.right = 0
        self.sounds.ufo_stop()
        self.sounds.shoot_play()

    def reset(self):
        self.state = 0
        self.rect.right = 0
        self.image = ufo_a
        self.hit = False
        self.sounds.ufo_stop()
