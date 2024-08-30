import pygame
from RNA.insulin import INSOLIN_AS_PRE_MRNA
from simulation import Simulation
from utils.contants import SCREEN_WIDTH, SCREEN_HEIGHT


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Protein Synthesis Simulation")

    simulation = Simulation(screen, INSOLIN_AS_PRE_MRNA)
    simulation.run()

if __name__ == "__main__":
    print(__package__)
    main()
