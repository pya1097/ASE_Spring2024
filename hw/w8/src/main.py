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
    

    data_new = DATA(the['file'])
    mid_100, div_100 = data_new.mid_div()

    # random_seeds = random.sample(range(100),20)
    random_seeds = [21, 39]
    smo_output = []
    any50_output = []
    budget0, budget, some = 4, 5, 0.5  
    for random_seed in random_seeds: 
        d =DATA(the['file'])
        _,_, a = d.gate(random_seed, budget0, budget, some)
        smo_output.append(a)
        any50_output.append(d.any50(random_seed))
   
    best_100 = d.best_100(random_seed)

    print_centroid(d,mid_100, div_100, the)
    print("#")
    print_smo(smo_output)
    print("#")
    print_any50(any50_output)
    print("#")
    print(format_row("100%",best_100[0],best_100[1]))

    
    

