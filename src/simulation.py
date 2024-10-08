import pygame

from RNA.splicing.spliceosome import Exon, Spliceosome
from utils.string_util import chunk_string

from visualizer import Visualizer
from RNA.amino_acid_codons import ALL_ACIDS
from RNA.codon_reader import CodonPatternMatch, CodonReader
from models.ribosome import Ribosome
from models.mrna import mRNA
from models.trna import tRNA

# mRNA_SEQUENCE = "A | U | G | U | U | A | U | U | G | U | C | U | U | C | C | U | G | A | U | G | G | U | G | A"
# ANTI_SEQUENCE = "U | A | C | A | A | U | A | A | C | A | G | A | A | G | G | A | C | U | A | C | C | A | C | U"
mRNA_SEQUENCE = "AUGUUAUUGUCUUCCUGAUGGUGA"
ANTI_SEQUENCE = "UACAAUAACAGAAGGACUACCACU"

# Model <X> View
# Controller -> View
# Controller -> Model

# DNA -> pre mRNA -> [ mRNA -> Polypeptide Chain ]

MRNA_TRIPLETS_TO_SHOW_ON_SCREEN = 4

class Simulation:
    def __init__(self, screen: pygame.Surface, dna_sequence: str):
        self.current_trnas_to_show = None
        self.screen = screen
        self.visualizer = Visualizer(screen)
        
        exons = Spliceosome().splice(dna_sequence)
        self.codon_reader = CodonReader(ALL_ACIDS)

        self.polypeptide_chain, self.polypeptide_chain_length, self.error_at_end = Simulation._parse_until_failure(self.codon_reader, exons)

        # assert len(list(self.trna_triplets)) == len(list(acids_chain))
        # self.trna_list = map(lambda anti_codon: tRNA(anticodon=anti_codon, position=(150 + 10, 50)), self.trna_triplets)
        self.trna_list: list[tRNA] = [
            tRNA(codon_match.pattern.name, codon_match.get_match_string())
            for codon_match in self.polypeptide_chain
            ]

        self.trna_list = [None, None, None, *self.trna_list]
        self.current_triplet_index = 0

        self.mrna_string = ''.join(match.actual_match if match else '   ' for match in self.trna_list)
        
        self.mrna = mRNA(sequence='')
        self.ribosome = Ribosome()

    @staticmethod
    def _parse_until_failure(codon_reader: CodonReader, exons: list[Exon]) -> tuple[list[CodonPatternMatch], int, bool]:
        result = []
        was_error = True
        CodonPatternMatchLength = 0
        iter = codon_reader.translate_exons(exons)
        while True:
            try:
                result.append(next(iter))
                CodonPatternMatchLength += 1
                was_error = False
            except ValueError:
                was_error = True
                break
            except StopIteration:
                break

        return (result, CodonPatternMatchLength, was_error)

    def update(self):
        start_point = self.current_triplet_index * 3
        nucleotides_to_view = 3 * MRNA_TRIPLETS_TO_SHOW_ON_SCREEN

        new_mrna_slice = self.mrna_string[start_point:start_point + nucleotides_to_view]
        self.mrna.update(new_mrna_slice)

        self.current_trnas_to_show = self.trna_list[self.current_triplet_index : self.current_triplet_index + MRNA_TRIPLETS_TO_SHOW_ON_SCREEN]

    def nextStep(self):
        self.current_triplet_index += 1
        self.mrna.sequence=self.mrna.sequence[3:]

    def backStep(self):
        self.current_triplet_index -= 1

    def draw(self):
        self.visualizer.draw_mrna(self.mrna)
        self.visualizer.draw_ribosome(self.ribosome)
        self.visualizer.draw_trna_list(self.current_trnas_to_show)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_DOWN:
                        print("Down arrow key pressed!")
                        self.nextStep()    
                    if event.key == pygame.K_UP:
                        print("Up arrow key pressed!")
                        if self.current_triplet_index != 0:
                            self.backStep()
                        print(self.current_triplet_index)
            if (self.current_triplet_index > self.polypeptide_chain_length and self.error_at_end == True):
                font = pygame.font.SysFont(None, 36)
                text = font.render('Faulty DNA', True, 'white')
                bubble_rect = pygame.Rect(400, 250, 200, 100)
                pygame.draw.ellipse(self.screen, 'blue', bubble_rect)
                text_rect = text.get_rect(center=bubble_rect.center)
                self.screen.blit(text, text_rect)
                pygame.display.flip()
            else:
                self.update()
                self.screen.fill('white')
                self.draw()
                pygame.display.flip()
        
        pygame.quit()