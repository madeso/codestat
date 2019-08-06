#!/usr/bin/env python3

import argparse
import os
import filecmp
import subprocess
import shutil
import sys
import platform
import typing
import json
from enum import Enum

class Stat:
    def __init__(self, n):
        self.name = n
        self.number_of_structs = 0
        self.number_of_classes = 0
        self.max_indentation = 0


def update_stat(s, l):
    s.number_of_structs += l.number_of_structs
    s.number_of_classes += l.number_of_classes
    s.max_indentation = max(s.max_indentation, l.max_indentation)


def collect_stat(f):
    s = Stat(f.name)
    for line in f:
        l = Stat('')
        if 'class' in line:
            l.number_of_classes = 1
        elif 'struct' in line:
            l.number_of_structs = 1
        if line.strip() != '':
            l.max_indentation = len(line) - len(line.lstrip())
        update_stat(s, l)
    return s

def print_line():
    print('------------')


def print_stat(s):
    print_line()
    print(s.name)
    print('structs:', s.number_of_structs)
    print('classes:', s.number_of_classes)
    print('indent:', s.max_indentation)
    print()

def main():
    parser = argparse.ArgumentParser(description='Manage my dot files.')
    parser.add_argument('files', type=argparse.FileType('r'), help='files', nargs='+')
    args = parser.parse_args()

    s = Stat('Total')
    for f in args.files:
        l = collect_stat(f)
        print_stat(l)
        update_stat(s, l)

    print()
    print()
    print_stat(s)


if __name__ == "__main__":
    main()

