import json
import pprint
import argparse
import sys


def load_data(filepath):
    with open(filepath, encoding='utf8') as json_file:
        ugly_json_file = json.load(json_file)
    return ugly_json_file


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('name')
    parser.add_argument('-l', '--limiter', type=int)
    return parser


def pretty_print_json(data, limiter=None):
    if limiter:
        pprint.pprint(data[:limiter])
    else:
        pprint.pprint(data)


if __name__ == '__main__':
    parser = create_parser()
    params = parser.parse_args()
    data = load_data(params.name)
    pretty_print_json(data, params.limiter)
