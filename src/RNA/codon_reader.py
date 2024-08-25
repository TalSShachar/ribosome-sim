from typing import Iterable, Iterator
from .control_codons import STOP_CODON
from .codon_pattern import CodonPattern
from .nucleotide import Nucleotide, NucleotideTriplet, to_anti_codon

CODON_SIZE = 3
NUCLEOTIDE_TYPES = 4
ALL_POSSIBLE_CODONS = NUCLEOTIDE_TYPES ** CODON_SIZE

# Map to indexes to get base4 digits in arbitrary order
NUCLEOTIDE_TO_INDEX = {
    Nucleotide.A: 0,
    Nucleotide.G: 1,
    Nucleotide.C: 2,
    Nucleotide.U: 3,
}

class CodonReader:
    map: list[CodonPattern]

    def __init__(self, recognized_codons: Iterable[CodonPattern]):
        self.map = [None] * ALL_POSSIBLE_CODONS

        # Fill in map
        for codon in recognized_codons:
            for explicit_match in codon.explicit_matches():
                index = CodonReader._calculate_index(explicit_match)

                assert self.map[index] is None, f'Index {index} for triplet {explicit_match} is already taken by codec {self.map[index].name}'

                self.map[index] = codon

    @staticmethod
    def _calculate_index(triplet: NucleotideTriplet):
        first, second, third = map(lambda n: NUCLEOTIDE_TO_INDEX[n], triplet)

        # Calculate in base 4 for 3 digits
        return (
            NUCLEOTIDE_TYPES * (
                (NUCLEOTIDE_TYPES * first) + second)
            ) + third

    def translate(self, anti_codon: str) -> CodonPattern | None:
        triplet = tuple([Nucleotide[n.name] for n in to_anti_codon(anti_codon)])

        assert len(triplet) == CODON_SIZE

        return self.map[self._calculate_index(triplet)]
    
    def translate_chain(self, chain: Iterator[NucleotideTriplet]) -> Iterator[CodonPattern]:
        for anti_codon in chain:
            acid = self.translate(anti_codon)

            if not acid:
                raise ValueError(f'Invalid anti codon {anti_codon=}')

            if acid.name == STOP_CODON.name:
                break

            yield acid
        else:
            # Will execute only in case the break statement didn't happen
            raise ValueError('Invalid chain - reached end without stop codon')

    def translate_string(self, string: str):
        chunks = CodonReader._string_chunk(string.upper(), CODON_SIZE)

        chain = (
            (Nucleotide[chunk[0]], Nucleotide[chunk[1]], Nucleotide[chunk[2]])
            for chunk in chunks
        )
        
        return self.translate_chain(chain)

    @staticmethod
    def _string_chunk(string, length) -> Iterable[str]:
        if len(string) % length == 0:
            return (string[i:i + length] for i in range(0, len(string), length))

        raise ValueError(f'Tried to chunk a string of length {len(string)} into {length} char chunks')
