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
        # print("Accuracy :", round((wme['acc']/wme['tries'])*100,2)," %")
        return str(round((wme['acc']/wme['tries'])*100,2))

    def learn(data, row, my):
        my['n'] += 1
        kl = row.cells[data.cols.klass.at]
        if my['n'] > 10:
            my['tries'] += 1
            my['acc'] += 1 if kl == row.likes(my['datas'])[0] else 0
        my['datas'][kl] = my['datas'].get(kl, DATA(data.cols.names))
        my['datas'][kl].add(row.cells)
    

    file_path = the['file'] #'w2/data/auto93.csv'
    data = DATA(file_path)

    if(the['file']=='data/diabetes.csv' or the['file']=='data/weather.csv'):
        resp = bayes()
            # Save results to a file
        with open('w3_task03.out', 'w', newline='') as file:
            file.write("Accuracy of the bayes classifier for the dataset "+the['file']+" is :"+resp)
           
    elif(the['file']=='/data/soybean.csv'):
        print("hello")



    if the['help']:
        print(help_str)
    else:
        if the['test']:
            tests = Tests()
            tests.inp_test(the,inp_test_map)

       





    