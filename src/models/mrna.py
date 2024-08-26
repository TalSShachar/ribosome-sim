import pygame
from src.utils.drawingUtil import draw_polygon_with_upper_teeth
from src.utils.contants import mRNA_POSITION 

class mRNA:
    def __init__(self, sequence: str):
        self.sequence = sequence

    def update(self, newSequence):
        self.sequence = newSequence

    def draw(self, screen):
        position = mRNA_POSITION
        x, y = position
        draw_polygon_with_upper_teeth(screen, 'gray', x, y, 700, 20, 20, 20)
        
        font = pygame.font.Font(None, 24)
        text = font.render("     ".join(list(self.sequence)), True, 'black')
        screen.blit(text, (x + 568 - (len(self.sequence)/4)*135, y - 10))
