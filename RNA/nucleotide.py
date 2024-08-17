from enum import Flag, auto


class Nucleotide(Flag):
    A = auto()
    G = auto()
    T = auto()
    U = auto()