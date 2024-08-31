import pygame
from RNA.insulin import INSOLIN_AS_PRE_MRNA
from simulation import Simulation
from utils.contants import SCREEN_WIDTH, SCREEN_HEIGHT


def main():
    user_input = input("Please enter a DNA sequence (or press Enter to use the default): ")
    if not user_input.strip():
        dna_sequence = INSOLIN_AS_PRE_MRNA
    else:
        dna_sequence = user_input.strip()

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Protein Synthesis Simulation")

    simulation = Simulation(screen, dna_sequence)
    simulation.run()

if __name__ == "__main__":
    print(__package__)
    main()
