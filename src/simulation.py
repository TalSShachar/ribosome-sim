import pygame

from .visualizer import Visualizer
from .RNA.amino_acid_codons import ALL_ACIDS
from .RNA.codon_reader import CodonReader
from .models.ribosome import Ribosome
from .models.mrna import mRNA
from .models.trna import tRNA

# mRNA_SEQUENCE = "A | U | G | U | U | A | U | U | G | U | C | U | U | C | C | U | G | A | U | G | G | U | G | A"
# ANTI_SEQUENCE = "U | A | C | A | A | U | A | A | C | A | G | A | A | G | G | A | C | U | A | C | C | A | C | U"
mRNA_SEQUENCE = "AUGUUAUUGUCUUCCUGAUGGUGA"
ANTI_SEQUENCE = "UACAAUAACAGAAGGACUACCACU"

class Simulation:
    def __init__(self, screen):
        self.current_trnas_to_show = None
        self.screen = screen
        self.visualizer = Visualizer(screen)
        self.codon_reader = CodonReader(ALL_ACIDS)
        self.trna_triplets = self.codon_reader.translate_string_into_triplets(ANTI_SEQUENCE) 


        # assert len(list(self.trna_triplets)) == len(list(acids_chain))
        # self.trna_list = map(lambda anti_codon: tRNA(anticodon=anti_codon, position=(150 + 10, 50)), self.trna_triplets)
        self.trna_list = [  tRNA(anticodon=triplet)
                            for index, triplet in enumerate(self.trna_triplets) ]
        self.trna_list = [None, None, None] + self.trna_list
        self.mrna_triplets = ['', '', ''] + list(self.codon_reader._string_chunk(mRNA_SEQUENCE, 3))
        self.current_triplet_index = 0

        self.mrna = mRNA(sequence="")
        self.ribosome = Ribosome()

    def update(self):
        self.mrna.update(''.join(self.mrna_triplets[self.current_triplet_index : self.current_triplet_index + 4]))
        self.current_trnas_to_show = self.trna_list[self.current_triplet_index : self.current_triplet_index + 4]

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
                        self.backStep()

            self.update()
            self.screen.fill('white')
            self.draw()
            pygame.display.flip()

        pygame.quit()
