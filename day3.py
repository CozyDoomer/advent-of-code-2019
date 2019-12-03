from utils.parse_file_template import parse_input_file_comma_seperated, parse_input_file_linewise


def calc_points(A):
    DX = {"L": -1, "R": 1, "U": 0, "D": 0}
    DY = {"L": 0, "R": 0, "U": 1, "D": -1}
    x = y = length = 0
    result = {}

    for cmd in A:
        d = cmd[0]
        n = int(cmd[1:])
        assert d in ["L", "R", "U", "D"]
        for _ in range(n):
            x += DX[d]
            y += DY[d]
            length += 1
            if (x, y) not in result:
                result[(x, y)] = length
    return result


def min_steps_to_intersection(point_a, point_b):
    both = set(point_a.keys()) & set(point_b.keys())
    return min([abs(x) + abs(y) for (x, y) in both]), min([point_a[p] + point_b[p] for p in both])


if __name__ == "__main__":
    wire1, wire2 = [x.split(",") for x in parse_input_file_linewise("input_day3.txt", str)]

    point_a = calc_points(wire1)
    point_b = calc_points(wire2)

    result = min_steps_to_intersection(point_a, point_b)

    print(f"Part One: {result[0]}")  # 1195
    print(f"Part One: {result[1]}")  # 91518
