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

def parse_file(f):
    print('------------')
    print(f.name)
    number_of_structs = 0
    number_of_classes = 0
    for line in f:
        if 'class' in line:
            number_of_classes += 1
        elif 'struct' in line:
            number_of_structs += 1
    print('structs:', number_of_structs)
    print('classes:', number_of_classes)
    print()

def main():
    parser = argparse.ArgumentParser(description='Manage my dot files.')
    parser.add_argument('files', type=argparse.FileType('r'), help='files', nargs='+')
    args = parser.parse_args()

    for f in args.files:
        parse_file(f)

if __name__ == "__main__":
    main()

