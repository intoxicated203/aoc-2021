"""
aoc 2021 - Python
"""

import sys

def parse(file_name: str) -> list:
    data = []
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()
        # print(lines)
        for line in lines:
            line = line.split(' -> ')
            # print(line)
            cur_line = []
            for pair in line:
                cur_line.extend([int(x) for x in pair.split(',')])
                # print(cur_line)
            data.append(cur_line)

    # print(data)

    return data

def run_testcase(file_name: str, mode: int) -> None:
    try:
        data = parse(file_name)
    except FileNotFoundError:
        print(f'[NOT FOUND]: {file_name}')
        return None
    if mode == 1:
        print(f'File {file_name}: {data}') # add function results to print
    elif mode == 2:
        print(f'File {file_name}: ') # add function results to print

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
                file_name = file_name.translate({ord("'") : None})
                run_testcase(file_name, mode)
        else:
            for test_num in range(11):
                run_testcase(f'test{test_num}.txt', mode)
