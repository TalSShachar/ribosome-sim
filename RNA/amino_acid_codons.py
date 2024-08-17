from RNA.codon import Codon
from RNA.nucleotide import Nucleotide, ALL as ALL_NUCLEOTIDES

PHE = Codon((Nucleotide.U, Nucleotide.U, Nucleotide.U | Nucleotide.C))
LEU = Codon((Nucleotide.U, Nucleotide.U, Nucleotide.A | Nucleotide.G),
            (Nucleotide.C, Nucleotide.U, ALL_NUCLEOTIDES))
LLE = Codon((Nucleotide.A, Nucleotide.U, Nucleotide.U | Nucleotide.C | Nucleotide.A))
MET = Codon((Nucleotide.A, Nucleotide.U, Nucleotide.G))
VAL = Codon((Nucleotide.G, Nucleotide.U, ALL_NUCLEOTIDES))
SER = Codon((Nucleotide.U, Nucleotide.C, ALL_NUCLEOTIDES),
            (Nucleotide.A, Nucleotide.G, Nucleotide.U | Nucleotide.C))
PRO = Codon((Nucleotide.C, Nucleotide.C, ALL_NUCLEOTIDES))
THR = Codon((Nucleotide.A, Nucleotide.C, ALL_NUCLEOTIDES))
ALA = Codon((Nucleotide.G, Nucleotide.C, ALL_NUCLEOTIDES))
TYR = Codon((Nucleotide.U, Nucleotide.A, Nucleotide.U | Nucleotide.C))
HIS = Codon((Nucleotide.C, Nucleotide.A, Nucleotide.U | Nucleotide.C))
GLN = Codon((Nucleotide.C, Nucleotide.A, Nucleotide.A | Nucleotide.G))
ASN = Codon((Nucleotide.A, Nucleotide.A, Nucleotide.U | Nucleotide.C))
LYS = Codon((Nucleotide.A, Nucleotide.A, Nucleotide.A | Nucleotide.G))
ASP = Codon((Nucleotide.G, Nucleotide.A, Nucleotide.U | Nucleotide.C))
GLU = Codon((Nucleotide.G, Nucleotide.A, Nucleotide.A | Nucleotide.G))
CYS = Codon((Nucleotide.U, Nucleotide.G, Nucleotide.U | Nucleotide.C))
TRP = Codon((Nucleotide.U, Nucleotide.G, Nucleotide.G))

ARG = Codon((Nucleotide.C, Nucleotide.G, ALL_NUCLEOTIDES),
            (Nucleotide.A, Nucleotide.G, Nucleotide.A | Nucleotide.G))
GLY = Codon((Nucleotide.G, Nucleotide.G, ALL_NUCLEOTIDES))