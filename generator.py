import argparse

from utils import get_random_str, positive_int


parser = argparse.ArgumentParser(
    description='Huge files generator'
)


parser.add_argument('output_file',
                    help='path to output file')
parser.add_argument('-n', '--num_lines', default=10000, type=positive_int,
                    help='total number of strings in file')
parser.add_argument('-s', '--str_size', default=100, type=positive_int,
                    help='number of characters in each string')


args = parser.parse_args()

output_file = args.output_file
num_lines = args.num_lines
str_size = args.str_size


with open(output_file, 'w') as wf:
    for _ in range(num_lines):
        print(get_random_str(str_size),
              file=wf)
