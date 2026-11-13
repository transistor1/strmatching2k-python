"""Score a pair or check reference CSV/JSON, including optional Single hex bits."""
import argparse
import csv
import json
from pathlib import Path
import struct
from . import is_similar


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('reference', nargs='?')
    parser.add_argument('candidate', nargs='?')
    parser.add_argument('--algorithm', default='')
    parser.add_argument('--check', type=Path, help='reference CSV or JSON file')
    args = parser.parse_args()
    if args.check:
        if args.check.suffix.lower() == '.json':
            cases = json.loads(args.check.read_text())
        else:
            with args.check.open(newline='', encoding='utf-8-sig') as source:
                cases = list(csv.DictReader(source))
        failures = 0
        for case in cases:
            score = is_similar(case['reference'], case['candidate'], case.get('algorithm', ''))
            bits = f'{struct.unpack("<I", struct.pack("<f", score))[0]:08X}'
            ok = (bits == case['single_hex'].upper() if case.get('single_hex')
                  else format(score, '.6f') == case['expected_6dp'])
            failures += not ok
            print(f'{"PASS" if ok else "FAIL"} {case["reference"]!r} | {case["candidate"]!r}: {score:.6f} [{bits}]')
        print(f'{len(cases) - failures}/{len(cases)} passed')
        raise SystemExit(bool(failures))
    if args.reference is None or args.candidate is None:
        parser.error('provide two strings, or --check FILE')
    print(is_similar(args.reference, args.candidate, args.algorithm))


if __name__ == '__main__':
    main()
