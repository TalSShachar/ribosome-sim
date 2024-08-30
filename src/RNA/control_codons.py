from .codon_pattern import CodonPattern
from .nucleotide import Nucleotide

# UAA | UAG | UGA - A codon signaling the termination of construction and release of polypeptide strand
STOP_CODON = CodonPattern('*', 'Stop Transcription', (Nucleotide.U, Nucleotide.A, Nucleotide.A | Nucleotide.G),
                   (Nucleotide.U, Nucleotide.G, Nucleotide.A))

# AUG - A codon signaling the beginning of construction of polypeptide strand
BEGIN_CODON = CodonPattern('M', 'Methionine', (Nucleotide.A, Nucleotide.U, Nucleotide.G))