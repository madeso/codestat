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
    def __init__(self):
        self.number_of_structs = 0
        self.number_of_classes = 0

def collect_stat(f):
    s = Stat()
    for line in f:
        if 'class' in line:
            s.number_of_classes += 1
        elif 'struct' in line:
            s.number_of_structs += 1
    return s

def print_line():
    print('------------')

def parse_file(f):
    print_line()
    print(f.name)
    s = collect_stat(f)
    print('structs:', s.number_of_structs)
    print('classes:', s.number_of_classes)
    print()
    return s

def main():
    parser = argparse.ArgumentParser(description='Manage my dot files.')
    parser.add_argument('files', type=argparse.FileType('r'), help='files', nargs='+')
    args = parser.parse_args()

    s = Stat()
    for f in args.files:
        l = parse_file(f)
        s.number_of_structs += l.number_of_structs
        s.number_of_classes += l.number_of_classes

    print()
    print()
    print_line()
    print()
    print('Total number of structs:', s.number_of_structs)
    print('Total number of classes:', s.number_of_classes)


if __name__ == "__main__":
    main()

