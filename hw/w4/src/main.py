from data import DATA 
from helper import *
from config import *
from tests import Tests
import random

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

    def gate():
        budget0, budget, some = 4, 10, 0.5
        # print(the['seed'])
        d = DATA(file_path)

        # def sayd(row, txt):
        #     print(o(row.cells), txt, roundoff(row.d2h(d)))

        # def say(row, txt):
        #     print(o(row.cells), txt)

        # print(o(d.cols.names), "about", "d2h")
        # print("#overall")  # -------------------------------------
        # sayd(d.mid(), "mid")
        # say(d.div(), "div")
        # say(d.small(), f"small=div*{the['cohen']}")
        # print("#generality")  # ----------------------------------
        stats, bests = d.gate(budget0, budget, some)
        # for i, stat in enumerate(stats):
        #     sayd(stat, i + budget0)
        # print("#specifically")  # ----------------------------------------------------------
        # for i, best in enumerate(bests):
        #     sayd(best, i + budget0)
        # print("#optimum")  # ------------------------------------------------------
        # d.rows.sort(key=lambda row: row.d2h(d))
        # sayd(d.rows[0], len(d.rows))
        # print("#random")  # ------------------------------------------------------
        # rows = random.sample(d.rows, len(d.rows))
        # rows = rows [:int(math.log(0.05) / math.log(1 - the['cohen'] / 6))]
        # rows.sort(key=lambda row: row.d2h(d))
        # sayd(rows[0], 1)
    
    file_path = the['file'] #'w2/data/auto93.csv'
    # data = DATA(file_path)
    gate()
    # resp = km()
    # print(resp)
    # if 'diabetes.csv' in the['file']:
    #     with open('w3/w3_diabetes.out', 'w', newline='') as file:
    #         file.write(resp)
    # elif 'soybean.csv' in the['file']:
    #     with open('w3/w3_soybean.out', 'w', newline='') as file:
    #         file.write(resp)
    

    if the['help']:
        print(help_str)
    else:
        if the['test']:
            tests = Tests()
            tests.inp_test(the,inp_test_map)