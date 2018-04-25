import os
import io
import tempfile
import shutil

from utils import line_count


class InputArray:
    
    def __init__(self, input_file, ram, size=None):

        self.input_file = input_file
        self.ram = ram

        if size is None:
            self.size = line_count(self.input_file)
        else:
            self.size = size

        with open(input_file) as rf:
            self.element_size = len(next(rf))


    def get_sorted_range(self, start, end):
        with open(self.input_file) as rf:
            
            rf.seek(start * self.element_size)

            segment = [next(rf).rstrip() for _ in range(end - start)]
            segment.sort()

            return segment


class DiskArray:
    
    def __init__(self, initial_data, buffering=-1):

        self.data_file = tempfile.TemporaryFile(mode='w+', buffering=buffering)
        
        for x in initial_data:
            print(x, file=self.data_file)


    def __iter__(self):
        self.data_file.seek(0)
        return (line.rstrip() for line in self.data_file)


    def close_storage_file(self):
         self.data_file.close()


    def output(self, output_file):
        self.data_file.seek(0)

        with open(output_file, "w") as wf:
            for line in self.data_file:
                print(line.rstrip(), file=wf)
