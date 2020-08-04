#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

if len(sys.argv) < 2:
    print("Please pass in a second filename.")
    sys.exit()

file_name = sys.argv[1]
program = []
try:
    with open(file_name) as file:
        for line in file:
            split_line = line.split('#')[0]
            command = split_line.strip()

            if command == '':
                continue

            num = int(command, 2)
            program.append(num)
except FileNotFoundError:
    print(f'{sys.argv[0]}: {sys.argv[1]} file was not found.')
    sys.exit()

cpu = CPU()

cpu.load(program)
cpu.run()