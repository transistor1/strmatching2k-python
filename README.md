# StrMatching2k Python port

This port refers to the 2007 article [Fuzzy Matching Demo in Access](https://web.archive.org/web/20071014004910/http://www.codeguru.com/vb/gen/vb_database/microsoftaccess/article.php/c13137/), which is the source context for the recovered routines and behavior documented below.

Python 3.10 or newer. No Access installation, VBA files, decompiler environment,
network access or third-party runtime packages are required.

Keep the `strmatching2k` folder beside your script, or install this directory with
`python -m pip install .`. The package itself has no runtime dependencies.

```python
from strmatching2k import is_similar

score = is_similar("PAIN RELIEF", "PAINT REMOVER")
print(score)                 # 0.7452778220176697
print(f"{score:.6f}")        # 0.745278
```

The result is an IEEE-754 Single value represented in a Python float. Do not
round the return value unless you want display rounding. Single assignments
and relevant intermediate arithmetic are rounded to 32 bits as in the recovered
VBA; calculations explicitly promoted with CDbl remain double precision.

```python
is_similar("Smith", "Smyth")                 # combined score
is_similar("Smith", "Smyth", "Dice")         # original bigram score
is_similar("Smith", "Smyth", "Lev")          # raw edit distance: 1.0
is_similar("Smith", "Smyth", "SSLCS")        # raw LCS length: 4.0
is_similar("Smith", "Smyth", "DblMetaPh")    # phonetic LCS length: 3.0
is_similar(None, "Smith")                    # VBA Null input: 0.0
```

Modes follow the original routines: they are not all normalized similarities.
The original repeated-bigram counting can exceed 1; this port preserves it.
The original punctuation/hyphen preprocessing, array padding, early exits and
score formatting are preserved rather than replaced with a standard library's
Dice, edit-distance or Double Metaphone implementation.

Other public helpers are `bigram`, `dice`, `lev_dist`, `lcs`, `double_metaphone`,
`str_replace`, `get_last_chr_pos`, and `name_similarity`. String inputs to the
distance/LCS helpers receive the original IsSimilar character-array padding.
`bigram` returns the padded array including its final `EMPTY` sentinel;
`EMPTY` is different from `None` (VBA Null). `double_metaphone("Smith")` returns
`("SM0", "XMT")`; an unavailable alternate is returned as an empty string.
`name_similarity` expects the recovered `last~first~middle` representation,
for example `name_similarity("Smith~John~", "Smith~Jon~")`.

## Validation and limits

All five manually supplied Access results match at the precision provided:

| Reference | Candidate | Access / Python, six decimals |
|---|---|---|
| OMEPRA TEST | GENERIC OMEPRA TEST | 0.768889 |
| LEFLUNOMIDE + 12 spaces + 20 MG | LEFLUNOMIDE | 0.734017 |
| FUROSEMIDE + 13 spaces + 10 MG/M | FUROSEMIDE | 0.678803 |
| ALLERGY STOP | ALLERGY-STOP | 0.949583 |
| PAIN RELIEF | PAINT REMOVER | 0.745278 |

Exact strings (including spaces) live in `tests/reference_cases.json`. This
validates six displayed decimals, not bit-for-bit equivalence across all inputs.
There are 24 tests, including these cases, helper/edge cases, Single precision,
Null/Empty handling, ByRef updates, concurrent calls, and 320 small input/mode
combinations. A separate smoke check exercised 48 phonetic names without errors.
Only the five user-supplied cases are an external Access numerical oracle; other
tests exercise runtime semantics, known simple results and internal consistency.

Text comparison defaults to Unicode `str.casefold`, which approximates
case-insensitive English database comparison. It does **not** reproduce every
Jet/Windows locale or accented-character rule. A `text_key=` callable can override
comparison/search folding. Like character classes use Python's case-insensitive
regular expressions; they do not implement locale-specific character ranges.
Format masks `0.00` and `#.##` use decimal half-up formatting after 15-significant
digit rendering; midpoint behavior across Windows versions has not yet been
checked against Access. CInt/CLng use ties-to-even. UTF-16 positions are retained
for Len, Mid, Left and ordinary InStr searches; length-changing text folds remain
a collation limitation. These are the main areas for broader reference testing.

Each public call gets its own module-variable context, preserving shared state
between helpers within a call while avoiding cross-call/thread interference.
The phonetic helper's alternate output therefore reflects a fresh module state;
the original Access module's alternate flag can persist between separate calls.
Access UI writes in the explicit DblMetaPh mode are omitted. Numeric processing
continues and returns the score without requiring the original comparison form.
The main `is_similar` API accepts strings or None, rather than arbitrary COM
Variants. VBA-style overflow and invalid-array errors are exposed as ValueError
subclasses. The implementation retains the original quadratic array algorithms;
it has not been optimized for very long strings or large batches.

## Run and compare

```sh
python -m strmatching2k "PAIN RELIEF" "PAINT REMOVER"
python -m strmatching2k --check tests/reference_cases.json
python -m unittest discover -s tests -v
```

For a stronger comparison, optionally import
`validation/ExportPythonReferenceCases.bas` into the database containing the
original or reconstructed IsSimilar. Run `ExportPythonParityCases` in the VBA
Immediate window. It writes `python-reference.csv` beside the database with 56
input/mode cases and each result's actual Single bits. Copy that CSV to the
Python machine and run:

```sh
python -m strmatching2k --check python-reference.csv
```

When `single_hex` is present, the checker compares the exact 32-bit values.
The exporter has been supplied for use in Access; it has not been run here.

## Implementation and provenance

`scripts/build_python_port.py` translates the 18 consolidated VBA procedures
into ordinary Python functions and control-flow blocks in `_generated.py`.
This retains source statements as comments for review. `_runtime.py` provides
the specific array, Variant, ByRef, numeric and string behavior those functions
need; it is not a general VBA interpreter. Python performs all runtime work;
there is no runtime parsing of VBA or dependency on the original MDE.
`strmatching2k/provenance.json` records the VBA source hashes.

The port includes all six AlgorithmSuite routines, seven DblMetaPhone routines,
and five Globals helpers. It does not include the original forms or the ten
unrecovered database/import helpers. Regeneration from the repository is:

```sh
python scripts/build_python_port.py
```

Reference material used when checking the compatibility layer:
[Microsoft VBA Format documentation](https://learn.microsoft.com/en-us/office/vba/language/reference/user-interface-help/format-function-visual-basic-for-applications),
[Microsoft VBA language specification](https://download.microsoft.com/download/0/a/6/0a6f7755-9af5-448b-907d-13985accf53e/%5Bms-vbal%5D.pdf),
and [Wine's Automation formatter implementation](https://github.com/wine-mirror/wine/blob/master/dlls/oleaut32/varformat.c).
Wine's numeric formatting is supporting implementation evidence, not proof of
identical behavior on the user's Windows runtime.
