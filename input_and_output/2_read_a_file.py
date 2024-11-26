#!/usr/bin/env python3
def read_a_file(filename):
    with open(filename, 'r') as file:
        content = file.readlines()
        for count, line in enumerate(content, start=1):
            if len(content) == 1:
                return line
            if count == 3:
                return line



if __name__ == "__main__":
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = f"{dir_path}/data.txt"
    print(read_a_file(file_name))

