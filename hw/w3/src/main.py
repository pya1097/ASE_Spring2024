from data import DATA 
from helper import *
from config import *
import csv
from tests import Tests

if __name__ == "__main__":
    
    def bayes():
        wme = {'acc': 0, 'datas': {}, 'tries': 0, 'n': 0}
        llearn = lambda data, t: learn(data, t, wme)
        DATA(file_path, llearn)
        print("Accuracy :", (wme['acc']/wme['tries'])*100)

    def learn(data, row, my):
        my['n'] += 1
        kl = row.cells[data.cols.klass.at]
        if my['n'] > 10:
            my['tries'] += 1
            my['acc'] += 1 if kl == row.likes(my['datas'])[0] else 0
        print(data.cols.names)
        my['datas'][kl] = my['datas'].get(kl, DATA(data.cols.names))
        print("my['datas'][kl]",my['datas'][kl])
        my['datas'][kl].add(row['cells'])
    
    # Configuring input arguments
    inp, s_inp = settings(help_str)

    # Running main
    file_path = inp['file'] #'w2/data/auto93.csv'
    data = DATA(file_path)
    # stats = data.stats()
    cls_data = data.classes_data()
    print('-----------------Output-----------------')
    print(cls_data)

    bayes()

    # Save results to a file
    with open('w3.out', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([str(cls_data)])

    # Running tests
    # tests = Tests()
    if inp['help']:
        print(help_str)
    else:
        if inp['test']:
            tests = Tests()
            tests.inp_test(inp,inp_test_map)

       





    