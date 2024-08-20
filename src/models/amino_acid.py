import pygame

class AminoAcid:
    def __init__(self, name, color, position):
        self.name = name
        self.color = color
        self.position = position

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.position, 10)
