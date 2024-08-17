import re
from typing import Iterable
from RNA.nucleotide import to_anti_codon, NucleotideTriplet

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
                    for first in match[0]
                    for second in match[1]
                    for third in match[2]
            )

    def anti_codon(self):
        return CodonPattern(f'Anti({self.name})', *[
                to_anti_codon(match)
                for match in self.matches
            ])