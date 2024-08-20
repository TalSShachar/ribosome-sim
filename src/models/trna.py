import pygame
from src.utils.drawingUtil import draw_polygon_with_bottom_teeth

class tRNA:
    def __init__(self, anticodon, amino_acid, position):
        self.anticodon = anticodon
        self.amino_acid = amino_acid
        self.position = position
        self.bound = False  # Whether it is bound to the ribosome

    def update(self, ribosome):
        # Logic for tRNA movement towards the ribosome and binding
        pass


    def draw(self, screen):
        x,y = self.position[0], self.position[1]
        draw_polygon_with_bottom_teeth(screen, 'yellow', x, y, 80, 130, 20, 2)
    
        font = pygame.font.Font(None, 24)
        screen.blit(font.render('tRNA', True, 'black'),  (x + 10, y + 15))
        screen.blit((font.render(self.anticodon, True, 'red')), (x + 10, y + 70))