from utils.parse_file_template import parse_input_file_seperated


def TEST(input_list, input_param):
    p = 0
    while input_list[p] != 99:
        args = {1: input_list[p + 1] if int((input_list[p] % 1000) / 100) else input_list[input_list[p + 1]],
                2: input_list[p + 2] if int((input_list[p] % 10000) / 1000) or input_list[p] % 100 == 4 else input_list[input_list[p + 2]]}
        instr = input_list[p] % 100
        instr_func = {1: (input_list[p + 3], args[1] + args[2], p + 4),
                      2: (input_list[p + 3], args[1] * args[2], p + 4),
                      3: (input_list[p + 1], input_param, p + 2),
                      4: (0, input_list[0], p + 2),
                      5: (0, input_list[0], args[2] if args[1] else p + 3),
                      6: (0, input_list[0], args[2] if not args[1] else p + 3),
                      7: (input_list[p + 3], int(args[1] < args[2]), p + 4),
                      8: (input_list[p + 3], int(args[1] == args[2]), p + 4)}[instr]
        input_list[instr_func[0]] = instr_func[1]
        p = instr_func[2]
        if instr == 4:
            output = args[1]
    return(output)


if __name__ == "__main__":
    INPUT_LIST = parse_input_file_seperated("input_day5.txt", ",", int)
    print(f"{TEST(INPUT_LIST, 1)}")  # part 1

    INPUT_LIST = parse_input_file_seperated("input_day5.txt", ",", int)
    print(f"{TEST(INPUT_LIST, 5)}")  # part 2
