import re
from RNA.nucleotide import Nucleotide, to_anti_codon

class CodonPattern:
    matches: set[tuple[Nucleotide, Nucleotide, Nucleotide]]
    pattern: re.Pattern
    pattern_string: str
    name: str

    def __init__(self, name, *matches: list[tuple[Nucleotide, Nucleotide, Nucleotide]]):
        self.name = name
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
    
    def anti_codon(self) -> CodonPattern:
        return (f'Anti({self.name})', *[
                to_anti_codon(match)
                for match in self.matches
            ])