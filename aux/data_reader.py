import numpy as np

def open_file(file_name):
    data = []
    file = open(file_name, 'r')
    for line in file:
        data.append(line.split())
    return np.asarray(data, dtype = int)


def open_file_txt(file_name):
    file = open(file_name, 'r')
    data = file.readlines()
    return data[0][0:len(data[0]) - 1]