import math
from config import the
from helper import *

class ROW:
    # Initializing ROW instance
    def __init__(self, t):
        self.cells = t

    # Distance to best values (and _lower_ is _better_).
    def d2h(self, data):
        d, n, p = 0, 0, the['p']
        for col in data.cols.y.values():
            x = self.cells[col.at-1]
            if x is None:
                print("?")
            else:
                n += 1
                d += abs(col.heaven - col.norm(self.cells[col.at-1])) ** p
        return (d / n) ** (1 / p)
    
    # Minkowski dsitance (the.p=1 is taxicab/Manhattan; the.p=2 is Euclidean)
    def dist(self, other, data):
        d, n, p = 0, 0, the['p']
        for col in data.cols.x.values():
            n += 1
            d += col.dist(self.cells[col.at-1], other.cells[col.at-1]) ** p
        return (d / n) ** (1 / p)

    def neighbors(self, data, rows=None):
        return keysort(rows or data.rows, fun=lambda row: self.dist(row, data))


    #Finding out how much a row likes the data
    def like(self, data, n, nHypotheses, the):
        # print(the)
        prior = (len(data.rows) + the['k']) / (n + the['k'] * nHypotheses)
        out = math.log(prior)

        for col in data.cols.x:
            v = self.cells[col.at]
            if v != "?":
                inc = col.like(v, prior, the)
                if inc == 0:
                    out += float('-inf')
                else:
                    out += math.log(inc)

        return math.exp(1) ** out
    
    # Classifier
    def likes(self,datas):
        n, nHypotheses = 0, 0
        most, out = None, None
        # print(the)

        for k, data in datas.items():
            n += len(data.rows)
            nHypotheses += 1

        for k, data in datas.items():
            tmp = self.like(data, n, nHypotheses, the)
            if most is None or tmp > most:
                most, out = tmp, k

        return out, most
