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
        for row, dist in rows_sort:
            if(row_num % 30 == 1):
                print(row_num, row.cells, roundoff(dist))
            
            row_num += 1