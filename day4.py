from utils.parse_file_template import parse_input_file_seperated


def valid_password_p1(pw):
    pw = list(str(pw))
    if pw != sorted(pw) or len(set(pw)) == len(pw):
        return False
    return True


def valid_password_p2(pw):
    return 2 in [str(pw).count(d) for d in str(pw)]


if __name__ == "__main__":
    INPUT_LIST = parse_input_file_seperated("input_day4.txt", "-", int)
    
    pws = [pw for pw in range(INPUT_LIST[0], INPUT_LIST[1] + 1) if valid_password_p1(pw)]
    print(f"Part One: {len(pws)}") # 1919

    pws_2 = [pw for pw in pws if valid_password_p2(pw)]
    print(f"Part Two: {len(pws_2)}") #1291
        