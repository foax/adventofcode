#!/usr/bin/env python3

import sys
import re
from pprint import pprint


def run_program(i):
    accumulator = 0
    inst_count = 0
    has_run = set()

    while True:
        if inst_count in has_run:
            # print(f'Aborting on line {inst_count}')
            return False
        if inst_count == len(i):
            print(f'Accumlator value: {accumulator}')
            return True

        inst = i[inst_count]
        # print(f'line {inst_count}')
        # pprint(inst)
        has_run.add(inst_count)
        if inst['op'] == 'nop':
            inst_count += 1
        elif inst['op'] == 'acc':
            accumulator += inst['arg']
            inst_count += 1
        elif inst['op'] == 'jmp':
            inst_count += inst['arg']


line_re = re.compile('(\w{3}) ([+-]\d+)')
instructions = []

for line in sys.stdin:
    match = line_re.match(line.rstrip())
    op, arg = match.group(1, 2)
    inst = {
        'op': op,
        'arg': int(arg)
    }
    instructions.append(inst)

if not run_program(instructions):

    for i, inst in enumerate(instructions):
        # print(f'line: {i}; inst: {inst}')
        if inst['op'] == 'nop' or inst['op'] == 'jmp':
            new_insts = instructions.copy()
            new_inst = new_insts[i].copy()
            if inst == 'nop':
                new_inst['op'] = 'jmp'
            else:
                new_inst['op'] = 'nop'
            new_insts[i] = new_inst
            if run_program(new_insts):
                break
