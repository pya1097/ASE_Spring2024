from data import DATA 
from helper import *
from config import *
import csv
from tests import Tests
import copy

if __name__ == "__main__":
    
    def bayes():
        wme = {'acc': 0, 'datas': {}, 'tries': 0, 'n': 0}
        llearn = lambda data, t: learn(data, t, wme)
        DATA(file_path, llearn)
        # print("Accuracy :", round((wme['acc']/wme['tries'])*100,2)," %")
        return round((wme['acc']/wme['tries'])*100,2)

    def learn(data, row, my):
        my['n'] += 1
        kl = row.cells[data.cols.klass.at]
        if my['n'] > 10:
            my['tries'] += 1
            my['acc'] += 1 if kl == row.likes(my['datas'])[0] else 0
        my['datas'][kl] = my['datas'].get(kl, DATA(data.cols.names))
        my['datas'][kl].add(row.cells)
    
    def km():
        resp = ""
        best = 0
        final_k =0
        final_m =0
        for k in range(0,4):
            the['k']=k
            for m in range(0,4):
                the['m'] = m
                s = bayes()
                resp += "Accuracy for k = "+str(k)+" and m = "+str(m)+" is :"+str(s)+"% \n"
                if(s>=best):
                    best = s
                    final_k = k
                    final_m = m
        
        resp+= "Accuracy for the dataset "+the['file']+" is best for k="+str(final_k)+" and m="+str(final_m)+" with accuracy of "+str(best)+"%"
        return resp
    

    file_path = the['file'] #'w2/data/auto93.csv'
    data = DATA(file_path)

    resp = km()
    print(resp)
    with open('w3/w3_diabetes.out', 'w', newline='') as file:
        file.write(resp)
    

    if the['help']:
        print(help_str)
    else:
        if the['test']:
            tests = Tests()
            tests.inp_test(the,inp_test_map)

       





    