from concurrent.futures import ThreadPoolExecutor
import hashlib
import itertools
import json
import math
from pathlib import Path
import struct
import subprocess
import sys
import tempfile
import unittest

from strmatching2k import (EMPTY, bigram, dice, double_metaphone, get_last_chr_pos,
                          is_similar, lcs, lev_dist, name_similarity, str_replace)
from strmatching2k._runtime import (Array, Cell, Context, Integer, Long, Single,
                                    VBAError)
from strmatching2k._generated import FUNCTIONS

ROOT = Path(__file__).resolve().parents[1]


class AccessReferenceTests(unittest.TestCase):
    def test_user_supplied_access_outputs(self):
        cases = json.loads((Path(__file__).with_name('reference_cases.json')).read_text())
        for case in cases:
            with self.subTest(reference=case['reference'], candidate=case['candidate']):
                self.assertEqual(format(is_similar(case['reference'], case['candidate']), '.6f'), case['expected_6dp'])

    def test_output_is_exactly_representable_as_single(self):
        value = is_similar('John', 'Jon')
        self.assertEqual(struct.unpack('<f', struct.pack('<f', value))[0], value)
        self.assertNotEqual(value, round(value, 6))


class MatchingTests(unittest.TestCase):
    def test_null_and_default_empty_inputs(self):
        self.assertEqual(is_similar(None, 'John'), 0)
        self.assertEqual(is_similar('John', None), 0)
        self.assertEqual(is_similar(None, None), 0)
        self.assertEqual(is_similar('', ''), 1)
        self.assertEqual(is_similar('', 'John'), 0)
        self.assertEqual(is_similar(' ', ''), 0)

    def test_comparison_and_preprocessing(self):
        self.assertEqual(is_similar('JOHN', 'john'), 1)
        self.assertEqual(is_similar('J. Smith', 'J Smith'), 1)
        self.assertEqual(is_similar(' A/B ', 'AB'), 1)
        # The recovered hyphen path duplicates the suffix before removing '-'.
        self.assertEqual(is_similar('A-B', 'AB'), is_similar('ABB', 'AB'))

    def test_modes_preserve_raw_outputs(self):
        self.assertEqual(is_similar('Smith', 'Smyth', 'Lev'), 1)
        self.assertEqual(is_similar('Smith', 'Smyth', 'SSLCS'), 4)
        self.assertEqual(is_similar('Smith', 'Smyth', 'DblMetaPh'), 3)
        self.assertEqual(is_similar('Smith', 'Smyth', 'Dice'), float(Single(.67)))
        self.assertEqual(is_similar('Smith', 'Smyth', 'dice'), float(Single(.67)))

    def test_name_similarity_requires_original_delimiters(self):
        self.assertEqual(name_similarity('Smith~John~', 'Smith~John~'), 1)
        self.assertGreater(name_similarity('Smith~John~', 'Smith~Jon~'), .9)
        with self.assertRaises(VBAError):
            name_similarity('John Smith', 'Jon Smith')

    def test_bigram_boundaries_and_unused_slot(self):
        result = bigram('AB')
        self.assertEqual(result[:-1], ['%A', 'AB', 'B#'])
        self.assertIs(result[-1], EMPTY)

    def test_repeated_bigrams_are_not_deduplicated_or_clamped(self):
        self.assertEqual(dice('AAAA', 'AA'), 1.25)
        self.assertEqual(dice('AAAA', 'AA', dmph=True), .75)

    def test_edit_distance_transposition_and_insertions(self):
        for a, b, expected in [('AB', 'BA', 1), ('kitten', 'sitting', 3),
                               ('same', 'same', 0), ('', 'abc', 0)]:
            with self.subTest(a=a, b=b):
                self.assertEqual(lev_dist(a, b), expected)

    def test_lcs_normalized_and_raw(self):
        self.assertEqual(lcs('AB', 'BA'), .5)
        self.assertEqual(lcs('AB', 'BA', 'SSLCS'), 1)
        self.assertEqual(lcs('Smith', 'Smyth', 'Dmph'), 4)

    def test_recovered_metaphone_codes(self):
        self.assertEqual(double_metaphone('Smith'), ('SM0', 'XMT'))
        self.assertEqual(double_metaphone('Schmidt'), ('XMT', 'SMT'))
        self.assertEqual(double_metaphone('Robert'), ('RBRT', ''))

    def test_replacement_preserves_start_count_and_comparison(self):
        self.assertEqual(str_replace('aAaA', 'a', 'x', 1, 2), 'xxaA')
        self.assertEqual(str_replace('abcdef', 'b', 'X', 3), 'abcdef')
        self.assertEqual(str_replace('abcabc', 'abc', 'X'), 'XX')
        self.assertIsNone(str_replace(None, 'a', 'x'))

    def test_last_character_position(self):
        self.assertEqual(get_last_chr_pos('a~b~c', '~'), 4)
        self.assertEqual(get_last_chr_pos('ABC', 'b'), 2)
        self.assertEqual(get_last_chr_pos(None, '~'), 0)
        self.assertEqual(get_last_chr_pos('ABC', '~'), 0)

    def test_numeric_api_rejects_unintended_inputs(self):
        with self.assertRaises(TypeError): is_similar(123, '123')
        with self.assertRaises(TypeError): is_similar('abc', 'def', None)

    def test_finite_results_across_small_inputs_and_all_modes(self):
        words = ['', 'A', 'B', 'AB', 'BA', 'AA', 'A.B', 'A-B']
        for a, b, mode in itertools.product(words, words, ['', 'Dice', 'Lev', 'SSLCS', 'DblMetaPh']):
            with self.subTest(a=a, b=b, mode=mode):
                self.assertTrue(math.isfinite(is_similar(a, b, mode)))

    def test_parallel_calls_do_not_share_module_state(self):
        pairs = [('Smith', 'Smyth'), ('Robert', 'Rupert'), ('John', 'Jon')] * 8
        expected = [is_similar(*pair) for pair in pairs]
        with ThreadPoolExecutor(max_workers=4) as pool:
            self.assertEqual(list(pool.map(lambda pair: is_similar(*pair), pairs)), expected)


