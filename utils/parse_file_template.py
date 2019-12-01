def parse_input_file(path, type):
    with open(path) as input_file:
        input_list = list(map(type, input_file.read().splitlines()))
        return input_list
