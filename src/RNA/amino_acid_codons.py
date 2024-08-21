from RNA.codon_pattern import CodonPattern
from RNA.nucleotide import Nucleotide, ALL as ALL_NUCLEOTIDES
from RNA.control_codons import *

# A BUNCH of constants.

PHE = CodonPattern('Phenylalanine', (Nucleotide.U, Nucleotide.U, Nucleotide.U | Nucleotide.C))
LEU = CodonPattern('Leucine', (Nucleotide.U, Nucleotide.U, Nucleotide.A | Nucleotide.G),
            (Nucleotide.C, Nucleotide.U, ALL_NUCLEOTIDES))
ILE = CodonPattern('Isoleucine', (Nucleotide.A, Nucleotide.U, Nucleotide.U | Nucleotide.C | Nucleotide.A))
VAL = CodonPattern('Valine', (Nucleotide.G, Nucleotide.U, ALL_NUCLEOTIDES))
SER = CodonPattern('Serine', (Nucleotide.U, Nucleotide.C, ALL_NUCLEOTIDES),
            (Nucleotide.A, Nucleotide.G, Nucleotide.U | Nucleotide.C))
PRO = CodonPattern('Proline', (Nucleotide.C, Nucleotide.C, ALL_NUCLEOTIDES))
THR = CodonPattern('Threonine', (Nucleotide.A, Nucleotide.C, ALL_NUCLEOTIDES))
ALA = CodonPattern('Alanine', (Nucleotide.G, Nucleotide.C, ALL_NUCLEOTIDES))
TYR = CodonPattern('Tyrosine', (Nucleotide.U, Nucleotide.A, Nucleotide.U | Nucleotide.C))
HIS = CodonPattern('Histidine', (Nucleotide.C, Nucleotide.A, Nucleotide.U | Nucleotide.C))
GLN = CodonPattern('Glutamine', (Nucleotide.C, Nucleotide.A, Nucleotide.A | Nucleotide.G))
ASN = CodonPattern('Asparagine', (Nucleotide.A, Nucleotide.A, Nucleotide.U | Nucleotide.C))
LYS = CodonPattern('Lysine', (Nucleotide.A, Nucleotide.A, Nucleotide.A | Nucleotide.G))
ASP = CodonPattern('Aspartate', (Nucleotide.G, Nucleotide.A, Nucleotide.U | Nucleotide.C))
GLU = CodonPattern('Glutamate', (Nucleotide.G, Nucleotide.A, Nucleotide.A | Nucleotide.G))
CYS = CodonPattern('Cysteine', (Nucleotide.U, Nucleotide.G, Nucleotide.U | Nucleotide.C))
TRP = CodonPattern('Tryptophan', (Nucleotide.U, Nucleotide.G, Nucleotide.G))

ARG = CodonPattern('Arginine', (Nucleotide.C, Nucleotide.G, ALL_NUCLEOTIDES),
            (Nucleotide.A, Nucleotide.G, Nucleotide.A | Nucleotide.G))
GLY = CodonPattern('Glycine', (Nucleotide.G, Nucleotide.G, ALL_NUCLEOTIDES))

ALL_ACIDS = [
    BEGIN_CODON, STOP_CODON, PHE, LEU, ILE,
    VAL, SER, PRO, THR, ALA, TYR, HIS, GLN, ASN,
    LYS, ASP, GLU, CYS, TRP, ARG
]