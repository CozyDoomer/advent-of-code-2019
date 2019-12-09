from utils.parse_file_template import parse_input_file_seperated

import collections
import math
import re
import sys
import sortedcollections


def calc_boost(input_list, input_param):
    pc = 0
    outputs = []

    dict_int = collections.defaultdict(int)
    for i, v in enumerate(input_list):
        dict_int[i] = v
    input_list = dict_int

    relbase = 0

    arity = {99: 0, 1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 9: 1}

    def parse():
        nonlocal pc
        op = input_list[pc]
        pc += 1
        vals = []
        locs = []
        for i in range(arity[op % 100]):
            mode = (op // (10 ** (2 + i))) % 10
            vals.append(input_list[pc] if mode == 1 else input_list[input_list[pc] + relbase] if mode == 2 else input_list[input_list[pc]])
            locs.append(None if mode == 1 else input_list[pc] + relbase if mode == 2 else input_list[pc])
            pc += 1
        return op % 100, vals, locs

    while input_list[pc] != 99:
        opc = pc
        op, vals, locs = parse()

        if op == 1:
            input_list[locs[2]] = vals[0] + vals[1]
        elif op == 2:
            input_list[locs[2]] = vals[0] * vals[1]
        elif op == 3:
            input_list[locs[0]] = input_param  # 1 # yield
            assert input_list[locs[0]] is not None
        elif op == 4:
            yield vals[0]
        elif op == 5:
            if vals[0] != 0:
                pc = vals[1]
        elif op == 6:
            if vals[0] == 0:
                pc = vals[1]
        elif op == 7:
            input_list[locs[2]] = int(vals[0] < vals[1])
        elif op == 8:
            input_list[locs[2]] = int(vals[0] == vals[1])
        elif op == 9:
            relbase += vals[0]
        else:
            assert False

    return input_list[0], outputs[0] if outputs else None


if __name__ == "__main__":
    INPUT_LIST = parse_input_file_seperated("input_day9.txt", ",", int)

    print(f"Part One: {next(calc_boost(INPUT_LIST, 1))}")
    print(f"Part Two: {next(calc_boost(INPUT_LIST, 2))}")
