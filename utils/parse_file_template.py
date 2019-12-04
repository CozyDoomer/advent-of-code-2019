def parse_input_file_linewise(path, type):
    with open(path) as input_file:
        input_list = list(map(type, input_file.read().splitlines()))
        return input_list

def parse_input_file_seperated(path, seperator, type):
    with open(path) as input_file:
        input_list = list(map(type, input_file.read().split(seperator)))
        return input_list
