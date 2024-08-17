from RNA.codon_reader import CodonReader

reader = CodonReader()

def swap_chars(string, a, b):
    return string.replace(a, '|').replace(b, a).replace('|', b)

string = swap_chars(swap_chars('AUGUUAUUGUCUUCCUGAUGGUGA', 'A', 'U'),
                    'G', 'C')

print(string)

acid_chain = reader.translate_string(string)

print(list(acid_chain))

