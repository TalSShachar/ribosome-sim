from pprint import pprint
from RNA.splicing.three_prime_ss_candidate import ThreePrimeSpliceSequenceCandidate
from RNA.splicing.five_prive_ss_candidate import FivePrimeSpliceSiteCandidate

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

    def splice(self, sequence: str) -> list[Exon]:
        if len(sequence) == 0:
            return []

        five_prime_ss = FivePrimeSpliceSiteCandidate.find(sequence)

        if not five_prime_ss:
             return [Exon(sequence)]

        intron_prefixed_sequence = five_prime_ss.get_since_intron()

        most_probable_ss = Spliceosome.get_most_likely_splice_site(list(
            ThreePrimeSpliceSequenceCandidate.get_all_candidates(intron_prefixed_sequence)))

        next_exons = self.splice(intron_prefixed_sequence[most_probable_ss.resulting_intron_size:])
        
        assert next_exons

        return [Exon(sequence[:five_prime_ss.intron_start]), *next_exons]

    @staticmethod
    def get_most_likely_splice_site(possible_splice_sites: list[ThreePrimeSpliceSequenceCandidate]) -> ThreePrimeSpliceSequenceCandidate:
        return Spliceosome.rank_and_sort_possible_splice_sites(possible_splice_sites)[-1][0]

    @staticmethod
    def rank_and_sort_possible_splice_sites(possible_splice_sites: list[ThreePrimeSpliceSequenceCandidate]) \
            -> list[tuple[ThreePrimeSpliceSequenceCandidate, float]]:
        intron_len_range = ThreePrimeSpliceSequenceCandidate.find_intron_length_range(possible_splice_sites)

        sorted_list = sorted(
            map(lambda c: (c, ThreePrimeSpliceSequenceCandidate.score(c, intron_len_range)),
                filter(ThreePrimeSpliceSequenceCandidate.is_valid, possible_splice_sites)),
            key=lambda t: t[1]
            )

        return sorted_list