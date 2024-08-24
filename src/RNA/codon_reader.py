from typing import Iterable, Iterator
from RNA.control_codons import STOP_CODON
from RNA.codon_pattern import CodonPattern
from RNA.nucleotide import Nucleotide, NucleotideTriplet

# Consants for calculating mapper array length
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

# Exon: contain genetic coding nucleotides
# Intron: don't contain any information about the genetic code

# DNA(TGAC) -> precursor mRNA -> mRNA(UGAC) -> Polypeptide chain

# CAGGUGAGU
# MAG/GURAGU
# M in [A, C]
# R in [A, G]

# Donor site - 5' splice site concensus sequence
# Acceptor site - 3' splice site concensus sequence

# Pyrimidine = [C, U]
# PolyPyrimidine = A lot of pyrimidines
#  [CU]AG

# PolyPyrimidine tract

class CodonReader:
    """
    Responsible for the ribosomes mRNA parsing logic. Receives a map of recognized codons and
    uses it to be able to parse an mRNA nucleotide codon chain.
    """

    _map: list[CodonPattern]

    def __init__(self, recognized_codons: Iterable[CodonPattern]):
        self._map = [None] * ALL_POSSIBLE_CODONS

        # Fill in map
        for codon in recognized_codons:
            # Flatten out nucleotide patterns to concrete nucleotide types
            for explicit_match in codon.explicit_matches():
                index = CodonReader._calculate_index(explicit_match)

                assert self._map[index] is None, \
                    f'Index {index} for triplet {explicit_match} is already taken by codec {self._map[index].name}'

                self._map[index] = codon

    @staticmethod
    def _calculate_index(triplet: NucleotideTriplet):
        """
        Calculates a position in a mapping array of size 4^3 (nucleotide types ^ codon length)
        for a given concrete nucleotide triplet
        """

        # Make sure the flag-count for each nucleotide is 1 (a single bit is active)
        assert all((len(n) == 1 for n in triplet)),\
            'Should be a triplet of concrete nucleotides'

        # Expand tuple of size 3 to 3 variables,
        # after mapping each nucleotide to its corresponding digit in base 4
        first, second, third = map(lambda n: NUCLEOTIDE_TO_INDEX[n], triplet)

        # Calculate in base 4 for 3 digits
        return (
            NUCLEOTIDE_TYPES * (
                (NUCLEOTIDE_TYPES * first) + second)
            ) + third

    def translate(self, codon: NucleotideTriplet) -> CodonPattern | None:
        """
        Translates a codon string to a CodonPattern variable 
        """
        assert len(codon) == CODON_SIZE

        return self._map[self._calculate_index(codon)]
    
    def translate_chain(self, chain: Iterator[NucleotideTriplet]) -> Iterator[CodonPattern]:
        """
        Takes in an Iterator of Nucleotide Triplets and,
        as a generator, outputs concrete codon patterns with the matching
        Amino acid name 
        """
        for codon in chain:
            acid = self.translate(codon)

            # If translating the codon failed
            if not acid:
                raise ValueError(f'Invalid codon {codon=}')

            # Termination codon, break translation
            if acid.name == STOP_CODON.name:
                yield acid
                break

            yield acid


    def translate_string(self, string: str):
        """
        Takes in an mRNA string, chunks it to 3-char chunks,
        Parses them as nucleotide-char triplets, and translates those triplets
        as a codon chain
        """
        chunks = CodonReader._string_chunk(string.upper(), CODON_SIZE)

        # A generator pattern for producing Nucleotide triplets out of 3-char strings
        chain: Iterator[NucleotideTriplet] = (
            (Nucleotide[chunk[0]], Nucleotide[chunk[1]], Nucleotide[chunk[2]])
            for chunk in chunks
        )

        return self.translate_chain(chain)

    @staticmethod
    def _string_chunk(string, length) -> Iterable[str]:
        """
        A utility method, takes in a string and the length of the desired chunks,
        And generates chunks of that length
        """
        assert len(string) % length == 0, \
            f'Tried to chunk a string of length {len(string)} into {length} char chunks'

        return (string[i:i + length] for i in range(0, len(string), length))
