import pygame
from utils.contants import RIBOSOME_POSITION

class Ribosome:
    def __init__(self):
        self.position = RIBOSOME_POSITION
        self.bound_trna = None  # Current tRNA bound to the ribosome
        self.synthesized_protein = []

    def update(self, mrna):
        # TODO: draw the current binded trna in the middle
        # TODO: draw next tRNA on right side of screen
        # TODO: draw the last tRNA that finished its job
        pass


    def draw(self, screen):
        # Draw the ribosome on the screen
        pygame.draw.circle(screen, (0, 0, 255), self.position, 20)

    def bind_trna(self, trna):
        self.bound_trna = trna
        self.synthesized_protein.append(trna.amino_acid)
