import sys
import argparse
import heapq

from utils import positive_int, chunks
from disk_array import InputArray, DiskArray


def merge(sorted_subarrays):

    iterators = (iter(subarray) for subarray in sorted_subarrays)
    result = DiskArray(heapq.merge(*iterators))

    return result


def merge_sort(input_array, start, end, k):

    
    if (end - start) * input_array.element_size <= input_array.ram:
        return DiskArray(input_array.get_sorted_range(start, end))

    chunks_idx = chunks(start, end, k)
    sorted_subarrays = [merge_sort(input_array, chunk_start, chunk_end, k) for chunk_start, chunk_end in chunks_idx]

    result = merge(sorted_subarrays)
    
    for subarray in sorted_subarrays:
        subarray.close_storage_file()
    
    return result


def main(input_file, output_file,
         num_lines, ram, k):

    input_array = InputArray(input_file, ram, num_lines)

    if input_array.element_size > input_array.ram:
        
        print("RAM size too small, it can't even hold a single string.",
              file=sys.stderr)

        return

    sorted_xs = merge_sort(input_array, 0, input_array.size, k)

    sorted_xs.output(output_file)
    sorted_xs.close_storage_file()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='External sorting'
    )


    parser.add_argument('input_file',
                        help='path to input file')
    parser.add_argument('output_file',
                        help='path to output file')
    parser.add_argument('-n', '--num_lines', type=positive_int,
                        help='number of lines in input file (pass to speed things up a little)')
    parser.add_argument('-r', '--ram', default=1e8, type=positive_int,
                        help='size of RAM in bytes that we can comfortably use')
    parser.add_argument('-k', '--k_way', default=3, type=positive_int,
                        help='k in k-way merge sort')

    args = parser.parse_args()

    if args.k_way == 1:
        raise argparse.ArgumentTypeError("k must be more than 1!")

    main(args.input_file, args.output_file,
         args.num_lines, args.ram, args.k_way)
