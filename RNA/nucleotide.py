from enum import Flag, auto

class Nucleotide(Flag):
    G = auto()
    C = auto()
    U = auto()
    A = auto()

ANTI = {
    Nucleotide.A: Nucleotide.U, 
    Nucleotide.U: Nucleotide.A, 
    Nucleotide.C: Nucleotide.G, 
    Nucleotide.G: Nucleotide.C, 
}

def to_anti_nucleotide(n: Nucleotide) -> Nucleotide:
    return Nucleotide(sum([ANTI[flag].value for flag in n]))

def to_anti_codon(codon: tuple[Nucleotide, Nucleotide, Nucleotide]):
    return (to_anti_nucleotide(codon[0]),
            to_anti_nucleotide(codon[1]),
            to_anti_nucleotide(codon[2]))

ALL = Nucleotide.A | Nucleotide.G | Nucleotide.U | Nucleotide.C

NucleotideTriplet = tuple[Nucleotide, Nucleotide, Nucleotide]
