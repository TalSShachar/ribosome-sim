from RNA.codon import Codon
from RNA.nucleotide import Nucleotide

# UAA | UAG | UGA
STOP_CODON = Codon((Nucleotide.U, Nucleotide.A, Nucleotide.A | Nucleotide.G),
                   (Nucleotide.U, Nucleotide.G, Nucleotide.A))

BEGIN_CODON = Codon((Nucleotide.U, Nucleotide.A, Nucleotide.G))