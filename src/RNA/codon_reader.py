from typing import Callable, Iterable, Iterator

from RNA.splicing.spliceosome import Exon
from utils.string_util import chunk_string
from .control_codons import STOP_CODON
from .codon_pattern import CodonPattern
from .nucleotide import Nucleotide, NucleotideTriplet

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

# A chemical, programatically artificial boundry
NONSENSE_MEDIATED_DECAY_IDENTIFICATION_THRESHOLD = 54

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
        chunks = chunk_string(string.upper(), CODON_SIZE)

        # A generator pattern for producing Nucleotide triplets out of 3-char strings
        chain: Iterator[NucleotideTriplet] = (
            (Nucleotide[chunk[0]], Nucleotide[chunk[1]], Nucleotide[chunk[2]])
            for chunk in chunks
        )
        
        return self.translate_chain(chain)

    def translate_exons(self, exons: list[Exon]):
        exon_indices = CodonReader.get_exon_indices(exons)

        joined_exons = ''.join([exon.code for exon in exons])
        first_methionine_index = joined_exons.find('AUG')
        mrna_from_methionine = joined_exons[first_methionine_index:]
        mrna_from_methionine = mrna_from_methionine[:-(len(mrna_from_methionine)%3)]

        index = first_methionine_index
        for acid in self.translate_string(mrna_from_methionine):
            if acid == STOP_CODON:
                distance = CodonReader.get_offset_within_current_middle_exon(index, exon_indices)
                if distance is None or distance < NONSENSE_MEDIATED_DECAY_IDENTIFICATION_THRESHOLD:
                    break

                raise ValueError(f'Codon sequence appears in index {index}, which is not in the last exon. Decaying polypeptide chain!')

            yield acid
            index += 3

    @staticmethod
    def get_exon_indices(exons: list[Exon]) -> list[int]:
        aggr_index = 0
        exon_indices: list[int] = []
        for exon in exons:
            exon_indices.append(aggr_index)
            aggr_index += len(exon.code)
        return exon_indices
    
    def get_offset_within_current_middle_exon(index, exon_indices: list[int]) -> int | None:
        last_index = CodonReader._get_last_index(exon_indices,
                                                 lambda exon_index: exon_index <= index)
        
        assert last_index >= 0

        # if Not a middle exon
        if last_index == len(exon_indices) - 1:
            return None
        
        return index - exon_indices[last_index]
        
    @staticmethod
    def _get_last_index(elements: list[int], predicate):
        last_index = -1
        for i, elem in enumerate(elements):
            if predicate(elem):
                last_index = i

        return last_index


    @staticmethod
    def translate_string_into_triplets(string: str):
        """
        Takes in an mRNA string, chunks it to 3-char chunks,
        Parses them as nucleotide-char triplets and returns it
        """
        chunks = chunk_string(string.upper(), CODON_SIZE)

        # A generator pattern for producing Nucleotide triplets out of 3-char strings
        chain = [
            (Nucleotide[chunk[0]], Nucleotide[chunk[1]], Nucleotide[chunk[2]])
            for chunk in chunks
        ]
        
        return chain
