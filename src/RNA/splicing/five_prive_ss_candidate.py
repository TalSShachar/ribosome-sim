import re
from typing import Union

# According to the consensus sequence MAG/GURAGU, where
# M is A or C, and R is A or G
FIVE_PRIME_SITE_REGEX = re.compile(r'([AC]AG(G?))(GU[AG]AGU|GUGAGC|GUGGGC)')

class FivePrimeSpliceSiteCandidate:
    sequence: str
    intron_start: int

    def __init__(self, sequence: str, intron_start: int):
        self.intron_start = intron_start
        self.sequence = sequence

    @staticmethod
    def find(sequence: str) -> Union['FivePrimeSpliceSiteCandidate', None]:
        if match := FIVE_PRIME_SITE_REGEX.search(sequence):
            return FivePrimeSpliceSiteCandidate(sequence, match.span()[0] + len(match.group(1)))

        return None
    
    def get_since_intron(self) -> str:
        return self.sequence[self.intron_start:]