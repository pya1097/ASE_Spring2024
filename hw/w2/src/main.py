from data import DATA 
from helper import *
from config import *
import csv
from tests import Tests

if __name__ == "__main__":
    # Configuring input arguments
    inp, s_inp = settings(help_str)

    # Running main
    file_path = inp['file'] #'w2/data/auto93.csv'
    data = DATA(file_path)
    stats = data.stats()
    print('-----------------Output-----------------')
    print(stats)

    # Save results to a file
    with open('w2/w2.out', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([str(stats)])

    # Running tests
    # tests = Tests()
    if inp['help']:
        print(help_str)
    else:
        if inp['test']:
            tests = Tests()
            tests.inp_test(inp,inp_test_map)