

from utils.parse_file_template import parse_input_file


def calc_fuel(mass):
    return mass // 3 - 2


def calc_fuel_recursive(mass):
    fuel = calc_fuel(mass)
    return calc_fuel_recursive(fuel) + fuel if fuel > 0 else 0


if __name__ == "__main__":
    INPUT_LIST = parse_input_file("input_day1.txt", int)

    assert calc_fuel(12) == 2
    assert calc_fuel(14) == 2
    assert calc_fuel(1969) == 654
    assert calc_fuel(100756) == 33583
    print(f"Part One: {sum([calc_fuel(input_int) for input_int in INPUT_LIST])}")

    assert calc_fuel_recursive(14) == 2
    assert calc_fuel_recursive(1969) == 966
    assert calc_fuel_recursive(100756) == 50346
    print(f"Part Two: {sum([calc_fuel_recursive(input_int) for input_int in INPUT_LIST])}")
