from RNA.codon_reader import CodonReader
from RNA.amino_acid_codons import ALL_ACIDS

reader = CodonReader(ALL_ACIDS)

def swap_chars(string: str, a: str, b: str):
    return string.replace(a, '|').replace(b, a).replace('|', b)

string = 'AUGAGAAGAUUAUUGUCUUCCUGAUGGUGA'
print(string)

acid_chain = reader.translate_string(string)

print(list(acid_chain))