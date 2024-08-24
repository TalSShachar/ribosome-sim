import re
from pprint import pprint
# According to the consensus sequence MAG/GURAGU, where
# M is A or C, and R is A or G
FIVE_PRIME_SITE_REGEX = re.compile(r'([AC]AG(G?))(GU[AG]AGU|GUGAGC|GUGGGC)')
THREE_PRIME_END_MARKER = re.compile(r'CAG')

PYRIMIDINE_NUCLEOTIDES = ['C', 'U']
KNOWN_POLYPYRIMIDINE_TRACTS = ['CUCUGCGCGGCACGUCCUGGC']

POLYPYRIMIDINE_TRACT_SUSPECTION_LENGTH = 21
POLYPYRIMIDINE_TRACT_SUSPECTION_THRESHOLD = .61
MINIMUM_INTRON_SIZE = 70
AVERAGE_INTRON_SIZE = 700 # 3000 bp

MAX_LENGTH_SCORE = 50
MAX_RATIO_SCORE = 250

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
    def _is_polypyrimidine_tract(sequence: str) -> bool | float:
        if not sequence:
            return False

        if len(sequence) < POLYPYRIMIDINE_TRACT_SUSPECTION_LENGTH:
            return False

        assert len(sequence) <= POLYPYRIMIDINE_TRACT_SUSPECTION_LENGTH

        count = 0
        for c in sequence:
            count += int(c in PYRIMIDINE_NUCLEOTIDES)

        ratio = count / len(sequence)

        # print(f'suspected_polypyrimidine_tract={sequence}/{sequence.replace('U', 'T')} {{{len(sequence)}}} {ratio=}')

        return ratio if ratio >= POLYPYRIMIDINE_TRACT_SUSPECTION_THRESHOLD else False
    
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
        possible_tracts = Spliceosome.get_all_possible_polypyrimidine_tracts(intron_prefixed_sequence)
        
        possible_tracts = Spliceosome.rank_and_sort_possible_tracts(list(possible_tracts))

        # pprint(possible_tracts)

        most_probable_tract = possible_tracts[-1]

        next_exon_junction_index = most_probable_tract[1].span()[0] + 3
    
        return self.splice(intron_prefixed_sequence[next_exon_junction_index:])
        
    @staticmethod
    def rank_and_sort_possible_tracts(possible_tracts):
        distance_to_average = lambda t: abs((AVERAGE_INTRON_SIZE - t[1].span()[0]))
        closest_length_to_average_intron_size = min(possible_tracts,
            key=distance_to_average)[1].span()[0]
        

        farthest_length_to_average_intron_size = max(possible_tracts,
            key=distance_to_average)[1].span()[0]
        
        length_range = abs(farthest_length_to_average_intron_size - closest_length_to_average_intron_size)
        # print(f'{closest_length_to_average_intron_size=} {farthest_length_to_average_intron_size=} {length_range=}')        
        
        get_length_score = lambda length: MAX_LENGTH_SCORE * (1 - (length  / length_range))
        get_ratio_score = lambda ratio: MAX_RATIO_SCORE * (ratio ** 4)


        filtered = list(filter(lambda t: t[1].span()[0] > MINIMUM_INTRON_SIZE, possible_tracts))

        get_overall_score = lambda t: \
            (2 if t[2] in KNOWN_POLYPYRIMIDINE_TRACTS else 1) \
                * (get_ratio_score(t[0]) + get_length_score(distance_to_average(t)))

        sorted_list = sorted(
            filtered,
            key=get_overall_score 
            )
        # for t in sorted_list:
        #     print(t, 'score is', get_ratio_score(t[0]) + get_length_score(distance_to_average(t)))
        return sorted_list
    
    @staticmethod
    def get_all_possible_polypyrimidine_tracts(intron_prefixed_sequence):
        for splice_end_site in THREE_PRIME_END_MARKER.finditer(intron_prefixed_sequence):
            suspected_polypyrimidine_tract = \
                intron_prefixed_sequence[splice_end_site.span()[0] + 1 - POLYPYRIMIDINE_TRACT_SUSPECTION_LENGTH:]\
                        [:POLYPYRIMIDINE_TRACT_SUSPECTION_LENGTH]
            

            if not (ratio := Spliceosome._is_polypyrimidine_tract(suspected_polypyrimidine_tract)):
                continue

            yield (ratio, splice_end_site, suspected_polypyrimidine_tract)