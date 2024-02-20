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
        # print("Task 1:")
        # print()
        # for row in rows_sort:
        #     if(row_num % 30 == 1):
        #         print(row_num, row.cells, roundoff(row_one.dist(row, data)))    
        #     row_num += 1
    

    data_new = DATA(the['file'])
    #DATA.far(the, data_new)

    print("Task 1: Implementing the recursive tree\n")
    t, evals = data_new.tree(True)
    t.show()
    print("evals: ", evals)
    print()

    print("Task 2: Optimization output - Single Descent\n")
    best, rest, evals = data_new.branch()
    print("centroid of output cluster: ")
    print(o(best.mid().cells), o(rest.mid().cells))
    print("evals: ", evals)
    print()

    print("Task 3: Double tap\n")
    best1, rest, evals1 = data_new.branch(32)
    best2, _, evals2 = best1.branch(4)
    print("median and best found in that four: ")
    print(o(best2.mid().cells), o(rest.mid().cells))
    print("evals: ",evals1 + evals2)

