import pygame
from src.RNA.codon_pattern import CodonPattern
from src.RNA.amino_acid_codons import ALL_ACIDS

class AminoAcid:
    def __init__(self, name, color, position):
        self.name = name
        self.color = color
        self.position = position

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, 10)
