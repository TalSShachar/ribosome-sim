from typing import Iterator
from amino_acid_codons import ALL_ACIDS
from control_codons import BEGIN_CODON, STOP_CODON
from RNA.codon_pattern import CodonPattern
from nucleotide import Nucleotide, to_anti_codon

CODON_SIZE = 3

class CodonReader:
    def __init__(self):
        pass

    def translate(_self, anti_codon: str) -> CodonPattern | None:
        for acid in ALL_ACIDS:
            if not acid.matches(to_anti_codon(anti_codon)):
                continue

            return acid
        return None
    
    def translate_chain(self, chain: Iterator[tuple[Nucleotide, Nucleotide, Nucleotide]]) -> Iterator[CodonPattern]:
        for anti_codon in chain:
            acid = self.translate(anti_codon)

            if acid == STOP_CODON:
                break

            yield acid

        yield CodonPattern('Invalid Chain', ())

    def translate_string(self, string: str):
        chunks = CodonReader._string_chunk(string.upper(), CODON_SIZE)

        chain = [
            tuple(Nucleotide(chunk[0]), Nucleotide(chunk[1]), Nucleotide(chunk[2]))
            for chunk in chunks
        ]

        return self.translate_chain(chain)

    @staticmethod
    def _string_chunk(string, length):
        if len(string) % length == 0:
            return [string[i:i + length] for i in range(len(string), len(string) // length)]

        raise ValueError(f'Tried to chunk a string of length {len(string)} into {length} char chunks')
