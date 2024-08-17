from typing import Iterator
from RNA.amino_acid_codons import ALL_ACIDS
from RNA.control_codons import BEGIN_CODON, STOP_CODON
from RNA.codon_pattern import CodonPattern
from RNA.nucleotide import Nucleotide, to_anti_codon

CODON_SIZE = 3

class CodonReader:
    def __init__(self):
        pass

    def translate(_self, anti_codon: str) -> CodonPattern | None:
        deantified_codon = ''.join([n.name for n in to_anti_codon(anti_codon)])
        print(f'Parsing codon {deantified_codon}')

        for acid in ALL_ACIDS:
            if acid.ismatch(deantified_codon):
                return acid
        return None
    
    def translate_chain(self, chain: Iterator[tuple[Nucleotide, Nucleotide, Nucleotide]]) -> Iterator[CodonPattern]:
        reached_end_codon = False
        for anti_codon in chain:
            acid = self.translate(anti_codon)

            if not acid:
                raise ValueError(f'Invalid anti codon {anti_codon=}')

            if acid.name == STOP_CODON.name:
                reached_end_codon = True
                break

            yield acid

        if not reached_end_codon:
            raise ValueError('Invalid chain - reached end without stop codon')

    def translate_string(self, string: str):
        chunks = CodonReader._string_chunk(string.upper(), CODON_SIZE)

        print(f'{chunks=}')

        chain = [
            (Nucleotide[chunk[0]], Nucleotide[chunk[1]], Nucleotide[chunk[2]])
            for chunk in chunks
        ]
        
        return self.translate_chain(chain)

    @staticmethod
    def _string_chunk(string, length):
        if len(string) % length == 0:
            return [string[i:i + length] for i in range(0, len(string), length)]

        raise ValueError(f'Tried to chunk a string of length {len(string)} into {length} char chunks')
