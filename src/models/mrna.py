import pygame
from src.utils.drawingUtil import draw_polygon_with_upper_teeth
from src.utils.contants import mRNA_POSITION 

class mRNA:
    def __init__(self, sequence: str):
        self.sequence = sequence
        self.position = mRNA_POSITION 

    def update(self):
        # Logic to move the mRNA or manage its interaction with the ribosome
        pass

    def draw(self, screen):
        draw_polygon_with_upper_teeth(screen, 'gray', self.position[0], self.position[1], 500, 50, 20, 10)
        
        font = pygame.font.Font(None, 24)
        screen.blit((font.render(self.sequence, True, 'red')), self.position)
