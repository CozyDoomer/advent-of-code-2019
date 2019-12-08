from utils.parse_file_template import parse_input_file_string
from matplotlib import pyplot as plt
import numpy as np
import sys
import functools


def calc_layer_code(input_list, window=(25, 6)):
    layer_length = window[0] * window[1]
    last_zero_count = sys.maxsize
    result = -1
    for i in range(0, len(input_list), layer_length):
        single_layer = np.array([values for values in input_list[i:i+layer_length]]).astype(int)
        min_zero_count = len(single_layer[single_layer == 0])
        if min_zero_count < last_zero_count:
            last_zero_count = min_zero_count
            result = len(single_layer[single_layer == 1]) * len(single_layer[single_layer == 2])
    return result


def decode_image(input_list, window=(25, 6)):
    layer_length = window[0] * window[1]
    decoded = np.zeros((len(input_list)//layer_length, layer_length))
    result = []
    for i, j in enumerate(range(0, len(input_list), layer_length)):
        decoded[i] = np.array([values for values in input_list[j:j+layer_length]]).astype(int)
    for layer in np.rollaxis(decoded, 1):
        result.append(int(functools.reduce(lambda a, b: np.where(a < 2, a, b), layer)))
    return np.reshape(result, (6, 25))


if __name__ == "__main__":
    INPUT_STRING = parse_input_file_string("input_day8.txt", str)
    print(f"Part One: {calc_layer_code(INPUT_STRING)}")
    plt.imshow(decode_image(INPUT_STRING))
    plt.show()
