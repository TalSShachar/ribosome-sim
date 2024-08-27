import pygame
from src.simulation import Simulation
from src.utils.contants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Protein Synthesis Simulation")

    simulation = Simulation(screen)
    simulation.run()

if __name__ == "__main__":
    print(__package__)
    main()
