from .codon_pattern import CodonPattern
from .nucleotide import Nucleotide

# UAA | UAG | UGA
STOP_CODON = CodonPattern('Stop Transcription', (Nucleotide.U, Nucleotide.A, Nucleotide.A | Nucleotide.G),
                   (Nucleotide.U, Nucleotide.G, Nucleotide.A))

BEGIN_CODON = CodonPattern('Begin Transcription', (Nucleotide.A, Nucleotide.U, Nucleotide.G))