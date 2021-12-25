"""
aoc 2021 - Python
"""

import sys

def parse(file_name: str) -> tuple[list[int], list[list[list[int]]]]:
    with open(file_name, 'r') as f:
        file = f.read().splitlines()
        marked = [int(x) for x in file[0].split(',')]
        file = [line.split() for line in file[1:]]
        # print(file)
        boards, new_board = [], []
        count = 0
        for line in file:
            int_list = [int(x) for x in line]
            # print(int_list, sum_boards)
            new_board.append(int_list)
            if count == 4: # 5x5 board is complete
                boards.append(new_board.copy())
                new_board.clear()
                count = 0
            else:
                count += 1

    # print(marked, boards)

    return marked, boards, 

def check_done(boards: list[list[int]]) -> list[int]:
    boards_done = []
    for board_index, board in enumerate(boards):
        for row_index, row in enumerate(board):
            # print(row, '*')
            if not any(row): # searching for row completed
                boards.append(board_index)
            # print([board[row_count][row_index] for row_count in range(5)])
            if not any([board[row_count][row_index] for row_count in range(5)]): # searching for column completed
                boards.append(board_index)
    return list(set(boards)) if len(boards) > 0 else [-1]

def cross_out(marked: list[int], boards: list[list[list[int]]]) -> tuple[list[int], list[list[list[int]]], int]:
    marked_num = marked.pop(0)
    for board_index, board in enumerate(boards):
        for row_index, row in enumerate(board):
                # print(board, ' :: ')
                # print(board_index)
                while marked_num in row:
                    marked_num_index = row.index(marked_num)
                    boards[board_index][row_index][marked_num_index] = None
    
    return marked, boards
                
def get_sum_board(boards: list[list[list[int, bool]]], done: int) -> int:
    sum_boards = 0
    for row in boards[done]:
        # print(row, [x for x in row if x])
        sum_boards += sum([x for x in row if x])

    return sum_boards

def bingo(marked: list[int], boards: list[list[list[int]]]) -> int:
    # cur_marked = 1
    # print(marked, boards)
    done = [-1]
    while done == [-1]:
        cur_marked = marked[0]
        marked, boards = cross_out(marked, boards)
        done = check_done(boards)
        # print(marked)
    sum_boards = get_sum_board(boards, done[0])
    # print(cur_marked, sum_boards)
    return cur_marked * sum_boards

def demark(marked_ref: list[int], boards: list[list[list[int]]], boards_ref: list[list[list[int]]]) -> tuple[list[int], list[list[list[int, bool]]]]:
    marked_num = marked_ref.pop()
    for board_index, board_ref in enumerate(boards_ref):
        for row_index, row_ref in enumerate(board_ref):
            while marked_num in row_ref:
                marked_num_index = row_ref.index(marked_num)
                boards[board_index][row_index][marked_num_index] = marked_num

    return marked_ref, boards

def last_board(marked: list[int], boards: list[list[list[int]]]) -> int:
    boards_ref = boards.copy()
    marked_ref = marked.copy()
    while len(marked) > 0:
        marked, boards = cross_out(marked, boards) # cross out all of the marked

    boards_done = range(len(boards))

    done = 0
    marked = marked_ref.copy()
    while done != -1:
        cur_marked = marked_ref[-1]
        marked_ref, boards = demark(marked_ref, boards, boards_ref) # demark the boards using marked_ref and boards_ref until boards is not done
        last_done, done = done, check_done(boards)
    sum_boards = get_sum_board(boards, last_done)

    return cur_marked * last_done

def run_testcase(file_name: str, mode: int) -> None:
    try:
        marked, boards = parse(file_name)
    except FileNotFoundError:
        print(f'[NOT FOUND]: {file_name}')
        return None
    # print(bingo(marked, boards, sum_board))
    # print(boards)
    if mode == 1:
        print(f'File {file_name}: {bingo(marked, boards)}') # add function results to print
    elif mode == 2:
        print(f'File {file_name}: {last_board(marked, boards)}') # add function results to print

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
