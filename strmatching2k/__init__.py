"""Python port of the recovered StrMatching2k matching routines.

Returned scores are VBA Single values represented exactly in Python floats.
The default text comparison uses Unicode casefold, not Windows Jet collation.
"""
from ._generated import FUNCTIONS
from ._runtime import Array, Cell, Context, EMPTY, chars

__all__ = ['is_similar', 'name_similarity', 'double_metaphone', 'bigram',
           'lev_dist', 'dice', 'lcs', 'str_replace', 'get_last_chr_pos', 'EMPTY']


def _context(text_key):
    return Context(FUNCTIONS, text_key=text_key)


def _array(values, padding=False):
    if isinstance(values, Array):
        return values
    items = chars(values) if isinstance(values, str) else list(values)
    if padding:
        items.append(EMPTY)
    result = Array([(0, len(items) - 1)])
    for i, item in enumerate(items):
        result.set([i], item)
    return result


def is_similar(reference, candidate, algorithm='', *, text_key=str.casefold):
    """Return the recovered IsSimilar score; None represents VBA Null.

    algorithm: '', 'Dice', 'Lev', 'SSLCS', or 'DblMetaPh'. 'Lev' returns the
    original raw edit distance; 'SSLCS' and 'DblMetaPh' return raw LCS lengths.
    Access form writes in DblMetaPh mode are omitted; only the score is returned.
    """
    for value in (reference, candidate):
        if value is not None and not isinstance(value, str):
            raise TypeError('is_similar inputs must be strings or None')
    if not isinstance(algorithm, str):
        raise TypeError('algorithm must be a string')
    return float(_context(text_key).call('issimilar', [reference, candidate, algorithm]))


def name_similarity(reference, candidate, *, text_key=str.casefold):
    """Run the recovered NameSimilarity routine using its original name rules."""
    return float(_context(text_key).call('namesimilarity', [reference, candidate]))


def double_metaphone(word, *, text_key=str.casefold):
    """Return (primary, alternate) codes from the recovered implementation."""
    primary, alternate = Cell(), Cell()
    _context(text_key).call('doublemetaphone', [_array(word, padding=isinstance(word, str)), primary, alternate])
    return ('' if primary.value is EMPTY else primary.value,
            '' if alternate.value is EMPTY else alternate.value)


def bigram(word, *, text_key=str.casefold):
    """Return the original padded bigram array, including its final EMPTY slot."""
    output = Cell()
    _context(text_key).call('bigram', [word, output])
    return [output.value.get(i) for i in range(output.value.bounds[0][1] + 1)]


def lev_dist(first, second, *, text_key=str.casefold):
    """Original transposition-aware distance; string inputs are padded as in IsSimilar."""
    return int(_context(text_key).call('levdist', [_array(first, isinstance(first, str)), _array(second, isinstance(second, str))]))


def dice(first, second, dmph=False, *, text_key=str.casefold):
    """Pairwise bigram score, with original two-decimal formatting and optional cap."""
    first = bigram(first, text_key=text_key) if isinstance(first, str) else first
    second = bigram(second, text_key=text_key) if isinstance(second, str) else second
    return float(_context(text_key).call('dice', [_array(first), _array(second), dmph]))


def lcs(first, second, algorithm='', *, text_key=str.casefold):
    """Normalized LCS, or raw length for 'SSLCS'/'Dmph', as in the original."""
    return float(_context(text_key).call('lcs', [_array(first, isinstance(first, str)),
                                               _array(second, isinstance(second, str)), algorithm]))


def str_replace(text, search, replacement, start=0, count=0, *, text_key=str.casefold):
    """Recovered StrReplace with case-insensitive comparison and VBA start/count rules."""
    return _context(text_key).call('strreplace', [text, search, replacement, start, count])


def get_last_chr_pos(text, char, *, text_key=str.casefold):
    """Return a one-based position, or zero when absent/Null."""
    return int(_context(text_key).call('getlastchrpos', [text, char]))
