import re
from typing import Iterable
from .nucleotide import NucleotideTriplet

# Regex fun
ANTI_CODON_PATTERN = re.compile(r'^Anti\((.*)\)$')

class CodonPattern:
    """
    A class used to match nucleotide triplets. Corresponds to a name, such as an amino acid
    or a broaded term such as a stop-codon.
    """

    _matches: set[NucleotideTriplet]
    name: str

    def __init__(self, abbr: str, name: str, *matches: tuple[NucleotideTriplet]):
        """Creates a codon pattern instances matching the matches given

        Args:
            name (str): The name of the codon match (An amino acid, a control command)
            *matches (list[NucleotideTriplet]): A variadic argument tuple for the match patterns of nucleotide triplets
        """
        self.abbr = abbr
        self.name = name
        self._matches = set(matches)

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return str(self)

    def explicit_matches(self) -> Iterable[NucleotideTriplet]:
        """Enumerates over all explicit matches of the nucleotide triplet matches and yields them

        Returns:
            Iterable[NucleotideTriplet]: A generator yielding all possible explicit concrete matches for this codon pattern
        """
        return (
            (first, second, third) 
                for match in self._matches
                    for first in match[0] # Possibilities for first nucleotide
                    for second in match[1] # Possibilities for secon nucleotide
                    for third in match[2] # Possibilities for third nucleotide
            )