#!/usr/bin/env python3
import sys
from pprint import pprint

passport_fields = {
    'byr': {},
    'iyr': {},
    'eyr': {},
    'hgt': {},
    'hcl': {},
    'ecl': {},
    'pid': {},
    'cid': {'optional': True}
}

passports = []
current_passport = {}
valid_count = 0

for line in sys.stdin:
    fields = line.rstrip().split(' ')
    if len(fields[0]) == 0:
        passports.append(current_passport)
        current_passport = {}
        continue

    for field in fields:
        field_name, field_value = field.split(':')
        current_passport[field_name] = field_value

if len(current_passport) > 0:
    passports.append(current_passport)

for p in passports:
    valid = True
    for f, v in passport_fields.items():
        if 'optional' in v and v['optional']:
            continue

        if f not in p:
            valid = False
            break

    if valid:
        valid_count += 1

print(f'Valid passports: {valid_count}')
