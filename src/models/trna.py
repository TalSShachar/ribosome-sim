import pygame
from src.RNA.nucleotide import NucleotideTriplet, to_complementing_codon
from src.RNA.codon_pattern import CodonPattern
from src.utils.drawingUtil import draw_polygon_with_bottom_teeth
from src.RNA.codon_reader import CodonReader
from src.RNA.amino_acid_codons import ALL_ACIDS
from src.utils.contants import *
from enum import Enum

class DrawingType(Enum):
    OUTGOING = 0
    FIRST = 1
    SECOND = 2
    INCOMING = 3
tRNA_DRAWING_TYPES_MATCHER = {DrawingType.OUTGOING: tRNA_OUTGOING, DrawingType.FIRST: FIRST_tRNA_IN_RIBOSOME, DrawingType.SECOND: SECOND_tRNA_IN_RIBOSOME, DrawingType.INCOMING: tRNA_INCOMING}


def triplet_to_string(triplet: NucleotideTriplet) -> str:
    return "    ".join(nucleotide.name for nucleotide in triplet)


class tRNA:
    def __init__(self, anticodon: NucleotideTriplet):
        self.anticodon = anticodon
        self.amino_acid = self.producedAminoAcid()
        self.bound = False  # Whether it is bound to the ribosome
    
    def producedAminoAcid(self) -> CodonPattern | None:
        reader = CodonReader(ALL_ACIDS)
        return reader.translate(self.anticodon)

    def update(self, ribosome):
        # Logic for tRNA movement towards the ribosome and binding
        pass


    def draw(self, screen, type: DrawingType):
        position = tRNA_DRAWING_TYPES_MATCHER[type]
        x,y = position[0], position[1]
        draw_polygon_with_bottom_teeth(screen, 'yellow', x, y, 80, 130, 20, 2)
        pygame.draw.circle(screen, 'pink', (x+40,y-25), 20)

        # Add text to polynom
        font = pygame.font.Font(None, 24)
        screen.blit(font.render('tRNA', True, 'black'),  (x + 10, y + 15))
        screen.blit((font.render(triplet_to_string(self.anticodon), True, 'red')), (x + 8, y + 90))

        # Add text to polynom
        screen.blit((font.render(self.amino_acid.name, True, 'red')), (x+40,y-25))
