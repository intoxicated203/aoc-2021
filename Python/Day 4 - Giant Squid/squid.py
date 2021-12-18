"""
aoc 2021 - Python
"""

import sys

def parse(file_name: str) -> list:
    with open(file_name, 'r') as f:
        file = [line[:-1] for line in f.readlines() if line != '\n']
        marked = [int(x) for x in file[0].split(',')]
        file = [line.split() for line in file[1:]]
        boards, new_board = [], []
        count = 0
        for line in file:
            int_list = [int(x) for x in line]
            new_board.append(int_list)
            if count == 4: # 5x5 board is complete
                boards.append(new_board.copy())
                new_board.clear()
                count = 0
            else:
                count += 1

    return marked, boards

def check_done(boards: list[list[int]]) -> int:
    for index, board in enumerate(boards):
        for row in board:
            if len(row) == 0:
                return index
    return -1

def cross_out(marked: list[int], boards: list[list[list[int]]]) -> tuple[list[int], list[list[list[int]]]]:
    marked_num = marked.pop(0)
    for board_index, board in enumerate(boards.copy()):
        for row_index, row in enumerate(board.copy()):
            while marked_num in row:
                boards[board_index][row_index].remove(marked_num)
                

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
                run_testcase(file_name, mode)
        else:
            for test_num in range(11):
                run_testcase(f'test{test_num}.txt', mode)
