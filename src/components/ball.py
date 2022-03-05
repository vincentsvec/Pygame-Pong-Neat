"""
module for ball
"""
import pygame
import random
from config.globals import ball_conf


class Ball:
    def __init__(self, surface, paddles):
        self.dis = surface
        self.paddles = paddles
        self.radius = ball_conf["radius"]
        self.color = ball_conf["color"]
        self.speed = ball_conf["speed"]
        self.posx = self.dis.get_width() / 2
        self.posy = self.dis.get_height() / 2
        self.vectorX, self.vectorY = self.generate_vector()

    def update(self):
        """
        Updates all properties of ball. Returns True if game is over.
        """
        self.draw()
        if self.check_collision():
            return True

        self.move()

    def draw(self):
        """
        Draws the ball.
        """
        self.rect = pygame.draw.circle(self.dis, self.color, [
            self.posx, self.posy], self.radius, self.radius)

    def move(self):
        """
        Moves the ball by adding the vecors to positon of the ball.
        """
        self.posx += self.vectorX
        self.posy += self.vectorY

    def generate_vector(self):
        """
        Randomly generates initial vectors.
        """
        x = random.choice((-self.speed, self.speed))
        y = random.choice((-self.speed, self.speed))
        return x, y

    def check_collision(self):
        """
        Checks for different collisions. If ball hits the returns True if game is over.
        """

        # ball hits the upper or bottom wall
        if self.posy <= 0 or self.posy >= self.dis.get_height():
            self.vectorY *= -1

        # ball hits the paddle
        for paddle in self.paddles:
            if paddle.get_rect().colliderect(self.rect):
                self.vectorX *= -1

        # ball hits left or right wall
        if self.posx <= 0 or self.posx >= self.dis.get_width():
            return True
