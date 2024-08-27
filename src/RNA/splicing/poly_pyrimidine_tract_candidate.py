MAX_LENGTH = 21
MIN_LENGTH = 15
PYRIMIDINE_RATIO_THRESHOLD = .61
PYRIMIDINE_NUCLEOTIDES = ['C', 'U']
KNOWN_POLYPYRIMIDINE_TRACTS = ['CUCUGCGCGGCACGUCCUGGC']

class PolyPyrimidineTractCandidate:
    three_prime_ss_candidate: str
    tract_string: str
    ratio: float

    def __init__(self, three_prime_ss_candidate):
        self.three_prime_ss_candidate = three_prime_ss_candidate

        max_ratio = .0
        max_sequence = ''
        for size in range(MIN_LENGTH, MAX_LENGTH + 1):
            cur_sequence = three_prime_ss_candidate[-size:]

            ratio = PolyPyrimidineTractCandidate.calculate_ratio(cur_sequence)
            # print(f'{cur_sequence=} {len(cur_sequence)=} {ratio=}')
            
            if ratio > max_ratio:
                max_sequence, max_ratio = cur_sequence, ratio

        self.tract_string = max_sequence
        self.ratio = ratio

    @staticmethod
    def calculate_ratio(sequence: str):
        count = 0
        for c in sequence:
            count += int(c in PYRIMIDINE_NUCLEOTIDES)

        return count / len(sequence)

    def is_valid(self):
        return self.ratio >= PYRIMIDINE_RATIO_THRESHOLD
    
    def score(self, max_score: float):
        return (self.ratio ** 4) * max_score
    
    def get_multiplier(self) -> float:
        if self.tract_string in KNOWN_POLYPYRIMIDINE_TRACTS:
            return 2

        return 1