import pygame
from .models.ribosome import Ribosome
from .models.mrna import mRNA
from .models.trna import tRNA
from .visualizer import Visualizer
from .RNA.nucleotide import Nucleotide

mRNA_SEQUENCE = "AUGUUAUUGUCUUCCUGAUGGUGA"
ANTI_SEQUENCE = "UACAAUAACAGAAGGACUACCACU"

class Simulation:
    def __init__(self, screen):
        self.screen = screen
        self.mrna = mRNA(sequence=mRNA_SEQUENCE)
        self.ribosome = Ribosome()
        self.trna_list = [tRNA(anticodon=(Nucleotide.U,Nucleotide.A, Nucleotide.A), position=(150, 50))]
        self.visualizer = Visualizer(screen)
        self.current_anticodon_index = 0

    def update(self):
        self.ribosome.update(self.mrna)
        for trna in self.trna_list:
            trna.update(self.ribosome)

    def draw(self):
        self.visualizer.draw_mrna(self.mrna)
        self.visualizer.draw_ribosome(self.ribosome)
        self.visualizer.draw_trna_list(self.trna_list)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        print("Down arrow key pressed!")
                        self.current_anticodon_index += 3
            
            self.update()
            self.screen.fill('white')
            self.draw()
            pygame.display.flip()

        pygame.quit()
