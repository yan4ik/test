import argparse
import random
import string


def positive_int(arg_str):
    value = int(arg_str)
    if value <= 0:
        raise argparse.ArgumentTypeError("%s is an invalid positive int value" % arg_str)
    return value


def get_random_str(str_len): 
    return ''.join(random.choices(string.ascii_lowercase, k=str_len))


def chunks(start, end, k):
    """
    Yields k borders of successive chunks of consecutive integers from [start, end].
    """

    assert start < end
    assert k > 1

    k = min(k, end - start)

    chunk_len = (end - start) // k

    result = [(i, min(end, i + chunk_len)) for i in range(start, end, chunk_len)]
    
    if len(result) > k:
        last_chunk = result.pop()
        result[-1] = (result[-1][0], last_chunk[-1])

    assert len(result) == k

    return result


def line_count(fname):
    with open(fname) as f:
        return sum(1 for _ in f)

