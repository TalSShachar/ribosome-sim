import pygame

class Ribosome:
    def __init__(self, position):
        self.position = position
        self.bound_trna = None  # Current tRNA bound to the ribosome
        self.synthesized_protein = []

    def update(self, mrna):
        # Logic for binding tRNA, reading mRNA, and adding amino acids
        pass


    def draw(self, surface):
        # Draw the ribosome on the screen
        pygame.draw.circle(surface, (0, 0, 255), self.position, 20)

    def bind_trna(self, trna):
        self.bound_trna = trna
        self.synthesized_protein.append(trna.amino_acid)
