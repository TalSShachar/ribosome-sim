import pygame
from src.RNA.nucleotide import NucleotideTriplet, to_anti_codon
from src.RNA.codon_pattern import CodonPattern
from src.utils.drawingUtil import draw_polygon_with_bottom_teeth
from src.RNA.codon_reader import CodonReader
from src.RNA.amino_acid_codons import ALL_ACIDS

class tRNA:
    def __init__(self, anticodon: NucleotideTriplet, position):
        self.anticodon = anticodon
        self.amino_acid = self.producedAminoAcid()
        self.position = position
        self.bound = False  # Whether it is bound to the ribosome
    
    def producedAminoAcid(self) -> CodonPattern | None:
        reader = CodonReader(ALL_ACIDS)
        return reader.translate(self.anticodon)

    def update(self, ribosome):
        # Logic for tRNA movement towards the ribosome and binding
        pass


    def draw(self, screen):
        x,y = self.position[0], self.position[1]
        draw_polygon_with_bottom_teeth(screen, 'yellow', x, y, 80, 130, 20, 2)
    
        font = pygame.font.Font(None, 24)
        screen.blit(font.render('tRNA', True, 'black'),  (x + 10, y + 15))
        screen.blit((font.render(self.triplet_to_string(self.anticodon), True, 'red')), (x + 10, y + 70))

    def triplet_to_string(self, triplet: NucleotideTriplet) -> str:
        return ''.join(nucleotide.name for nucleotide in triplet)
