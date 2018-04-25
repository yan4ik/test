# External Sorting in Python

Written in Python 3.6

Source code overview:
 * `generator.py` - generates a file which contains strings of equal length.
 * `external_sort.py` - sorts the file using k-way merge sort.
 * `disk_array.py` - classes of external memory arrays.
 * `utils.py` - misc utility functions.
 * `test.py` - simple test utility to compare against unix built-in `sort` function.

Example usage:
```bash

# generate a big file
python3 generator.py huge_input.txt --num_lines 50000000 --str_size 100

# sort it using approximately 2GB of RAM (in practice it can take a little more)
python3 external_sort.py huge_input.txt huge_output.txt --num_lines 50000000 --ram 2000000000 -k 3
```
