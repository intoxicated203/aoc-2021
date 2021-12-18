"""
aoc 2021 - Python
"""

import sys
from collections import Counter

def parse(file_name: str) -> list:
    with open(file_name, 'r') as f:
        lines = [line.strip() for line in f.read().split('\n')]
    return lines

def get_consumption(data: list[str]) -> int:
    gamma_rate, epsilon_rate = '0b', '0b'
    for column in range(len(data[0])):
        bit_column = [line[column] for line in data]
        count = dict(Counter(bit_column))
        if count['0'] > count['1']:
            gamma_rate, epsilon_rate = '0', '1'
        else:
            epsilon_rate, gamma_rate = '0', '1'
    return int(gamma_rate, 2) * int(epsilon_rate, 2)

def filter(data: list[str], mode: int) -> str: # mode = 1 -> oxy, mode = 2 -> co2
    column = 0
    while len(data) > 1 or column <= len(data[0]) - 1:
        bit_column = [line[column] for line in data]
        count = dict(Counter(bit_column))
        if len(count) > 1:
            if mode == 1:
                if count['0'] > count['1']:
                    key = '0'
                else:
                    key = '1'
            else:
                if count['0'] > count['1']:
                    key = '1'
                else:
                    key = '0'

            for binary in data.copy():
                if binary[column] != key:
                    data.remove(binary)
        column += 1

    return int(f'0b{data[0]}', 2)

def get_life_support(data: list[str]) -> int:
    oxy = filter(data.copy(), 1)
    co2_scrub = filter(data.copy(), 2)
    return oxy * co2_scrub

def run_testcase(file_name: str, mode: int) -> None:
    try:
        data = parse(file_name)
    except FileNotFoundError:
        print(f'[NOT FOUND]: {file_name}')
        return None
    if mode == 1:
        print(f'File {file_name}: {get_consumption(data)}') # add function results to print
    elif mode == 2:
        print(f'File {file_name}: {get_life_support(data)}') # add function results to print

if __name__ == '__main__':
    if len(sys.argv) <= 2:
        print("[SUBCOMMAND] Mising subcommand '-m' or mode arg")
    elif sys.argv[1] == '-m':
        mode = sys.argv[2]
        try:
            mode = int(mode[-1])
        except ValueError:
            print('[SUBCOMMAND] Invalid mode')
            sys.exit(1)
        if len(sys.argv) > 3 and sys.argv[3] != '.':
            for file_name in sys.argv[3:]:
                run_testcase(file_name, mode)
        else:
            for test_num in range(11):
                run_testcase(f'test{test_num}.txt', mode)
