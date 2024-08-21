from RNA.codon_pattern import CodonPattern
from RNA.nucleotide import Nucleotide, ALL as ALL_NUCLEOTIDES
from RNA.control_codons import *

PHE = CodonPattern('Phe', (Nucleotide.U, Nucleotide.U, Nucleotide.U | Nucleotide.C))
LEU = CodonPattern('Leu', (Nucleotide.U, Nucleotide.U, Nucleotide.A | Nucleotide.G),
            (Nucleotide.C, Nucleotide.U, ALL_NUCLEOTIDES))
LLE = CodonPattern('Lle', (Nucleotide.A, Nucleotide.U, Nucleotide.U | Nucleotide.C | Nucleotide.A))
VAL = CodonPattern('VAL', (Nucleotide.G, Nucleotide.U, ALL_NUCLEOTIDES))
SER = CodonPattern('Ser', (Nucleotide.U, Nucleotide.C, ALL_NUCLEOTIDES),
            (Nucleotide.A, Nucleotide.G, Nucleotide.U | Nucleotide.C))
PRO = CodonPattern('Pro', (Nucleotide.C, Nucleotide.C, ALL_NUCLEOTIDES))
THR = CodonPattern('Thr', (Nucleotide.A, Nucleotide.C, ALL_NUCLEOTIDES))
ALA = CodonPattern('Ala', (Nucleotide.G, Nucleotide.C, ALL_NUCLEOTIDES))
TYR = CodonPattern('Tyr', (Nucleotide.U, Nucleotide.A, Nucleotide.U | Nucleotide.C))
HIS = CodonPattern('His', (Nucleotide.C, Nucleotide.A, Nucleotide.U | Nucleotide.C))
GLN = CodonPattern('Gln', (Nucleotide.C, Nucleotide.A, Nucleotide.A | Nucleotide.G))
ASN = CodonPattern('Asn', (Nucleotide.A, Nucleotide.A, Nucleotide.U | Nucleotide.C))
LYS = CodonPattern('Lys', (Nucleotide.A, Nucleotide.A, Nucleotide.A | Nucleotide.G))
ASP = CodonPattern('Asp', (Nucleotide.G, Nucleotide.A, Nucleotide.U | Nucleotide.C))
GLU = CodonPattern('Glu', (Nucleotide.G, Nucleotide.A, Nucleotide.A | Nucleotide.G))
CYS = CodonPattern('Cys', (Nucleotide.U, Nucleotide.G, Nucleotide.U | Nucleotide.C))
TRP = CodonPattern('Trp', (Nucleotide.U, Nucleotide.G, Nucleotide.G))

ARG = CodonPattern('Arg', (Nucleotide.C, Nucleotide.G, ALL_NUCLEOTIDES),
            (Nucleotide.A, Nucleotide.G, Nucleotide.A | Nucleotide.G))
GLY = CodonPattern('Gly', (Nucleotide.G, Nucleotide.G, ALL_NUCLEOTIDES))

ALL_ACIDS = [
    BEGIN_CODON, STOP_CODON, PHE, LEU, LLE,
    VAL, SER, PRO, THR, ALA, TYR, HIS, GLN, ASN,
    LYS, ASP, GLU, CYS, TRP
]