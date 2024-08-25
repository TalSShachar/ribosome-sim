import re
from typing import Iterable
from .nucleotide import NucleotideTriplet

ANTI_CODON_PATTERN = re.compile(r'^Anti\((.*)\)$')

class CodonPattern:
    matches: set[NucleotideTriplet]
    name: str

    def __init__(self, name, *matches: list[NucleotideTriplet]):
        self.name = name
        self.matches = set(matches)

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return str(self)

    def explicit_matches(self) -> Iterable[NucleotideTriplet]:
        return (
            (first, second, third) 
                for match in self.matches
                    for first in match[0] # Possibilities for first nucleotide
                    for second in match[1] # Possibilities for secon nucleotide
                    for third in match[2] # Possibilities for third nucleotide
            )