import sys
import numpy as np
from utils.parse_file_template import parse_input_file_linewise


def count_orbits_to_com(orbits, current_orbit):
    count_orbit = 1
    new_center, new_orbit = current_orbit
    while new_center != "COM":
        new_center, new_orbit = np.squeeze(orbits[np.squeeze((orbits[:, 1:] == new_center))])
        count_orbit += 1
    return count_orbit


def orbits_to_com(orbits, current_orbit):
    result = []
    new_center, new_orbit = current_orbit
    while new_center != "COM":
        new_center, new_orbit = np.squeeze(orbits[np.squeeze((orbits[:, 1:] == new_center))])
        result += [new_center]
    return np.array(result)


def calc_orbits(input_list):
    orbits = np.array([orbits.split(")") for orbits in input_list])
    count = 0
    for orbit in orbits:
        count += count_orbits_to_com(orbits, orbit)
    return count


def calc_shortest_path(input_list):
    orbits = np.array([orbits.split(")") for orbits in input_list])
    orbits_you = np.squeeze(orbits[np.squeeze((orbits[:, 1:] == "YOU"))])
    orbits_santa = np.squeeze(orbits[np.squeeze((orbits[:, 1:] == "SAN"))])
    to_com_you = orbits_to_com(orbits, orbits_you)
    to_com_santa = orbits_to_com(orbits, orbits_santa)
    intersections = np.intersect1d(to_com_you, to_com_santa)
    count = sys.maxsize
    for intersection in intersections:
        distance = (np.where(to_com_you == intersection)[0] + np.where(to_com_santa == intersection)[0] + 2)[0]
        count = distance if distance < count else count
    return count


if __name__ == "__main__":
    INPUT_LIST = parse_input_file_linewise("input_day6.txt", str)
    print(f"Part One: {calc_orbits(INPUT_LIST)}")
    print(f"Part Two: {calc_shortest_path(INPUT_LIST)}")
