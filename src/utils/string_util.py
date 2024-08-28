from typing import Iterable

def chunk_string(string, length) -> Iterable[str]:
    """
    A utility method, takes in a string and the length of the desired chunks,
    And generates chunks of that length
    """
    assert len(string) % length == 0, \
        f'Tried to chunk a string of length {len(string)} into {length} char chunks'

    return (string[i:i + length] for i in range(0, len(string), length))