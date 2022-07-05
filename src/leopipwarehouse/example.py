import math
import numpy as np
import pandas as pd

def pi_add_one(number):
    arr = np.array([2,4,6,8])
    framework = pd.DataFrame(arr)
    print(framework)
    return number + math.pi + 1

def read_file(filename):
    with open(filename) as reader:
        line = reader.readline()
        while line != '':  # The EOF char is an empty string
            print(line, end='')
            line = reader.readline()

def write_file(filename, content):
    with open(filename, 'w') as writer:
        writer.writelines(content)

# if __name__ == "__main__":
    # read_file('awg.wfm')
    # write_file('awg.wfm', 'hi')
    # pi_add_one(2)
    





