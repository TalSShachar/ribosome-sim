import re
from pprint import pprint
from types import NoneType
# According to the consensus sequence MAG/GURAGU, where
# M is A or C, and R is A or G
FIVE_PRIME_SITE_REGEX = re.compile(r'([AC]AG(G?))(GU[AG]AGU|GUGAGC|GUGGGC)')
THREE_PRIME_END_MARKER = re.compile(r'[CU]AG')
BPS_PATTERN = re.compile(r'[CU][AUGC][CU]U[AG]A[CU]')

PYRIMIDINE_NUCLEOTIDES = ['C', 'U']
KNOWN_POLYPYRIMIDINE_TRACTS = ['CUCUGCGCGGCACGUCCUGGC']

SUSPECTED_SPLICE_SITE_EXAMINATION_LENGTH = 40
POLYPYRIMIDINE_TRACT_SUSPECTION_LENGTH_MIN = 15
POLYPYRIMIDINE_TRACT_SUSPECTION_LENGTH_MAX = 21
POLYPYRIMIDINE_TRACT_SUSPECTION_THRESHOLD = .61
MINIMUM_INTRON_SIZE = 70
AVERAGE_INTRON_SIZE = 700

MAX_LENGTH_SCORE = 1
MAX_RATIO_SCORE = 5
BPS_FOUND_BONUS = 1

class Exon:
    code: str

    def __str__(self):
        return f'<{self.code}>'
    def __repr__(self):
        return f'<{self.code}>'

    def __init__(self, code: str):
        self.code = code

class Spliceosome:
    def __init__(self):
        pass

    @staticmethod
    def _maybe_find_polypyrimidine_tract(sequence: str) -> NoneType | tuple[float, str]:
        if not sequence:
            return None

        if len(sequence) < POLYPYRIMIDINE_TRACT_SUSPECTION_LENGTH_MIN:
            return None

        assert len(sequence) <= POLYPYRIMIDINE_TRACT_SUSPECTION_LENGTH_MAX

        # print(sequence, len(sequence))

        max_ratio = 0
        max_sequence = ''
        for size in range(POLYPYRIMIDINE_TRACT_SUSPECTION_LENGTH_MIN, POLYPYRIMIDINE_TRACT_SUSPECTION_LENGTH_MAX + 1):
            cur_sequence = sequence[-size:]

            ratio = Spliceosome.calculate_ratio(cur_sequence)
            # print(f'{cur_sequence=} {len(cur_sequence)=} {ratio=}')
            max_sequence, max_ratio = (cur_sequence, ratio) if ratio > max_ratio else (max_sequence, max_ratio)

        return (ratio, max_sequence) if ratio >= POLYPYRIMIDINE_TRACT_SUSPECTION_THRESHOLD else None
    
    @staticmethod
    def calculate_ratio(sequence: str):
        count = 0
        for c in sequence:
            count += int(c in PYRIMIDINE_NUCLEOTIDES)

        return count / len(sequence)


    def splice(self, sequence: str) -> list[Exon]:
        if len(sequence) == 0:
            return []

        if not (first_match := FIVE_PRIME_SITE_REGEX.search(sequence)):
             return [Exon(sequence)]

        intron_start_position = first_match.span()[0] + len(first_match.group(1))

        next_exons = self.blah(sequence[intron_start_position:])

        if not next_exons:
            return []
        
        return [Exon(sequence[:intron_start_position]), *next_exons]

    def blah(self, intron_prefixed_sequence: str):
        possible_tracts = Spliceosome.get_all_possible_splice_end_sites(intron_prefixed_sequence)
        
        possible_tracts = Spliceosome.rank_and_sort_possible_splice_sites(list(possible_tracts))

        most_probable_tract = possible_tracts[-1]

        next_exon_junction_index = most_probable_tract[1].span()[0] + 3
    
        return self.splice(intron_prefixed_sequence[next_exon_junction_index:])

    @staticmethod
    def rank_and_sort_possible_splice_sites(possible_splice_sites: list[float, re.Match, str, str]):
        distance_to_average = lambda t: abs((AVERAGE_INTRON_SIZE - t[1].span()[0]))
        closest_length_to_average_intron_size = min(possible_splice_sites,
            key=distance_to_average)[1].span()[0]
        

        farthest_length_to_average_intron_size = max(possible_splice_sites,
            key=distance_to_average)[1].span()[0]
        
        length_range = abs(farthest_length_to_average_intron_size - closest_length_to_average_intron_size)
        # print(f'{closest_length_to_average_intron_size=} {farthest_length_to_average_intron_size=} {length_range=}')        
        
        get_length_score = lambda length: MAX_LENGTH_SCORE * (1 - (length  / length_range))
        get_ratio_score = lambda ratio: MAX_RATIO_SCORE * (ratio ** 4)

        filtered = list(filter(lambda t: t[1].span()[0] > MINIMUM_INTRON_SIZE, possible_splice_sites))

        get_overall_score = lambda t: \
            (2 if t[2] in KNOWN_POLYPYRIMIDINE_TRACTS else 1) \
                * (get_ratio_score(t[0]) + get_length_score(distance_to_average(t)) + Spliceosome._get_bps_score(t[3], len(t[2])))

        sorted_list = sorted(
            filtered,
            key=get_overall_score 
            )
        # for t in sorted_list:
        #   print(t, 'score is', get_overall_score(t))
        return sorted_list
    
    @staticmethod
    def _get_bps_score(full_sequence, tract_postfix_length):
        if not BPS_PATTERN.search(full_sequence[:SUSPECTED_SPLICE_SITE_EXAMINATION_LENGTH-tract_postfix_length]):
            return 0
        
        return BPS_FOUND_BONUS

    @staticmethod
    def get_all_possible_splice_end_sites(intron_prefixed_sequence):
        for splice_end_site in THREE_PRIME_END_MARKER.finditer(intron_prefixed_sequence):
            last_pyrimidine_index = splice_end_site.span()[0] + 1
            suspected_polypyrimidine_tract = \
                intron_prefixed_sequence[last_pyrimidine_index - POLYPYRIMIDINE_TRACT_SUSPECTION_LENGTH_MAX:]\
                        [:POLYPYRIMIDINE_TRACT_SUSPECTION_LENGTH_MAX]
            

            if not (tract := Spliceosome._maybe_find_polypyrimidine_tract(suspected_polypyrimidine_tract)):
                continue

            ratio, tract_sequence = tract

            yield (
                ratio,
                splice_end_site,
                tract_sequence,
                intron_prefixed_sequence[last_pyrimidine_index - SUSPECTED_SPLICE_SITE_EXAMINATION_LENGTH:]\
                        [:SUSPECTED_SPLICE_SITE_EXAMINATION_LENGTH])