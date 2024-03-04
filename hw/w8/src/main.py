from data import DATA 
from helper import *
from config import *
import random, statistics
from stats import SAMPLE, eg0

def hw7_part2(the):
    print("\n")
    print("\n")
    d = DATA(src = the['file'])
    print("date:{}\nfile:{}\nrepeat:{}\nseed:{}\nrows:{}\ncols:{}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),the['file'],"20",the['seed'],len(d.rows), len(d.rows[0].cells)))
    sortedRows =  sorted(d.rows, key=lambda x: x.d2h(d))
    print(f"best: {o(sortedRows[0].d2h(d),n=2)}")
    all = base(d)
    print(f"tiny: {o(statistics.stdev(all)*0.35,n=2)}")
    print("#base #bonr9 #rand9 #bonr15 #rand15 #bonr20 #rand20 #rand358 ")
    eg0([
        SAMPLE(randN(d,9, the=the), "rand9"),
        SAMPLE(randN(d,15, the=the), "rand15"),
        SAMPLE(randN(d,20, the=the), "rand20"), 
        SAMPLE(randN(d,358, the=the), "rand358"), 
        SAMPLE(bonrN(d,9, the=the), "bonr9"),
        SAMPLE(bonrN(d,15,the=the), "bonr15"),
        SAMPLE(bonrN(d,20, the=the), "bonr20"),
        SAMPLE(base(d), "base")
    ])

def base(d):
    baseline_output = [row.d2h(d) for row in d.rows]
    return baseline_output

def randN(d, n, the):
    random.seed(the['seed'])
    rand_arr = []
    for _ in range(20):
        rows = d.rows
        random.shuffle(rows)
        rowsN = random.sample(rows,n)
        rowsN.sort(key=lambda row: row.d2h(d))
        rand_arr.append(round(rowsN[0].d2h(d),2))

    return rand_arr

def bonrN(d, n, the):
    bonr_arr = []
    for _ in range(20):
        _,_, best_stats = d.gate(the['seed'], 4, n-4, 0.5)
        bonr_arr.append(best_stats[1])

    return bonr_arr

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

    random_seeds = random.sample(range(100),20)
    # random_seeds = [21, 39]
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
    hw7_part2(the)

    


