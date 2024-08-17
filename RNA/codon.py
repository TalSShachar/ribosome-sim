import re
from RNA.nucleotide import Nucleotide

class Codon:
    matches: set[tuple[Nucleotide, Nucleotide, Nucleotide]]
    pattern: re.Pattern
    pattern_string: str

    def __init__(self, *matches: list[tuple[Nucleotide, Nucleotide, Nucleotide]]):
        self.matches = set(matches)
        self.pattern_string = '|'.join([
            ''.join([
                n.name
                    if len(n) == 1
                    else '[' + ''.join([flag.name for flag in n]) + ']'
                for n in match
            ]) for match in matches
        ])
        self.pattern = re.compile(self.pattern_string)

    def __str__(self) -> str:
        return self.pattern_string
    
    def ismatch(self, codon: str | tuple[Nucleotide, Nucleotide, Nucleotide]) -> bool:
        if isinstance(codon, str):
            return bool(self.pattern.match(codon))
        
        return codon in self.matches