from enum import Flag, auto


class Nucleotide(Flag):
    """
    Implemented as an Enum flag class - meaning that A nucleotide value can consist of multiple possible nucleotides.
    Under the hood this is implemented through binary digits
    For example, in a usage in difining a codon pattern AUM where M can be either U or G,
    Nucleotide.G | Nucleotide.U can be used to express M.
    """
    G = auto() # 0b0001
    C = auto() # 0b0010
    U = auto() # 0b0100
    A = auto() # 0b1000

# A type alias for a nucleotide triplet
type NucleotideTriplet = tuple[Nucleotide, Nucleotide, Nucleotide]

# The complementing Nucleotide when looking at tRNA<->mRNA
COMPLEMENT_NUCLEOTIDE = {
    Nucleotide.A: Nucleotide.U, 
    Nucleotide.U: Nucleotide.A, 
    Nucleotide.C: Nucleotide.G, 
    Nucleotide.G: Nucleotide.C, 
}


# Takes in a Nucleotide value that can have differnt explicit matches (For example, [AU] in regex),
# Takes the complements of all possible nucleotides,
# and sums them up (Since all possible flags are flags and are distinct, summing is equivalent to a binary | operator)
def to_anti_nucleotide(n: Nucleotide) -> Nucleotide:
    return Nucleotide(sum([COMPLEMENT_NUCLEOTIDE[flag].value for flag in n]))

# Takes in a codon (A triplet of nucleotides, each being possible a pattern opposed to an explicit nucleotide)
# And returns the triplet of complementing nucleotides
def to_complementing_codon(codon: NucleotideTriplet):
    return (to_anti_nucleotide(codon[0]),
            to_anti_nucleotide(codon[1]),
            to_anti_nucleotide(codon[2]))

# An Nucleotide enum value that matches all 4 nucleotides
ALL = Nucleotide.A | Nucleotide.G | Nucleotide.U | Nucleotide.C