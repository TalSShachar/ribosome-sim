from src.utils.drawingUtil import draw_polygon_with_upper_teeth

class mRNA:
    def __init__(self, sequence, position):
        self.sequence = sequence  # List of codons (e.g., ['AUG', 'CGA', 'UAA'])
        self.position = position

    def update(self):
        # Logic to move the mRNA or manage its interaction with the ribosome
        pass

    def draw(self, screen):
        draw_polygon_with_upper_teeth(screen, 'blue', self.position[0], self.position[1], 500, 130, 20, 10)

        # # Draw mRNA as a series of codons
        # for i, codon in enumerate(self.sequence):
        #     codon_position = (self.position[0] + i * 30, self.position[1])
        #     pygame.draw.rect(screen, (0, 0, 0), (*codon_position, 20, 20))
        #     # Optionally draw the codon letters
