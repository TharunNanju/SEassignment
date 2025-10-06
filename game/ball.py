import pygame
import random

pygame.mixer.init()

SOUND_PADDLE = pygame.mixer.Sound("assets/sounds/paddle_hit.mp3")
SOUND_WALL = pygame.mixer.Sound("assets/sounds/wall_bounce.mp3")
SOUND_SCORE = pygame.mixer.Sound("assets/sounds/score.mp3")

class Ball:
    def __init__(self, x, y, width, height, screen_width, screen_height):
        self.original_x = x
        self.original_y = y
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.velocity_x = random.choice([-5, 5])
        self.velocity_y = random.choice([-3, 3])

    def move(self, player, ai):
        # Move
        self.x += self.velocity_x
        self.y += self.velocity_y

        # Bounce off top/bottom walls
        if self.y <= 0 or self.y + self.height >= self.screen_height:
            self.velocity_y *= -1
            SOUND_WALL.play()

        # Collision with paddles
        if self.rect().colliderect(player.rect()):
            self.x = player.x + player.width
            self.velocity_x *= -1
            SOUND_PADDLE.play()

        elif self.rect().colliderect(ai.rect()):
            self.x = ai.x - self.width
            self.velocity_x *= -1
            SOUND_PADDLE.play()

    def reset(self):
        # Reset position
        self.x = self.original_x
        self.y = self.original_y
        self.velocity_x *= -1
        self.velocity_y = random.choice([-3, 3])
        SOUND_SCORE.play()

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
