from data import DATA 
from helper import *
from config import *
from tests import Tests
import random


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

def gate():
        budget0, budget, some = 4, 10, 0.5        
        randomSeeds = random.sample(range(15000),20)
        for randomSeed in randomSeeds:
            d = DATA(file_path) #loads the data
            d.gate(randomSeed,budget0, budget, some)

        print('\n'.join(map(str, DATA.list_1)))
        print('\n')
        print('\n'.join(map(str, DATA.list_2)))
        print('\n')
        print('\n'.join(map(str, DATA.list_3)))
        print('\n')
        print('\n'.join(map(str, DATA.list_4)))
        print('\n')
        print('\n'.join(map(str, DATA.list_5)))
        print('\n')
        print('\n'.join(map(str, DATA.list_6)))

        with open('../../w4/w4.out', 'w') as file:
            for sublist in DATA.list_1:
                file.write(sublist + '\n')
            for sublist in DATA.list_2:
                file.write(sublist + '\n')
            for sublist in DATA.list_3:
                file.write(sublist + '\n')
            for sublist in DATA.list_4:
                file.write(sublist + '\n')
            for sublist in DATA.list_5:
                file.write(sublist + '\n')
            for sublist in DATA.list_6:
                file.write(sublist + '\n')
             


if __name__ == "__main__":
    
    print("HI in main")
    file_path = the['file']
    gate()
    

    if the['help']:
        print(help_str)
    else:
        if the['test']:
            tests = Tests()
            tests.inp_test(the,inp_test_map)