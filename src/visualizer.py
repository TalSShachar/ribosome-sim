import pygame
from src.utils.drawingUtil import *

class Visualizer:
    def __init__(self, screen):
        self.screen = screen

    def draw_ribosome(self, ribosome):
        pygame.draw.circle(self.screen, (0, 0, 255), ribosome.position, 20)

    def draw_mrna(self, mrna):
        mrna.draw(self.screen)
                              
    def draw_trna_list(self, trna_list):
        for trna in trna_list:
            # pygame.draw.polygon(self.screen, (0, 255, 0), self.calculate_trna_points(trna.position))
            trna.draw(self.screen)
    
    def calculate_trna_points(self, position):
        x, y = position
        return [(x, y), (x + 20, y), (x + 10, y + 30)]
