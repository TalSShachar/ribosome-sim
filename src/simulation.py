import pygame
from src.models.ribosome import Ribosome
from src.models.mrna import mRNA
from src.models.trna import tRNA
from src.visualizer import Visualizer


class Simulation:
    def __init__(self, screen):
        self.screen = screen
        self.ribosome = Ribosome((100, 100))
        self.mrna = mRNA(sequence="AUGCGAUAA", position=(100, 300))
        self.trna_list = [tRNA(anticodon="UAC", amino_acid="Methionine", position=(150, 50))]
        self.visualizer = Visualizer(screen)

    def update(self):
        self.ribosome.update(self.mrna)
        for trna in self.trna_list:
            trna.update(self.ribosome)

    def draw(self):
        self.visualizer.draw_ribosome(self.ribosome)
        self.visualizer.draw_mrna(self.mrna)
        self.visualizer.draw_trna_list(self.trna_list)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.update()
            self.screen.fill('white')
            self.draw()
            pygame.display.flip()

        pygame.quit()
