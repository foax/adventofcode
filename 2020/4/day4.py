#!/usr/bin/env python3
import sys
import re
from pprint import pprint


def in_range(x, minmax):
    return x >= minmax[0] and x <= minmax[1]


passport_fields = {
    'byr': {
        'regex': '\d{4}',
        'range': (1920, 2002)
    },
    'iyr': {
        'regex': '\d{4}',
        'range': (2010, 2020)
    },
    'eyr': {
        'regex': '\d{4}',
        'range': (2020, 2030)
    },
    'hgt': {
        'regex': '(\d+)(cm|in)',
        'cm': (150, 193),
        'in': (59, 76)
    },
    'hcl': {
        'regex': '#[0-9a-f]{6}'
    },
    'ecl': {
        'regex': '(amb|blu|brn|gry|grn|hzl|oth)'

    },
    'pid': {
        'regex': '\d{9}'
    },
    'cid': {'optional': True}
}

passports = []
current_passport = {}
valid_count = 0

for line in sys.stdin:
    fields = line.rstrip().split(' ')
    if len(fields[0]) == 0:
        # Hit a line break, so add last passport to the list
        passports.append(current_passport)
        current_passport = {}
        continue

    for field in fields:
        field_name, field_value = field.split(':')
        current_passport[field_name] = field_value

# Just in case there is no trailing line break
if len(current_passport) > 0:
    passports.append(current_passport)

for p in passports:
    # Assume valid until proven otherwise
    valid = True
    for f, v in passport_fields.items():
        if 'optional' in v and v['optional']:
            continue

        if f not in p:
            valid = False
            break

        match = re.fullmatch(v['regex'], p[f])
        if not match:
            valid = False
            break

        try:
            x, unit = match.group(1, 2)
            if not in_range(int(x), v[unit]):
                valid = False
                break
        except IndexError:
            pass

        if 'range' in v:
            if not in_range(int(p[f]), v['range']):
                valid = False
                break

    if valid:
        valid_count += 1

print(f'Valid passports: {valid_count}')
