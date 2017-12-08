from aux import data_reader as reader
import numpy as np


def run_Corruption_Checksum_1(spreadsheet):
    dff = [int(max(spreadsheet[i]))-int(min(spreadsheet[i])) for i in xrange(len(spreadsheet))]
    print 'The solution to ' +str(spreadsheet) + ' spreadsheet is: \n' + str(sum(dff))

def run_Corruption_Checksum_2(spreadsheet):
    res = np.int32(np.asarray([[[j / k for j in spreadsheet_idx if j % k == 0 and j!= k] for k in spreadsheet_idx] for spreadsheet_idx in spreadsheet]).sum()).sum()
    print 'The solution to \n' + str(spreadsheet) + ' spreadsheet is: \n' + str(res)

if __name__ == '__main__':
    input = reader.open_file('./file_directory/Day_2.txt')

    run_Corruption_Checksum_1(input)

    run_Corruption_Checksum_2(input)