from RNA.codon_pattern import CodonPattern
from RNA.nucleotide import Nucleotide

# UAA | UAG | UGA
STOP_CODON = CodonPattern('Stop Transcription', (Nucleotide.U, Nucleotide.A, Nucleotide.A | Nucleotide.G),
                   (Nucleotide.U, Nucleotide.G, Nucleotide.A))

BEGIN_CODON = CodonPattern('Begin Transcription', (Nucleotide.U, Nucleotide.A, Nucleotide.G))