from data import DATA 
from helper import *
from config import *
import random


if __name__ == "__main__":
    file_path = the['file']

    if the['help']:
        print(help_str)
    else:
        data = DATA(the['file'])
        row_one = data.rows[0]
        rows_sort = row_one.neighbors(data=data)
        row_num = 1
        print("Task 1:")
        print()
        for row in rows_sort:
            if(row_num % 30 == 1):
                print(row_num, row.cells, roundoff(row_one.dist(row, data)))    
            row_num += 1
    

    data_new = DATA(the['file'])
    DATA.far(the, data_new)