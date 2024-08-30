import pygame
from RNA.nucleotide import COMPLEMENT_NUCLEOTIDE_STRING
from utils.drawingUtil import draw_polygon_with_bottom_teeth
from utils.contants import *
from enum import Enum

class DrawingType(Enum):
    OUTGOING = 0
    FIRST = 1
    SECOND = 2
    INCOMING = 3
tRNA_DRAWING_TYPES_MATCHER = {
    DrawingType.OUTGOING: tRNA_OUTGOING,
    DrawingType.FIRST: FIRST_tRNA_IN_RIBOSOME,
    DrawingType.SECOND: SECOND_tRNA_IN_RIBOSOME,
    DrawingType.INCOMING: tRNA_INCOMING
}

class tRNA:
    amino_acid_name: str
    actual_match: str
    bound: bool

    def __init__(self, amino_acid_name: str, actual_match: str):
        self.amino_acid_name = amino_acid_name
        self.actual_match = tRNA._translate_match_to_complement(actual_match)
        self.bound = False  # Whether it is bound to the ribosome element on screen

    def update(self, ribosome):
        # Logic for tRNA movement towards the ribosome and binding
        pass

    @staticmethod
    def _translate_match_to_complement(match: str):
        return ''.join(COMPLEMENT_NUCLEOTIDE_STRING[c] for c in match)

    @staticmethod
    def _space_characters(string: str, space: int):
        return (space * ' ').join(string)

    def draw(self, screen, type: DrawingType):
        position = tRNA_DRAWING_TYPES_MATCHER[type]
        x,y = position[0], position[1]
        draw_polygon_with_bottom_teeth(screen, 'yellow', x, y, 80, 130, 20, 2)
        pygame.draw.circle(screen, 'pink', (x+40,y-25), 20)

        # Add text to polynom
        font = pygame.font.Font(None, 24)
        screen.blit(font.render('tRNA', True, 'black'),  (x + 10, y + 15))
        screen.blit((font.render(tRNA._space_characters(self.actual_match, 4), True, 'red')), (x + 8, y + 90))

        # Add text to polynom
        screen.blit((font.render(self.amino_acid_name[:3], True, 'red')), (x+27,y-30))
