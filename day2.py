from utils.parse_file_template import parse_input_file_comma_seperated


def calc_intcode(input_list):
    i = 0
    cursor = input_list[i]
    while cursor != 99:
        if cursor == 1:
            input_list[input_list[i+3]] = input_list[input_list[i+1]] + input_list[input_list[i+2]]
        elif cursor == 2:
            input_list[input_list[i+3]] = input_list[input_list[i+1]] * input_list[input_list[i+2]]
        i+=4
        cursor = input_list[i]
    return input_list


def find_noun_verb(input_list, target):
    for x in range(100):
        for y in range(100):
            reset_input_list = input_list[:]
            reset_input_list[1] = x
            reset_input_list[2] = y
            reset_input_list = calc_intcode(reset_input_list)
            
            if reset_input_list[0] == 19690720:
                return 100 * x + y


def test_calc_intcode():
    assert calc_intcode([1,0,0,0,99]) == [2,0,0,0,99]
    assert calc_intcode([2,3,0,3,99]) == [2,3,0,6,99]
    assert calc_intcode([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
    assert calc_intcode([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]


if __name__ == "__main__":
    INPUT_LIST = parse_input_file_comma_seperated("input_day2.txt", int)
    
    test_calc_intcode()
    INPUT_LIST[1] = 12
    INPUT_LIST[2] = 2
    print(f"Part One: {calc_intcode(INPUT_LIST)[0]}") # 3562672
    
    INPUT_LIST = parse_input_file_comma_seperated("input_day2.txt", int)
    print(f"Part Two: {find_noun_verb(INPUT_LIST, 19690720)}") # 8250
