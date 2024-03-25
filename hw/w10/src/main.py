from data import DATA 
from helper import *
from config import *
import random
#from stats import SAMPLE, eg0
from ranges import Range
from rules import RULES


def _ranges1(col, rowss, the):
    out, nrows = {}, 0
    for y, rows in rowss.items():
        nrows += len(rows)
        for row in list(rows):
            x = row.cells[col.at]
            if x != "?":
                bin = col.bin(x)
                if bin not in out:
                    out[bin] = Range(col.at, col.txt, x)
                out[bin].add(x, y)
    out = list(out.values())
    out.sort(key=lambda r: r.x['lo'])
    return out if hasattr(col, 'has') else _mergeds(out, nrows / the['bins'])

def _ranges(cols, rowss, the):
    t = []
    for col in cols:
        for range in _ranges1(col, rowss, the):
            t.append(range)
    return t

def _mergeds(ranges, tooFew):
    t = []
    i = 1
    while i <= len(ranges):
        a = ranges[i-1]
        if i < len(ranges):
            both = a.merged(ranges[i], tooFew)
            if both:
                a = both
                i += 1
        t.append(a)
        i += 1
    if len(t) < len(ranges):
        return _mergeds(t, tooFew)
    for i in range(1, len(t)):
        t[i].x['lo'] = t[i - 1].x['hi']
    t[0].x['lo'] = -math.inf
    t[-1].x['hi'] = math.inf
    return t


def eg_rules2(the):
    for _ in range(1, 2):
        d = DATA(the['file'])
        tmp = shuffle(d.rows)
        train = d.clone(tmp[:len(tmp) // 2])
        test = d.clone(tmp[len(tmp) // 2:])
        test.rows.sort(key=lambda row: row.d2h(d))
        test.rows = shuffle(test.rows)
        best0, rest, evals1 = train.branch(the['d'])
        best, _, evals2 = best0.branch(the['D'])
        LIKE = best.rows
        HATE = slice(shuffle(rest.rows), 1, 3 * len(LIKE))
        rowss = {'LIKE': LIKE, 'HATE': HATE}
        test.rows = shuffle(test.rows)
        random = test.clone(slice(test.rows, 1, int(evals1 + evals2 + the['D'])))
        random.rows.sort(key=lambda row: row.d2h(d))
        for i, rule in enumerate(RULES(_ranges(train.cols.x, rowss, the), "LIKE", rowss, the=the).sorted):
            result = train.clone(rule.selects(test.rows))
            if len(result.rows) > 0:
                result.rows.sort(key=lambda row: row.d2h(d))
                print(roundoff(rule.scored), o(result.mid().cells), "\t", rule.show())


if __name__ == "__main__":
    file_path = the['file']

    if the['help']:
        print(help_str)   

    
    d = DATA(the['file'])

    eg_rules2(the=the)

    # best, rest, _ = d.branch()
    # LIKE = best.rows
    # HATE = slice(random.sample(rest.rows, min(3 * len(LIKE), len(rest.rows))))
    # def score(range_, the):
    #     return range_.score("LIKE", len(LIKE), len(HATE), the=the)
    # print()
    # print("PART - 1")
    # t = []
    # for col in list(d.cols.x):
    #     print("")
    #     for range_ in _ranges1(col, {"LIKE": LIKE, "HATE": HATE}, the=the):
    #         temp_x = {'hi':range_.x['hi'], 'lo':range_.x['lo']}
    #         temp_y = {}
    #         if 'HATE' in range_.y:
    #             temp_y['HATE'] = range_.y['HATE']
    #         if 'LIKE' in range_.y:
    #             temp_y['LIKE'] = range_.y['LIKE']
    #         d = {'at':(range_.at)+1, 'scored':range_.scored, 'txt':range_.txt, 'x':temp_x, 'y':temp_y}
    #         print(d)
    #         t.append(range_)
    # t.sort(key=lambda a: score(a, the), reverse=True)
    # max_score = score(t[0], the=the)
    # print("\n\nPART - 2")
    # print("\n#scores:\n")
    # for v in t[:int(the['Beam'])]:
    #     if score(v, the) > max_score * 0.1:
    #         temp_x = {'hi':v.x['hi'], 'lo':v.x['lo']}
    #         temp_y = {}
    #         if 'HATE' in v.y:
    #             temp_y['HATE'] = v.y['HATE']
    #         if 'LIKE' in v.y:
    #             temp_y['LIKE'] = v.y['LIKE']
    #         d_v = {'at':(v.at)+1, 'scored':v.scored, 'txt':v.txt, 'x':temp_x, 'y':temp_y}
    #         print("{:.2f}".format(roundoff(score(v,the), 2)), d_v)
    # print({"HATE": len(HATE),"LIKE": len(LIKE),})