class CompatibilityTests(unittest.TestCase):
    def setUp(self):
        self.context = Context(FUNCTIONS)

    def test_integer_bankers_rounding_and_overflow(self):
        self.assertEqual(Integer(2.5), 2)
        self.assertEqual(Integer(3.5), 4)
        self.assertEqual(Long(-2.5), -2)
        with self.assertRaises(VBAError): Integer(32768)

    def test_single_intermediate_addition(self):
        self.assertEqual(self.context.binary('+', Single(16777216), Single(1)), 16777216)
        self.assertEqual(self.context.binary('+', Single(16777216), 1.0), 16777217)

    def test_variant_empty_null_and_boolean_logic(self):
        c = self.context
        self.assertTrue(c.binary('=', EMPTY, ''))
        self.assertTrue(c.binary('=', EMPTY, 0))
        self.assertIsNone(c.binary('=', None, None))
        self.assertFalse(c.binary('and', None, False))
        self.assertTrue(c.binary('or', None, True))
        self.assertEqual(c.binary('&', 'A', EMPTY), 'A')

    def test_utf16_string_positions(self):
        c = self.context
        self.assertEqual(c.builtin('len', ['A\U0001f600B']), 4)
        self.assertEqual(c.builtin('mid', ['A\U0001f600B', 4, 1]), 'B')

    def test_format_uses_decimal_ties_separately_from_cint(self):
        self.assertEqual(self.context.builtin('format', [.125, '0.00']), '0.13')
        self.assertEqual(self.context.builtin('format', [.5, '#.##']), '.5')

    def test_byref_array_and_scalar_updates(self):
        output = Cell()
        self.context.call('str2arry', ['AB', output])
        self.assertEqual(output.value.get(0), 'A')
        self.assertEqual(output.value.get(1), 'B')
        start, count = Cell(Long(1), 'long'), Cell(Long(0), 'long')
        self.context.call('strreplace', ['aaa', 'a', 'b', start, count])
        self.assertEqual(count.value, 3)

    def test_generation_source_hashes(self):
        provenance = json.loads((ROOT / 'strmatching2k/provenance.json').read_text())
        self.assertEqual(len(provenance['procedures']), 18)
        for name, expected in provenance['vba_sha256'].items():
            self.assertEqual(hashlib.sha256((ROOT / 'access-import' / name).read_bytes()).hexdigest(), expected)


class CommandLineTests(unittest.TestCase):
    def test_exact_single_checker_accepts_match_and_rejects_one_bit_difference(self):
        bits = struct.unpack('<I', struct.pack('<f', is_similar('PAIN RELIEF', 'PAINT REMOVER')))[0]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'reference.csv'
            header = 'reference,candidate,algorithm,single_hex\n'
            for expected, exit_status in [(bits, 0), (bits ^ 1, 1)]:
                path.write_text(header + f'PAIN RELIEF,PAINT REMOVER,,{expected:08X}\n')
                result = subprocess.run([sys.executable, '-m', 'strmatching2k', '--check', str(path)],
                                        cwd=ROOT, capture_output=True, text=True)
                self.assertEqual(result.returncode, exit_status, result.stderr)


if __name__ == '__main__':
    unittest.main()
