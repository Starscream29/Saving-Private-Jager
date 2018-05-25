import pygame as py
import math
from Functions import constrain


class Scott(py.sprite.Sprite):
    # Create player
    def __init__(self, screen):

        py.sprite.Sprite.__init__(self)

        self.image = py.image.load("Images/SC.PNG").convert()
        self.center = (650, 300)
        self.width, self.height = screen.get_size()
        self.rect = self.image.get_rect(center=self.center)
        self.step = 5
        self.angle = self.get_angle(py.mouse.get_pos())

    def get_angle(self, mouse):
        # Find angle between center of player and mouse location
        offset = (self.rect.centerx - mouse[0], self.rect.centery - mouse[1])
        self.angle = math.degrees(math.atan2(offset[0], offset[1])) - 135

    def update(self):
        # Movement
        # Constrain is present to keep the player from moving out of bounds
        key = py.key.get_pressed()

        if key[py.K_RIGHT] or key[py.K_d]:
            self.rect.x += self.step
            self.rect.centerx = constrain(self.rect.centerx, 0, self.width - self.step)
        if key[py.K_LEFT] or key[py.K_a]:
            self.rect.x -= self.step
            self.rect.centerx = constrain(self.rect.centerx, 0, self.width - self.step)
        if key[py.K_UP] or key[py.K_w]:
            self.rect.y -= self.step
            self.rect.centery = constrain(self.rect.centery, 0, self.height - self.step)
        if key[py.K_DOWN] or key[py.K_s]:
            self.rect.y += self.step
            self.rect.centery = constrain(self.rect.centery, 0, self.height - self.step)

    def get_event(self, event, bulletList):
        # Check for mouse button pressed (left)
        if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
            bulletList.add(Bullet(self.rect.center, self.angle))
        # Check for mouse movement
        if event.type == py.MOUSEMOTION:
            self.get_angle(event.pos)

    def draw(self, surface):
        # Draw image
        surface.blit(self.image, self.rect)


class Bullet(py.sprite.Sprite):
    # Class for bullets
    def __init__(self, location, angle):

        py.sprite.Sprite.__init__(self)

        # Creates bullet
        self.image = py.Surface([10, 10])
        self.image.fill((255, 0, 0))
        # Calculates angle based off of angle from Player class
        self.angle = -math.radians(angle-135)
        # Create a rect at the center of location
        self.rect = self.image.get_rect(center=location)
        # Coordinates
        self.move = [self.rect.x, self.rect.y]
        # Speed magnitude (can change for faster bullet)
        self.speed_magnitude = 10
        # Determines speed based off of angles
        self.speed = (self.speed_magnitude*math.cos(self.angle), self.speed_magnitude*math.sin(self.angle))
        self.screen_rect = py.display.get_surface().get_rect()

    def update(self, screen_rect):
        # Add speed to coordinates for movement of bullet
        self.move[0] += self.speed[0]
        self.move[1] += self.speed[1]
        # New coordinates
        self.rect.topleft = self.move
        # Bullets that have left the screen will be removed from the sprite group
        self.remove(screen_rect)

    def remove(self, screen_rect):
        if not self.rect.colliderect(screen_rect):
            self.kill()

class Jager(py.sprite.Sprite):
    # Create Jager
    def __init__(self, screen):

        py.sprite.Sprite.__init__(self)

        self.image = py.image.load("Images/Jager.PNG").convert()
        self.center = (650, 500)
        self.width, self.height = screen.get_size()
        self.rect = self.image.get_rect(center=self.center)

    def draw(self, surface):
        # Draw image
        surface.blit(self.image, self.rect)
