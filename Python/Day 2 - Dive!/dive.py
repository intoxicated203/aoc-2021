"""
aoc 2021 - Python
"""

import sys

DIR = {
    'forward' : [1, 0],
    'down': [0, 1],
    'up': [0, -1],
}

def parse(file_name: str) -> list:
    with open(file_name, 'r') as f:
        lines = [line.strip() for line in f.read().split('\n')]
    return [x.split() for x in lines]

def get_product(data: list[list], is_aim: bool=False) -> int:
    pos = [0, 0]
    aim = 0
    for line in data:
        direction = DIR[line[0]]
        value = int(line[1])
        if not is_aim:
            pos = [pos[i] + value for i in range(2)]
        else:
            if direction[1] != 0: # which means either 'down' or 'up'
                aim += direction[1] * value
            else: # which means definitely 'forward'
                pos[0] += value
                pos[1] += aim * value
    return pos[0] * pos[1]

def run_testcase(file_name: str, mode: int) -> None:
    try:
        data = parse(file_name)
    except FileNotFoundError:
        print(f'[NOT FOUND]: {file_name}')
        return None
    if mode == 1:
        print(f'File {file_name}: ', get_product(data))  # add function results to print
    elif mode == 2:
        print(f'File {file_name}: ', get_product(data, True)) # add function results to print


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
