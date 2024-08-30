import re
from typing import Iterable
import RNA.splicing.poly_pyrimidine_tract_candidate as pptc

INSPECTION_SIZE = 42
BPS_PATTERN = re.compile(r'[CU][AUGC][CU]U[AG]A[CU]') # YNYURAY

# Score Constants
MAX_RATIO_SCORE = 8.0
MAX_LENGTH_SCORE = 1.0
BPS_FOUND_BONUS = 1.0

AVERAGE_INTRON_SIZE = 700
MIN_INTRON_SIZE = 50

THREE_PRIME_END_MARKER = re.compile(r'[UC]AG')

class IntronLengthRange:
    min: int
    max: int

    def __init__(self, min: int, max: int):
        self.min, self.max = min, max

    def len_range(self):
        return self.max - self.min + 1

class ThreePrimeSpliceSequenceCandidate:
    tract: pptc.PolyPyrimidineTractCandidate | None
    bps: re.Match[str] | None
    resulting_intron_size: int

    def __init__(self, suffixed_sequence: str):
        inspected_sequence = suffixed_sequence[-INSPECTION_SIZE:]
        self.resulting_intron_size = len(suffixed_sequence)

        if self.resulting_intron_size <= 0:
            self.tract = None
            self.bps = None
            return

        self._initialize_from_inspected_sequence(inspected_sequence)

    def _initialize_from_inspected_sequence(self, inspected_sequence: str):
        """Initializes the Poly Pyrimidine tract and the Branchpoint Sequence, if found

        Args:
            inspected_sequence (str): A sequence of an agreed size, in which the polypyrimidine tract
            ends in the third to last character (A constant when working with the 3' splice-site),
            and the Branchpoint Sequence (bps) may appear.
        """
        last_pyrimidine_index = len(inspected_sequence) - 2
        
        self.tract = pptc.PolyPyrimidineTractCandidate(inspected_sequence[:last_pyrimidine_index])
        self.bps = BPS_PATTERN.search(inspected_sequence[:INSPECTION_SIZE-len(self.tract.tract_string)])

    def get_bps_score(self) -> float:
        """Returns the constant BPS bonus if found, otherwise 0

        Returns:
            float: Score points
        """
        return BPS_FOUND_BONUS if self.bps else 0
    
    def get_length_score(self, intron_length_range: IntronLengthRange) -> float:
        """According to the range of possible deviations from the average intron size
        in humans (estimate) derived from some given 3' SS candidates, returns a
        normalized score, calculated by taking the distance from the average, mapping it to [0, 1]
        using the local deviation range, and normalizes that number according to the function
        f(x) = (1 - x)^3, to make sure that:
            * Very big deviations give very small scores
            * Very small deviations give very big scores
            * Average deviations give average+ scores

        Args:
            intron_length_range (IntronLengthRange): The smallest and biggest deviations from the average, in the 
            current inspected intron candidates

        Returns:
            float: A score for this length deviation, from [0, MAX_LENGTH_SCORE]
        """
        delta = self.delta_from_average_resulting_intron_size()

        # In [0, 1], because of the way we generated
        average_intron_size_ratio = (delta - intron_length_range.min) / intron_length_range.len_range()

        average_intron_size_ratio = ThreePrimeSpliceSequenceCandidate._normalize_length_score_mutliplier(
            average_intron_size_ratio)

        return MAX_LENGTH_SCORE * average_intron_size_ratio

    @staticmethod
    def _normalize_length_score_mutliplier(ratio):
        """Normalizes with bias to average ratios"""

        return (1 - ratio) ** 3

    def is_valid(self):
        """Whether the tract is valid and the resulting intron is sufficiently long"""
        return self.tract and self.tract.is_valid() and self.resulting_intron_size > MIN_INTRON_SIZE

    def score(self, intron_length_range: int):
        """Aggregates a total score according to the length, poly-pyrimidine-tract richness, and the existence of a BPS"""
        score = (self.get_bps_score()
                + self.tract.score(MAX_RATIO_SCORE)
                + self.get_length_score(intron_length_range))
    
        return self.tract.get_multiplier() * score

    def delta_from_average_resulting_intron_size(self) -> int:
        return abs(AVERAGE_INTRON_SIZE - self.resulting_intron_size)

    @staticmethod
    def find_intron_length_range(ss_candiates: list['ThreePrimeSpliceSequenceCandidate']) -> IntronLengthRange:
        """Returns the smallest and largest deviations in derived intron sizes from a given list of SS candidates"""
        all_intron_size_deltas: list[int] = list(map(
            ThreePrimeSpliceSequenceCandidate.delta_from_average_resulting_intron_size,
            ss_candiates))
        
        max_intron_size_delta: int = max(all_intron_size_deltas)
        min_intron_size_delta: int = min(all_intron_size_deltas)
        
        assert min_intron_size_delta <= max_intron_size_delta

        return IntronLengthRange(min_intron_size_delta, max_intron_size_delta)
    
    @staticmethod
    def get_all_candidates(intron_prefixed_sequence: str) -> Iterable['ThreePrimeSpliceSequenceCandidate']:
        for splice_end_site in THREE_PRIME_END_MARKER.finditer(intron_prefixed_sequence):
            candidate = ThreePrimeSpliceSequenceCandidate(intron_prefixed_sequence[:splice_end_site.span()[1]])
            
            if candidate.is_valid():
                yield candidate