from enum import Flag, auto


class Nucleotide(Flag):
    A = auto()
    G = auto()
    C = auto()
    U = auto()

ALL = Nucleotide.A | Nucleotide.G | Nucleotide.U | Nucleotide.C