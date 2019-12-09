from utils.parse_file_template import parse_input_file_string
from matplotlib import pyplot as plt
import numpy as np
import sys
import functools


def calc_layer_code(input_list, ):
    return min(((l == 0).sum(), (l == 1).sum() * (l == 2).sum()) for l in input_list)[1]


def decode_image(input_list):
    return functools.reduce(lambda a, b: np.where(a < 2, a, b), input_list)


if __name__ == "__main__":
    input_list = [int(value) for value in list(parse_input_file_string("input_day8.txt"))[:-1]]
    img_shape = (-1, 6, 25)
    input_list = np.reshape(input_list, img_shape)

    print(f"Part One: {calc_layer_code(input_list)}")
    plt.imshow(decode_image(input_list))
    plt.show()
