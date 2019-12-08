from utils.parse_file_template import parse_input_file_seperated

import collections
import math
import re
import sys

import sortedcollections
import itertools


def validate_intcode(intcode):
    pc = 0
    outputs = []

    arity = {99: 0, 1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3}

    def parse():
        nonlocal pc
        op = intcode[pc]
        pc += 1
        vals = []
        locs = []
        for i in range(arity[op % 100]):
            mode = (op // (10 ** (2 + i))) % 10
            vals.append(intcode[pc] if mode == 1 else intcode[intcode[pc]])
            locs.append(None if mode == 1 else intcode[pc])
            pc += 1
        return op % 100, vals, locs

    while intcode[pc] != 99:
        opc = pc
        op, vals, locs = parse()
        if op == 1:
            intcode[locs[2]] = vals[0] + vals[1]
        elif op == 2:
            intcode[locs[2]] = vals[0] * vals[1]
        elif op == 3:
            intcode[locs[0]] = yield
            assert intcode[locs[0]] is not None
        elif op == 4:
            yield vals[0]
        elif op == 5:
            if vals[0] != 0:
                pc = vals[1]
        elif op == 6:
            if vals[0] == 0:
                pc = vals[1]
        elif op == 7:
            intcode[locs[2]] = int(vals[0] < vals[1])
        elif op == 8:
            intcode[locs[2]] = int(vals[0] == vals[1])
        else:
            assert False

    return intcode[0], outputs[0] if outputs else None


def try_permutations(input_list, permutation_range):
    m = 0
    for a, b, c, d, e in itertools.permutations(permutation_range):
        ap = validate_intcode(input_list[:])
        bp = validate_intcode(input_list[:])
        cp = validate_intcode(input_list[:])
        dp = validate_intcode(input_list[:])
        ep = validate_intcode(input_list[:])

        next(ap)
        ap.send(a)
        next(bp)
        bp.send(b)
        next(cp)
        cp.send(c)
        next(dp)
        dp.send(d)
        next(ep)
        ep.send(e)

        eo = -123
        val = 0
        for lo in range(10000000000000000):
            done = False
            for p in (ap, bp, cp, dp, ep):
                try:
                    if lo != 0:
                        next(p)
                    val = p.send(val)
                    if p == ep:
                        eo = val
                except StopIteration:
                    done = True
                    break
            if done:
                break

        if eo > m:
            m = eo
    return m


if __name__ == "__main__":
    INPUT_LIST = parse_input_file_seperated("input_day7.txt", ",", int)

    print(f"Part One: {try_permutations(INPUT_LIST, range(5))}")
    print(f"Part Two: {try_permutations(INPUT_LIST, range(5, 10))}")
