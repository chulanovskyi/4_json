import json
import pprint


def load_data(filepath):
    with open(filepath, encoding='utf8') as file:
        ugly_json_file = json.loads(file.read())
    return ugly_json_file


def pretty_print_json(data, max_len=0):
    if max_len:
        pprint.pprint(data[:max_len])
    else:
        pprint.pprint(data)


if __name__ == '__main__':
    data = load_data('Bars.json')
    '''
    Because file "Bars.json" have many nesting records,
    you can use second argument as a limiter for records to be printed
    '''
    pretty_print_json(data, 5)
