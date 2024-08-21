from RNA.codon_pattern import CodonPattern
from RNA.nucleotide import Nucleotide

# UAA | UAG | UGA - A codon signaling the termination of construction and release of polypeptide strand
STOP_CODON = CodonPattern('Stop Transcription', (Nucleotide.U, Nucleotide.A, Nucleotide.A | Nucleotide.G),
                   (Nucleotide.U, Nucleotide.G, Nucleotide.A))

# AUG - A codon signaling the beginning of construction of polypeptide strand
BEGIN_CODON = CodonPattern('Begin Transcription', (Nucleotide.A, Nucleotide.U, Nucleotide.G))