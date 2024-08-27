from .codon_pattern import CodonPattern
from .nucleotide import Nucleotide, ALL as ALL_NUCLEOTIDES
from .control_codons import *

# A BUNCH of constants.

PHE = CodonPattern('F', 'Phenylalanine', (Nucleotide.U, Nucleotide.U, Nucleotide.U | Nucleotide.C))
LEU = CodonPattern('L', 'Leucine', (Nucleotide.U, Nucleotide.U, Nucleotide.A | Nucleotide.G),
            (Nucleotide.C, Nucleotide.U, ALL_NUCLEOTIDES))
ILE = CodonPattern('I', 'Isoleucine', (Nucleotide.A, Nucleotide.U, Nucleotide.U | Nucleotide.C | Nucleotide.A))
VAL = CodonPattern('V', 'Valine', (Nucleotide.G, Nucleotide.U, ALL_NUCLEOTIDES))
SER = CodonPattern('S', 'Serine', (Nucleotide.U, Nucleotide.C, ALL_NUCLEOTIDES),
            (Nucleotide.A, Nucleotide.G, Nucleotide.U | Nucleotide.C))
PRO = CodonPattern('P', 'Proline', (Nucleotide.C, Nucleotide.C, ALL_NUCLEOTIDES))
THR = CodonPattern('T', 'Threonine', (Nucleotide.A, Nucleotide.C, ALL_NUCLEOTIDES))
ALA = CodonPattern('A', 'Alanine', (Nucleotide.G, Nucleotide.C, ALL_NUCLEOTIDES))
TYR = CodonPattern('Y', 'Tyrosine', (Nucleotide.U, Nucleotide.A, Nucleotide.U | Nucleotide.C))
HIS = CodonPattern('H', 'Histidine', (Nucleotide.C, Nucleotide.A, Nucleotide.U | Nucleotide.C))
GLN = CodonPattern('Q', 'Glutamine', (Nucleotide.C, Nucleotide.A, Nucleotide.A | Nucleotide.G))
ASN = CodonPattern('N', 'Asparagine', (Nucleotide.A, Nucleotide.A, Nucleotide.U | Nucleotide.C))
LYS = CodonPattern('K', 'Lysine', (Nucleotide.A, Nucleotide.A, Nucleotide.A | Nucleotide.G))
ASP = CodonPattern('D', 'Aspartate', (Nucleotide.G, Nucleotide.A, Nucleotide.U | Nucleotide.C))
GLU = CodonPattern('E', 'Glutamate', (Nucleotide.G, Nucleotide.A, Nucleotide.A | Nucleotide.G))
CYS = CodonPattern('C', 'Cysteine', (Nucleotide.U, Nucleotide.G, Nucleotide.U | Nucleotide.C))
TRP = CodonPattern('W', 'Tryptophan', (Nucleotide.U, Nucleotide.G, Nucleotide.G))

ARG = CodonPattern('R', 'Arginine', (Nucleotide.C, Nucleotide.G, ALL_NUCLEOTIDES),
            (Nucleotide.A, Nucleotide.G, Nucleotide.A | Nucleotide.G))
GLY = CodonPattern('G', 'Glycine', (Nucleotide.G, Nucleotide.G, ALL_NUCLEOTIDES))

ALL_ACIDS = [
    BEGIN_CODON, STOP_CODON, PHE, LEU, ILE,
    VAL, SER, PRO, THR, ALA, TYR, HIS, GLN, ASN,
    LYS, ASP, GLU, CYS, TRP, ARG, GLY
]