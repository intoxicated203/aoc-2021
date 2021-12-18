"""
aoc 2021 - Python
"""

import sys

def parse(file_name: str) -> list:
    with open(file_name, 'r') as f:
        lines = [int(line.strip()) for line in f.read().split('\n')]
    return lines

def get_increase(data: list, mode: int) -> int:
    count = 0
    if len(data) <= 1:
        return 0
    elif mode == 1:
        for i in range(1, len(data)):
            if data[i] > data[i - 1]:
                count += 1
    elif mode == 2:
        sums = []
        for i in range(len(data)):
            if i == 0 or i == len(data) - 1:
                continue
            sums.append(sum(data[i-1:i+2]))
            if len(sums) > 1 and sums[len(sums)-1] > sums[len(sums)-2]:
                count += 1
    return count

def run_testcase(file_name: str, mode: int) -> None:
    try:
        data = parse(file_name)
    except FileNotFoundError:
        print(f'[NOT FOUND!!!] {file_name}')
        return 
    print(f'Test "{file_name}": ', get_increase(data, mode))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '-m':
            mode = sys.argv[2]
            mode = int(mode[-1])
            if len(sys.argv) >= 4 and sys.argv[3] != '.':
                run_testcase(sys.argv[3], mode)
            else:
                for test_num in range(11):
                    run_testcase(f'test{test_num}.txt', mode)
    else:
        print('[ARGV] Please add subcommand "-m" and:\n - "main-1" for part 1\n - "main-2" for part 2\nAnd add:\n - a custom testcase file name (with extension)\n - or add "." for running all testcases')
        sys.exit(1)
